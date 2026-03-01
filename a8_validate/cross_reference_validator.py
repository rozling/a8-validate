"""Cross-reference validator module for Assimil8or preset files."""

import re


class CrossReferenceError(Exception):
    """Base exception for cross-reference validation errors."""

    pass


class ChannelModeError(CrossReferenceError):
    """Exception raised for invalid channel mode configurations."""

    pass


class LoopConfigurationError(CrossReferenceError):
    """Exception raised for invalid loop configurations."""

    pass


class ZoneVoltageRangeError(CrossReferenceError):
    """Exception raised for invalid zone voltage range configurations."""

    pass


class CVInputReferenceError(CrossReferenceError):
    """Exception raised for invalid CV input references."""

    pass


# Regex patterns for validation
CV_INPUT_PATTERN = r"^(Off|[0-8][A-C])$"


def validate_relationships(preset_data):
    """
    Validate parameter relationships in a preset.

    Args:
        preset_data: Dictionary containing the preset data

    Raises:
        CrossReferenceError: If validation fails
    """
    for preset_key, preset_value in preset_data.items():
        _validate_preset_relationships(preset_value)


def _validate_preset_relationships(preset):
    """
    Validate relationships within a preset.

    Args:
        preset: Dictionary containing the preset data

    Raises:
        CrossReferenceError: If validation fails
    """
    # Collect all channels
    channels = {}
    for key, value in preset.items():
        if key.startswith("Channel "):
            channel_number = int(key.split(" ")[1])
            channels[channel_number] = value

    # Validate crossfade groups
    _validate_crossfade_groups(preset, channels)

    # Validate channel modes
    _validate_channel_modes(channels)

    # Validate CV inputs
    _validate_cv_inputs(preset)

    # Validate each channel's internal relationships
    for channel_number, channel_data in channels.items():
        _validate_channel_relationships(channel_data, channel_number)


def _validate_crossfade_groups(preset, channels):
    """
    Validate crossfade group configurations.

    Args:
        preset: Dictionary containing the preset data
        channels: Dictionary of channel numbers to channel data

    Raises:
        CrossReferenceError: If validation fails
    """
    # Check for crossfade groups
    groups = {"A": [], "B": [], "C": [], "D": []}

    # Collect channels in each group
    for channel_number, channel_data in channels.items():
        if "XfadeGroup" in channel_data:
            group = channel_data["XfadeGroup"]
            if group in groups:
                groups[group].append(channel_number)

    # Validate each group
    for group, channel_numbers in groups.items():
        if channel_numbers:
            # Check that there are at least 2 channels in the group
            if len(channel_numbers) < 2:
                raise CrossReferenceError(
                    f"Crossfade Group {group} with XfadeGroup parameter must have at least 2 channels, "
                    f"but only has {len(channel_numbers)}"
                )

            # Check that the corresponding CV input exists
            cv_param = f"Xfade{group}CV"
            if cv_param not in preset:
                raise CrossReferenceError(f"{cv_param} is required for XfadeGroup {group}")


def _validate_channel_modes(channels):
    """
    Validate channel mode configurations.

    Args:
        channels: Dictionary of channel numbers to channel data

    Raises:
        ChannelModeError: If validation fails
    """
    # Check all channels for valid modes
    for channel_number, channel_data in channels.items():
        if "ChannelMode" in channel_data:
            mode = channel_data["ChannelMode"]

            # Link (1) and Cycle (3) modes require a Master channel above them
            if mode in [1, 3]:  # Link or Cycle
                # Check if there's a Master channel above
                has_master_above = False
                for i in range(1, channel_number):
                    if i in channels:
                        above_mode = channels[i].get("ChannelMode", 0)
                        if above_mode == 0:  # Master mode (or default)
                            has_master_above = True
                            break

                if not has_master_above:
                    mode_name = "Link" if mode == 1 else "Cycle"
                    raise ChannelModeError(
                        f"Channel {channel_number} is in {mode_name} mode but has no Master channel above it"
                    )


def _validate_cv_inputs(preset):
    """
    Validate CV input references.

    Args:
        preset: Dictionary containing the preset data

    Raises:
        CVInputReferenceError: If validation fails
    """
    # Check all CV input references in the preset
    for key, value in preset.items():
        if any(key.startswith(prefix) for prefix in ["XfadeACV", "XfadeBCV", "XfadeCCV", "XfadeDCV", "Data2asCV"]):
            if not isinstance(value, str):
                raise CVInputReferenceError(f"{key} must be a string, got {type(value).__name__}")

            if not re.match(CV_INPUT_PATTERN, value):
                raise CVInputReferenceError(f"{key} must be in format '1A'-'8C' or 'Off', got {value}")


def _validate_channel_relationships(channel_data, channel_number):
    """
    Validate relationships within a channel.

    Args:
        channel_data: Dictionary containing the channel data
        channel_number: Channel number

    Raises:
        CrossReferenceError: If validation fails
    """
    # Validate loop settings
    _validate_loop_settings(channel_data, channel_number)

    # Validate sample start/end
    _validate_sample_boundaries(channel_data, channel_number)

    # Collect all zones
    zones = {}
    for key, value in channel_data.items():
        if key.startswith("Zone "):
            zone_number = int(key.split(" ")[1])
            zones[zone_number] = value

    # Validate zone voltage ranges
    _validate_zone_voltage_ranges(zones, channel_number)

    # Validate each zone's internal relationships
    for zone_number, zone_data in zones.items():
        _validate_zone_relationships(zone_data, channel_data, channel_number, zone_number)


def _validate_loop_settings(channel_data, channel_number):
    """
    Validate loop settings in a channel with parameter inheritance support.

    This method implements a flexible parameter inheritance model for loop settings:
    - When LoopMode is enabled at the channel level, loop parameters can be defined:
      1. At the channel level (applies to all zones)
      2. Within individual zones (can override channel-level settings)

    Validation rules:
    - If loop parameters are explicitly provided, they must be consistent
    - Absence of explicit loop parameters implies a default "full sample loop"
    - LoopLength can be defined alone (LoopStart defaults to 0)
    - LoopStart requires LoopLength to be defined

    Args:
        channel_data: Dictionary containing the channel data
        channel_number: Channel number

    Raises:
        LoopConfigurationError: If loop parameters are inconsistently defined
    """
    if "LoopMode" in channel_data and channel_data["LoopMode"] != 0:
        # Check for zone-level loop parameters
        zone_loop_params = []
        for key, value in channel_data.items():
            if key.startswith("Zone "):
                if "LoopStart" in value or "LoopLength" in value:
                    zone_loop_params.append(value)

        # If explicit parameters exist, validate them
        all_loop_params = [channel_data] + zone_loop_params
        for params in all_loop_params:
            # Check for partial loop parameter definitions
            # LoopLength can be defined alone (LoopStart defaults to 0)
            # But if LoopStart is defined, LoopLength must also be defined
            if "LoopStart" in params and "LoopLength" not in params:
                raise LoopConfigurationError(f"Channel {channel_number}: LoopStart requires LoopLength to be defined")

            # Validate LoopLengthIsEnd flag consistency with LoopMode
            if "LoopLengthIsEnd" in params:
                is_end = params["LoopLengthIsEnd"]
                loop_mode = params.get("LoopMode", channel_data.get("LoopMode"))

                if loop_mode == 1 and is_end != 1:
                    raise LoopConfigurationError(
                        f"Channel {channel_number}: LoopMode 1 requires LoopLengthIsEnd to be 1"
                    )

                if loop_mode == 2 and is_end != 0:
                    raise LoopConfigurationError(
                        f"Channel {channel_number}: LoopMode 2 requires LoopLengthIsEnd to be 0"
                    )


def _validate_sample_boundaries(channel_data, channel_number):
    """
    Validate sample start and end points.

    Args:
        channel_data: Dictionary containing the channel data
        channel_number: Channel number

    Raises:
        CrossReferenceError: If validation fails
    """
    if "SampleStart" in channel_data and "SampleEnd" in channel_data:
        if channel_data["SampleStart"] >= channel_data["SampleEnd"]:
            raise CrossReferenceError(
                f"Channel {channel_number}: SampleStart ({channel_data['SampleStart']}) is greater than "
                f"SampleEnd ({channel_data['SampleEnd']})"
            )


def _validate_zone_voltage_ranges(zones, channel_number):
    """
    Validate zone voltage ranges.

    Args:
        zones: Dictionary of zone numbers to zone data
        channel_number: Channel number

    Raises:
        ZoneVoltageRangeError: If validation fails
    """
    if not zones:
        return

    # Check zone voltage ordering
    zone_voltages = []
    for zone_number in sorted(zones.keys()):
        zone_data = zones[zone_number]

        # Get MinVoltage if defined, or assume +5.00 for the first zone
        min_voltage = zone_data.get("MinVoltage", "+5.00" if zone_number == 1 else None)

        if min_voltage is None:
            continue  # Skip this zone if MinVoltage is not defined

        # Convert to float
        try:
            min_voltage_value = float(min_voltage)
        except ValueError:
            # Skip if not a valid float (schema validation will catch this)
            continue

        zone_voltages.append((zone_number, min_voltage_value))

    # Check that voltages are in descending order
    for i in range(len(zone_voltages) - 1):
        zone1_num, zone1_volt = zone_voltages[i]
        zone2_num, zone2_volt = zone_voltages[i + 1]

        if zone1_volt <= zone2_volt:
            raise ZoneVoltageRangeError(
                f"Channel {channel_number}: Zone {zone1_num} voltage ({zone1_volt}) must be "
                f"higher than Zone {zone2_num} voltage ({zone2_volt})"
            )


def _validate_zone_relationships(zone_data, channel_data, channel_number, zone_number):
    """
    Validate relationships within a zone.

    Args:
        zone_data: Dictionary containing the zone data
        channel_data: Dictionary containing the channel data
        channel_number: Channel number
        zone_number: Zone number

    Raises:
        CrossReferenceError: If validation fails
    """
    # Validate loop settings if overridden at zone level
    if "LoopMode" in zone_data and zone_data["LoopMode"] != 0:
        # Check if LoopStart and LoopLength are defined at zone level
        zone_loop_start = zone_data.get("LoopStart")
        zone_loop_length = zone_data.get("LoopLength")

        # Check if LoopStart and LoopLength are defined at channel level
        channel_loop_start = channel_data.get("LoopStart")
        channel_loop_length = channel_data.get("LoopLength")

        # Require LoopLength (LoopStart defaults to 0 if not defined)
        # But if LoopStart is defined, it requires LoopLength
        if zone_loop_start and not (zone_loop_length or channel_loop_length):
            raise LoopConfigurationError(
                f"Channel {channel_number}, Zone {zone_number}: LoopStart requires LoopLength to be defined"
            )
        if channel_loop_start and not (zone_loop_length or channel_loop_length):
            raise LoopConfigurationError(
                f"Channel {channel_number}, Zone {zone_number}: LoopStart requires LoopLength to be defined"
            )

        if not (zone_loop_length or channel_loop_length):
            raise LoopConfigurationError(
                f"Channel {channel_number}, Zone {zone_number} has LoopMode {zone_data['LoopMode']} "
                f"but LoopLength is not defined"
            )

    # Validate sample start and end points if defined at zone level
    if "SampleStart" in zone_data and "SampleEnd" in zone_data:
        sample_start = zone_data["SampleStart"]
        sample_end = zone_data["SampleEnd"]
        if sample_start >= sample_end:
            raise CrossReferenceError(
                f"Channel {channel_number}, Zone {zone_number}: SampleStart ({sample_start}) "
                f"is greater than SampleEnd ({sample_end})"
            )
