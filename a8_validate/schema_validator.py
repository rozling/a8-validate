"""Schema validator module for Assimil8or preset files."""

import re


class SchemaValidationError(Exception):
    """Base exception for schema validation errors."""

    def __init__(self, message, path=None):
        super().__init__(message)
        self.path = path


class InvalidParameterError(SchemaValidationError):
    """Exception raised for invalid parameter names."""

    pass


class InvalidValueError(SchemaValidationError):
    """Exception raised for invalid parameter values."""

    pass


class MissingRequiredParameterError(SchemaValidationError):
    """Exception raised for missing required parameters."""

    pass


# Define schema for preset parameters
PRESET_SCHEMA = {
    "Name": {"type": "string_or_number", "required": True, "max_length": 47},
    "Data2asCV": {"type": "cv_input", "required": False},
    "XfadeACV": {"type": "cv_input", "required": False},
    "XfadeAWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "XfadeBCV": {"type": "cv_input", "required": False},
    "XfadeBWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "XfadeCCV": {"type": "cv_input", "required": False},
    "XfadeCWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "XfadeDCV": {"type": "cv_input", "required": False},
    "XfadeDWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "MidiSetup": {"type": "integer", "required": False, "min": 1, "max": 16},
}

# Define schema for channel parameters
CHANNEL_SCHEMA = {
    "ChannelMode": {"type": "integer", "required": False, "values": [0, 1, 2, 3]},
    "Pitch": {"type": "float", "required": False, "min": -96.0, "max": 60.0},
    "Level": {"type": "float", "required": False, "min": -90.0, "max": 6.0},
    "Pan": {"type": "float", "required": False, "min": -1.0, "max": 1.0},
    "PanMod": {"type": "cv_input_with_amount", "required": False},
    "MixLevel": {"type": "float", "required": False, "min": -90.0, "max": 6.0},
    "PlayMode": {"type": "integer", "required": False, "values": [0, 1]},
    "AutoTrigger": {"type": "integer", "required": False, "values": [0, 1]},
    "LoopMode": {"type": "integer", "required": False, "values": [0, 1, 2]},
    "Reverse": {"type": "integer", "required": False, "values": [0, 1]},
    "Attack": {"type": "float", "required": False, "min": 0.0, "max": 99.0},
    "Release": {"type": "float", "required": False, "min": 0.0, "max": 99.0},
    "Bits": {"type": "float", "required": False, "min": 1.0, "max": 32.0},
    "Aliasing": {"type": "integer", "required": False, "min": 0, "max": 100},
    "SpliceSmoothing": {"type": "integer", "required": False, "values": [0, 1]},
    "PitchCV": {"type": "cv_input_with_amount", "required": False},
    "LinFM": {"type": "cv_input_with_amount", "required": False},
    "LinAM": {"type": "cv_input_with_amount", "required": False},
    "LinAMisExtEnv": {"type": "integer", "required": False, "values": [0, 1]},
    "ExpFM": {"type": "cv_input_with_amount", "required": False},
    "ExpAM": {"type": "cv_input_with_amount", "required": False},
    "PhaseCV": {"type": "cv_input_with_amount", "required": False},
    "PMSource": {"type": "pm_source", "required": False},
    "PMIndex": {"type": "float", "required": False, "min": 0.0, "max": 1.0},
    "PMIndexMod": {"type": "cv_input_with_amount", "required": False},
    "LoopStart": {"type": "integer", "required": False, "min": 0},
    "LoopLength": {"type": "float", "required": False, "min": 4.0},
    "LoopLengthIsEnd": {"type": "integer", "required": False, "values": [0, 1]},
    "LoopStartMod": {"type": "cv_input_with_amount", "required": False},
    "LoopLengthMod": {"type": "cv_input_with_amount", "required": False},
    "SampleStart": {"type": "integer", "required": False, "min": 0},
    "SampleEnd": {"type": "integer", "required": False, "min": 1},
    "SampleStartMod": {"type": "cv_input_with_amount", "required": False},
    "SampleEndMod": {"type": "cv_input_with_amount", "required": False},
    "MixMod": {"type": "cv_input_with_amount", "required": False},
    "MixModIsFader": {"type": "integer", "required": False, "values": [0, 1]},
    "BitsMod": {"type": "cv_input_with_amount", "required": False},
    "AliasingMod": {"type": "cv_input_with_amount", "required": False},
    "AttackMod": {"type": "cv_input_with_amount", "required": False},
    "ReleaseMod": {"type": "cv_input_with_amount", "required": False},
    "ZonesCV": {"type": "cv_input", "required": False},
    "ZonesRT": {"type": "integer", "required": False, "values": [0, 1]},
    "XfadeGroup": {"type": "string", "required": False, "values": ["A", "B", "C", "D"]},
}

# Define schema for zone parameters
ZONE_SCHEMA = {
    "Sample": {"type": "string", "required": True},
    "MinVoltage": {"type": "voltage", "required": False, "min": -5.0, "max": 5.0},
    "MaxVoltage": {"type": "voltage", "required": False, "min": -5.0, "max": 5.0},
    "LevelOffset": {"type": "float", "required": False, "min": -90.0, "max": 6.0},
    "PitchOffset": {"type": "float", "required": False, "min": -96.0, "max": 60.0},
    "Side": {"type": "integer", "required": False, "values": [0, 1]},
    "LoopMode": {"type": "integer", "required": False, "values": [0, 1, 2]},
    "LoopStart": {"type": "integer", "required": False, "min": 0},
    "LoopLength": {"type": "float", "required": False, "min": 4.0},
    "SampleStart": {"type": "integer", "required": False, "min": 0},
    "SampleEnd": {"type": "integer", "required": False, "min": 1},
    "Bits": {"type": "float", "required": False, "min": 1.0, "max": 32.0},
    "Smooth": {"type": "integer", "required": False, "values": [0, 1]},
}

# Regex patterns for validation
CV_INPUT_PATTERN = r"^(Off|[0-8][A-C])$"
CV_INPUT_WITH_AMOUNT_PATTERN = r"^(Off|[0-8][A-C]) [-+]?[0-9]*\.?[0-9]+$"
VOLTAGE_PATTERN = r"^[-+]?[0-9]*\.?[0-9]+$"
PM_SOURCE_PATTERN = r"^([1-8]|Sample Input (Left|Right))$"


def _is_numeric_string(value):
    """Check if a string represents a valid numeric value."""
    if not isinstance(value, str):
        return False
    return bool(re.match(r"^[+-]?\d+(\.\d+)?$", value))


def validate_preset(preset_data, path=()):
    """
    Validate a preset against the schema.

    Note: This function modifies the input preset_data dictionary in place by
    normalizing and validating parameter values. For example, string representations
    of numbers are converted to their numeric types, and the Name parameter is
    converted to a string if provided as a number.

    Args:
        preset_data: Dictionary containing the preset data (will be modified in place)
        path: Tuple representing the path to this preset in the overall structure

    Raises:
        SchemaValidationError: If validation fails
    """
    for preset_key, preset_value in preset_data.items():
        if not preset_key.startswith("Preset "):
            raise InvalidParameterError(
                f"Invalid preset key: {preset_key}", path=path + (preset_key,)
            )

        # Enforce channel count and order
        channel_keys = [k for k in preset_value.keys() if k.startswith("Channel ")]
        channel_numbers = []
        for k in channel_keys:
            try:
                num = int(k.split(" ")[1])
                channel_numbers.append(num)
            except (IndexError, ValueError):
                raise InvalidParameterError(
                    f"Invalid channel key format: {k}", path=path + (preset_key, k)
                )
        if len(channel_numbers) > 8:
            raise SchemaValidationError(
                f"Preset {preset_key} has {len(channel_numbers)} channels, maximum allowed is 8",
                path=path + (preset_key,),
            )
        # Check that channels are in ascending order (but allow non-sequential channels)
        # e.g., [1, 4, 7] is OK, but [4, 1, 7] is not OK
        if channel_numbers != sorted(channel_numbers):
            raise SchemaValidationError(
                f"Channel numbers in {preset_key} must be in ascending order",
                path=path + (preset_key,),
            )
        # Check that all channel numbers are in valid range (1-8)
        if any(num < 1 or num > 8 for num in channel_numbers):
            raise SchemaValidationError(
                f"Channel numbers in {preset_key} must be between 1 and 8",
                path=path + (preset_key,),
            )

        # Validate preset parameters
        for param, value in preset_value.items():
            if param.startswith("Channel "):
                # Validate channel
                channel_number = int(param.split(" ")[1])
                validate_channel(value, channel_number, path=path + (preset_key, param))
            else:
                # Validate preset parameter
                if param not in PRESET_SCHEMA:
                    raise InvalidParameterError(
                        f"Invalid preset parameter: {param}",
                        path=path + (preset_key, param),
                    )

                # Special case: convert Name to string if not already
                if param == "Name" and not isinstance(value, str):
                    value = str(value)

                preset_value[param] = _validate_parameter_value(
                    param,
                    value,
                    PRESET_SCHEMA[param],
                    context=f"{preset_key}",
                    path=path + (preset_key, param),
                )

        # Check for required parameters
        for param, schema in PRESET_SCHEMA.items():
            if schema.get("required", False) and param not in preset_value:
                raise MissingRequiredParameterError(
                    f"Missing required preset parameter: {param}",
                    path=path + (preset_key, param),
                )


def validate_channel(channel_data, channel_number, path=()):
    """
    Validate a channel against the schema.

    Note: This function modifies the input channel_data dictionary in place by
    normalizing and validating parameter values (e.g., converting string numbers
    to numeric types).

    Args:
        channel_data: Dictionary containing the channel data (will be modified in place)
        channel_number: Channel number
        path: Tuple representing the path to this channel in the overall structure

    Raises:
        SchemaValidationError: If validation fails
    """
    # Validate channel parameters
    for param, value in list(channel_data.items()):
        if param.startswith("Zone "):
            # Validate zone
            zone_number = int(param.split(" ")[1])
            validate_zone(value, channel_number, zone_number, path=path + (param,))
        else:
            # Validate channel parameter
            if param not in CHANNEL_SCHEMA:
                raise InvalidParameterError(
                    f"Invalid channel parameter: {param} in Channel {channel_number}",
                    path=path + (param,),
                )

            channel_data[param] = _validate_parameter_value(
                param,
                value,
                CHANNEL_SCHEMA[param],
                context=f"Channel {channel_number}",
                path=path + (param,),
            )

    # Enforce zone count and order
    zone_keys = [k for k in channel_data.keys() if k.startswith("Zone ")]
    zone_numbers = []
    for k in zone_keys:
        try:
            num = int(k.split(" ")[1])
            zone_numbers.append(num)
        except (IndexError, ValueError):
            raise InvalidParameterError(
                f"Invalid zone key format: {k}", path=path + (k,)
            )

    # Require at least one zone per channel
    if len(zone_numbers) == 0:
        raise SchemaValidationError(
            f"Channel {channel_number} must have at least one zone", path=path
        )

    if len(zone_numbers) > 8:
        raise SchemaValidationError(
            f"Channel {channel_number} has {len(zone_numbers)} zones, maximum allowed is 8",
            path=path,
        )
    if sorted(zone_numbers) != list(range(1, len(zone_numbers) + 1)):
        raise SchemaValidationError(
            f"Zone numbers in Channel {channel_number} must be sequential starting from 1",
            path=path,
        )


def validate_zone(zone_data, channel_number, zone_number, path=()):
    """
    Validate a zone against the schema.

    Note: This function modifies the input zone_data dictionary in place by
    normalizing and validating parameter values (e.g., converting string numbers
    to numeric types).

    Args:
        zone_data: Dictionary containing the zone data (will be modified in place)
        channel_number: Channel number
        zone_number: Zone number
        path: Tuple representing the path to this zone in the overall structure

    Raises:
        SchemaValidationError: If validation fails
    """
    # Validate zone parameters
    for param, value in zone_data.items():
        if param not in ZONE_SCHEMA:
            raise InvalidParameterError(
                f"Invalid zone parameter: {param} in Channel {channel_number}, Zone {zone_number}",
                path=path + (param,),
            )

        zone_data[param] = _validate_parameter_value(
            param,
            value,
            ZONE_SCHEMA[param],
            f"Channel {channel_number}, Zone {zone_number}",
            path=path + (param,),
        )

    # Check for required parameters
    for param, schema in ZONE_SCHEMA.items():
        if schema.get("required", False) and param not in zone_data:
            raise MissingRequiredParameterError(
                f"Missing required zone parameter: {param} in Channel {channel_number}, Zone {zone_number}",
                path=path + (param,),
            )


def _validate_parameter_value(param, value, schema, context="", path=()):
    """
    Validate a parameter value against its schema.

    Args:
        param: Parameter name
        value: Parameter value
        schema: Schema for the parameter
        context: Context for error messages (e.g., "Channel 1, Zone 2")
        path: Tuple representing the path to this parameter in the overall structure

    Raises:
        SchemaValidationError: If validation fails
    """
    param_type = schema["type"]
    context_str = f" in {context}" if context else ""

    # For numeric types, allow string representations and convert them
    if param_type in ("integer", "float"):
        if isinstance(value, str):
            try:
                if param_type == "integer":
                    value = int(value)
                else:
                    value = float(value)
            except ValueError:
                raise InvalidValueError(
                    f"Parameter {param}{context_str} must be a {param_type}, "
                    f"got string that cannot be converted: {value}",
                    path=path,
                )

    # Type validation
    if param_type == "string":
        if not isinstance(value, str):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a string, got {type(value).__name__}",
                path=path,
            )
        if "max_length" in schema and len(value) > schema["max_length"]:
            raise InvalidValueError(
                f"Parameter {param}{context_str} exceeds maximum length of {schema['max_length']}",
                path=path,
            )
        if "values" in schema and value not in schema["values"]:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be one of {schema['values']}, got {value}",
                path=path,
            )

    elif param_type == "integer":
        if not isinstance(value, int):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be an integer, got {type(value).__name__}",
                path=path,
            )
        if "min" in schema and value < schema["min"]:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at least {schema['min']}, got {value}",
                path=path,
            )
        if "max" in schema and value > schema["max"]:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at most {schema['max']}, got {value} (outside allowed range)",
                path=path,
            )
        if "values" in schema and value not in schema["values"]:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be one of {schema['values']}, got {value}",
                path=path,
            )

    elif param_type == "float":
        if not isinstance(value, (int, float)):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a numeric type (int or float), "
                f"got {type(value).__name__}. String representations are not allowed.",
                path=path,
            )

        # Range validation for numeric types
        if "min" in schema and value < schema["min"]:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at least {schema['min']}, got {value} (outside allowed range)",
                path=path,
            )
        if "max" in schema and value > schema["max"]:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at most {schema['max']}, got {value} (outside allowed range)",
                path=path,
            )

    elif param_type == "cv_input":
        if not isinstance(value, str):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a string, got {type(value).__name__}",
                path=path,
            )
        if not re.match(CV_INPUT_PATTERN, value):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be in format '1A'-'8C' or 'Off', got {value}",
                path=path,
            )

    elif param_type == "cv_input_with_amount":
        if not isinstance(value, str):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a string, got {type(value).__name__}",
                path=path,
            )
        if not re.match(CV_INPUT_WITH_AMOUNT_PATTERN, value):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be in format '1A 0.50', got {value}",
                path=path,
            )

    elif param_type == "voltage":
        if not isinstance(value, str) and not isinstance(value, (int, float)):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a number or string, got {type(value).__name__}",
                path=path,
            )

        # Convert to string if it's a number
        if isinstance(value, (int, float)):
            value = str(value)

        if not re.match(VOLTAGE_PATTERN, value):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be in format '+5.00' or '-3.50', got {value}",
                path=path,
            )

        # Check range
        try:
            float_val = float(value)
            if "min" in schema and float_val < schema["min"]:
                raise InvalidValueError(
                    f"Parameter {param}{context_str} must be at least {schema['min']}, "
                    f"got {value} (outside allowed range)",
                    path=path,
                )
            if "max" in schema and float_val > schema["max"]:
                raise InvalidValueError(
                    f"Parameter {param}{context_str} must be at most {schema['max']}, "
                    f"got {value} (outside allowed range)",
                    path=path,
                )
        except ValueError:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a valid numeric value, got {value}",
                path=path,
            )

    elif param_type == "pm_source":
        # PMSource accepts numeric values 0-10:
        # 0-7: channels (or 0 = off?)
        # 8: left input
        # 9: right input
        # 10: select CV
        if isinstance(value, int) and 0 <= value <= 10:
            return value

        if isinstance(value, str):
            # Support string representations of numbers
            if value.isdigit():
                int_val = int(value)
                if 0 <= int_val <= 10:
                    return int_val
            # Support legacy string format
            if value in ["Sample Input Left", "Sample Input Right"]:
                return value

        raise InvalidValueError(
            f"Parameter {param}{context_str} must be a numeric value (0-10), "
            f"where 0-7 are channels, 8=left input, 9=right input, 10=select CV. Got {value}",
            path=path,
        )

    return value
