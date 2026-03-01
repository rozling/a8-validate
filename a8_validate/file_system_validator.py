"""File system validator module for Assimil8or preset files."""

import os
import re
import wave
from typing import Optional, Tuple

# Path shape: (preset_key, channel_key?, zone_key?) — tuple of YAML keys for line_map lookup
ValidationPath = Tuple[str, ...]


def _path_to_context(path: ValidationPath) -> str:
    """Build human-readable context string from a validation path."""
    return ", ".join(path) if path else ""


class FileSystemValidationError(Exception):
    """Base exception for file system validation errors."""

    def __init__(self, message: str, path: Optional[ValidationPath] = None):
        super().__init__(message)
        self.path = path


class SampleFileNotFoundError(FileSystemValidationError):
    """Exception raised when a referenced sample file is not found."""

    pass


class InvalidSampleFormatError(FileSystemValidationError):
    """Exception raised when a sample file has an invalid format."""

    pass


class MemoryLimitExceededError(FileSystemValidationError):
    """Exception raised when total memory usage exceeds the limit."""

    pass


class InvalidPresetFilenameError(FileSystemValidationError):
    """Exception raised when a preset filename does not follow the required format."""

    pass


# Maximum memory limit for the Assimil8or (422MB)
MAX_MEMORY_BYTES = 422 * 1024 * 1024


def validate_sample_files(preset_data, folder_path):
    """
    Validate sample files referenced in a preset.

    Args:
        preset_data: Dictionary containing the preset data
        folder_path: Path to the folder containing the sample files

    Raises:
        FileSystemValidationError: If validation fails
    """
    # Get all sample references
    sample_references = _collect_sample_references(preset_data)

    # Validate each sample file
    for path, sample_filename in sample_references:
        _validate_sample_file(preset_data, folder_path, sample_filename, path)

    # Check total memory usage
    total_memory = calculate_total_memory(preset_data, folder_path)
    if total_memory > MAX_MEMORY_BYTES:
        raise MemoryLimitExceededError(
            f"Total memory usage ({total_memory / (1024 * 1024):.2f}MB) "
            f"exceeds the limit of 422MB"
        )


def _collect_sample_references(preset_data):
    """
    Collect all sample references from a preset.

    Args:
        preset_data: Dictionary containing the preset data

    Returns:
        List of tuples (path, sample_filename) where path is (preset_key, channel_key, zone_key)
    """
    sample_references = []

    for preset_key, preset_value in preset_data.items():
        for channel_key, channel_value in preset_value.items():
            if not channel_key.startswith("Channel "):
                continue

            for zone_key, zone_value in channel_value.items():
                if not zone_key.startswith("Zone "):
                    continue

                if "Sample" in zone_value:
                    sample_filename = zone_value["Sample"]
                    path = (preset_key, channel_key, zone_key)
                    sample_references.append((path, sample_filename))

    return sample_references


def _validate_sample_file(preset_data, folder_path, sample_filename, path: ValidationPath):
    """
    Validate a sample file.

    Args:
        preset_data: Dictionary containing the preset data
        folder_path: Path to the folder containing the sample files
        sample_filename: Filename of the sample
        path: Tuple (preset_key, channel_key, zone_key) for error reporting and line_map

    Raises:
        SampleFileNotFoundError: If the sample file is not found
        InvalidSampleFormatError: If the sample file has an invalid format
    """
    sample_path = os.path.join(folder_path, sample_filename)
    context = _path_to_context(path)

    # Check if file exists
    if not os.path.exists(sample_path):
        raise SampleFileNotFoundError(
            f"Sample file '{sample_filename}' referenced in {context} not found",
            path=path,
        )

    # Check if file is a valid WAV file
    if not sample_filename.lower().endswith(".wav"):
        raise InvalidSampleFormatError(
            f"Sample file '{sample_filename}' referenced in {context} is not a WAV file format",
            path=path,
        )

    # Try to open as WAV
    try:
        with wave.open(sample_path, "rb") as wav_file:
            # Get sample properties
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            frame_rate = wav_file.getframerate()

            # Validate sample properties
            if channels not in [1, 2]:
                raise InvalidSampleFormatError(
                    f"Sample file '{sample_filename}' referenced in {context} "
                    f"has an invalid number of channels: {channels}",
                    path=path,
                )

            if sample_width not in [1, 2, 3, 4]:
                raise InvalidSampleFormatError(
                    f"Sample file '{sample_filename}' referenced in {context} "
                    f"has an invalid sample width: {sample_width}",
                    path=path,
                )

            # Validate sample rate
            valid_rates = [44100, 48000, 96000, 192000]
            if frame_rate not in valid_rates:
                raise InvalidSampleFormatError(
                    f"Sample file '{sample_filename}' referenced in {context} "
                    f"has an invalid sample rate: {frame_rate}Hz",
                    path=path,
                )

    except wave.Error:
        raise InvalidSampleFormatError(
            f"Sample file '{sample_filename}' referenced in {context} "
            f"is not a valid WAV file format",
            path=path,
        )
    except Exception as e:
        raise FileSystemValidationError(
            f"Error validating sample file '{sample_filename}' referenced in {context}: {str(e)}",
            path=path,
        )

    # Validate sample positions if referenced in the preset
    _validate_sample_positions(preset_data, folder_path, sample_filename, path)


def _validate_sample_positions(preset_data, folder_path, sample_filename, path: ValidationPath):
    """
    Validate sample positions referenced in a preset.

    Args:
        preset_data: Dictionary containing the preset data
        folder_path: Path to the folder containing the sample files
        sample_filename: Filename of the sample
        path: Tuple (preset_key, channel_key, zone_key) for lookup and error reporting

    Raises:
        FileSystemValidationError: If validation fails
    """
    if len(path) < 3:
        return

    preset_key, channel_key, zone_key = path[0], path[1], path[2]

    # Get channel and zone data
    preset_value = preset_data.get(preset_key)
    if preset_value is None:
        return

    channel_value = preset_value.get(channel_key)
    if channel_value is None:
        return

    zone_value = channel_value.get(zone_key)
    if zone_value is None:
        return

    # Get sample length
    sample_path = os.path.join(folder_path, sample_filename)
    sample_length = get_sample_length(sample_path)
    context = _path_to_context(path)

    # Validate LoopStart
    loop_start = zone_value.get("LoopStart")
    if loop_start is None:
        loop_start = channel_value.get("LoopStart")

    if loop_start is not None and loop_start >= sample_length:
        raise FileSystemValidationError(
            f"LoopStart ({loop_start}) in {context} exceeds sample length ({sample_length})",
            path=path + ("LoopStart",),
        )

    # Validate SampleStart
    sample_start = zone_value.get("SampleStart")
    if sample_start is None:
        sample_start = channel_value.get("SampleStart")

    if sample_start is not None and sample_start >= sample_length:
        raise FileSystemValidationError(
            f"SampleStart ({sample_start}) in {context} exceeds sample length ({sample_length})",
            path=path + ("SampleStart",),
        )

    # Validate SampleEnd
    # Note: Assimil8or automatically clamps SampleEnd to the file length if it exceeds it,
    # so we don't treat this as an error - it's handled gracefully by the device
    sample_end = zone_value.get("SampleEnd")
    if sample_end is None:
        sample_end = channel_value.get("SampleEnd")

    # SampleEnd exceeding sample length is not an error - Assimil8or clamps it internally
    # We could add a warning here if desired, but it's not a validation failure


def get_sample_length(file_path):
    """
    Get the length (in samples) of a WAV file.

    Args:
        file_path: Path to the WAV file

    Returns:
        int: Sample length

    Raises:
        FileSystemValidationError: If the file cannot be read or is not a valid WAV file
    """
    try:
        with wave.open(file_path, "rb") as wav_file:
            return wav_file.getnframes()
    except wave.Error as e:
        raise FileSystemValidationError(f"Cannot read WAV file '{file_path}': {str(e)}")
    except Exception as e:
        raise FileSystemValidationError(f"Error reading file '{file_path}': {str(e)}")


def calculate_total_memory(preset_data, folder_path):
    """
    Calculate the total memory usage for all samples in a preset.

    Args:
        preset_data: Dictionary containing the preset data
        folder_path: Path to the folder containing the sample files

    Returns:
        int: Total memory usage in bytes
    """
    # Get unique sample references
    samples = set()
    sample_references = _collect_sample_references(preset_data)
    for _, sample_filename in sample_references:
        samples.add(sample_filename)

    # Calculate total memory
    total_bytes = 0
    for sample_filename in samples:
        sample_path = os.path.join(folder_path, sample_filename)
        if os.path.exists(sample_path):
            try:
                with wave.open(sample_path, "rb") as wav_file:
                    # Calculate memory for this sample
                    channels = wav_file.getnchannels()
                    sample_width = wav_file.getsampwidth()
                    n_frames = wav_file.getnframes()

                    # Memory = channels * width * frames
                    sample_bytes = channels * sample_width * n_frames
                    total_bytes += sample_bytes
            except wave.Error as e:
                # If WAV file is corrupted or invalid, skip it and log a warning
                # Using file size would be inaccurate (includes headers, compression, etc.)
                # Better to skip than give false memory calculations
                import warnings

                warnings.warn(
                    f"Cannot calculate memory for '{sample_filename}': {str(e)}. "
                    f"Skipping from memory calculation.",
                    UserWarning,
                )
            except Exception as e:
                # For other errors (permissions, etc.), also skip
                import warnings

                warnings.warn(
                    f"Cannot read '{sample_filename}': {str(e)}. "
                    f"Skipping from memory calculation.",
                    UserWarning,
                )

    return total_bytes


def validate_preset_filename(filename):
    """
    Validate that a preset filename follows the required format.

    Presets must follow the format prstxxx.yml where xxx is 000-999.
    The filename must be lowercase.

    Args:
        filename: The filename to validate (e.g., "prst001.yml")

    Raises:
        InvalidPresetFilenameError: If the filename does not match the required format
    """
    # Check if filename is lowercase
    if filename != filename.lower():
        raise InvalidPresetFilenameError(
            f"Preset filename '{filename}' must be lowercase (expected: '{filename.lower()}')"
        )

    # Check if filename matches the pattern prstxxx.yml where xxx is 000-999
    pattern = r"^prst\d{3}\.yml$"
    if not re.match(pattern, filename):
        raise InvalidPresetFilenameError(
            f"Preset filename '{filename}' does not match required format 'prstxxx.yml' "
            f"(where xxx is 000-999)"
        )

    # Extract the number part and validate it's in range 000-999
    match = re.match(r"^prst(\d{3})\.yml$", filename)
    if match:
        number = int(match.group(1))
        if number < 0 or number > 999:
            raise InvalidPresetFilenameError(
                f"Preset filename '{filename}' number must be between 000 and 999"
            )
