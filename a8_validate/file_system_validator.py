"""File system validator module for Assimil8or preset files."""

import os
import wave


class FileSystemValidationError(Exception):
    """Base exception for file system validation errors."""
    pass


class SampleFileNotFoundError(FileSystemValidationError):
    """Exception raised when a referenced sample file is not found."""
    pass


class InvalidSampleFormatError(FileSystemValidationError):
    """Exception raised when a sample file has an invalid format."""
    pass


class MemoryLimitExceededError(FileSystemValidationError):
    """Exception raised when total memory usage exceeds the limit."""
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
    for context, sample_filename in sample_references:
        _validate_sample_file(folder_path, sample_filename, context)
    
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
        List of tuples (context, sample_filename)
    """
    sample_references = []
    
    for preset_key, preset_value in preset_data.items():
        for channel_key, channel_value in preset_value.items():
            if not channel_key.startswith('Channel '):
                continue
            
            channel_number = int(channel_key.split(' ')[1])
            
            for zone_key, zone_value in channel_value.items():
                if not zone_key.startswith('Zone '):
                    continue
                
                zone_number = int(zone_key.split(' ')[1])
                
                if 'Sample' in zone_value:
                    sample_filename = zone_value['Sample']
                    context = f"{preset_key}, {channel_key}, {zone_key}"
                    sample_references.append((context, sample_filename))
    
    return sample_references


def _validate_sample_file(folder_path, sample_filename, context):
    """
    Validate a sample file.
    
    Args:
        folder_path: Path to the folder containing the sample files
        sample_filename: Filename of the sample
        context: Context for error messages
        
    Raises:
        SampleFileNotFoundError: If the sample file is not found
        InvalidSampleFormatError: If the sample file has an invalid format
    """
    sample_path = os.path.join(folder_path, sample_filename)
    
    # Check if file exists
    if not os.path.exists(sample_path):
        raise SampleFileNotFoundError(f"Sample file '{sample_filename}' referenced in {context} not found")
    
    # Check if file is a valid WAV file
    if not sample_filename.lower().endswith('.wav'):
        raise InvalidSampleFormatError(
            f"Sample file '{sample_filename}' referenced in {context} is not a WAV file"
        )
    
    # Try to open as WAV
    try:
        with wave.open(sample_path, 'rb') as wav_file:
            # Get sample properties
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            frame_rate = wav_file.getframerate()
            n_frames = wav_file.getnframes()
            
            # Validate sample properties
            if channels not in [1, 2]:
                raise InvalidSampleFormatError(
                    f"Sample file '{sample_filename}' referenced in {context} "
                    f"has an invalid number of channels: {channels}"
                )
            
            if sample_width not in [1, 2, 3, 4]:
                raise InvalidSampleFormatError(
                    f"Sample file '{sample_filename}' referenced in {context} "
                    f"has an invalid sample width: {sample_width}"
                )
            
            # Validate sample rate
            valid_rates = [44100, 48000, 96000, 192000]
            if frame_rate not in valid_rates:
                raise InvalidSampleFormatError(
                    f"Sample file '{sample_filename}' referenced in {context} "
                    f"has an invalid sample rate: {frame_rate}Hz"
                )
    
    except wave.Error:
        raise InvalidSampleFormatError(
            f"Sample file '{sample_filename}' referenced in {context} "
            f"is not a valid WAV file"
        )
    except Exception as e:
        raise FileSystemValidationError(
            f"Error validating sample file '{sample_filename}' referenced in {context}: {str(e)}"
        )
    
    # Validate sample positions if referenced in the preset
    _validate_sample_positions(preset_data, folder_path, sample_filename, context)


def _validate_sample_positions(preset_data, folder_path, sample_filename, context):
    """
    Validate sample positions referenced in a preset.
    
    Args:
        preset_data: Dictionary containing the preset data
        folder_path: Path to the folder containing the sample files
        sample_filename: Filename of the sample
        context: Context for error messages
        
    Raises:
        FileSystemValidationError: If validation fails
    """
    # Parse context to get channel and zone
    parts = [part.strip() for part in context.split(',')]
    if len(parts) < 3:
        return
    
    preset_key = parts[0]
    channel_key = parts[1]
    zone_key = parts[2]
    
    # Get channel and zone data
    preset_value = None
    for key, value in preset_data.items():
        if key == preset_key:
            preset_value = value
            break
    
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
    
    # Validate LoopStart
    loop_start = zone_value.get('LoopStart')
    if loop_start is None:
        loop_start = channel_value.get('LoopStart')
    
    if loop_start is not None and loop_start >= sample_length:
        raise FileSystemValidationError(
            f"LoopStart ({loop_start}) in {context} exceeds sample length ({sample_length})"
        )
    
    # Validate SampleStart
    sample_start = zone_value.get('SampleStart')
    if sample_start is None:
        sample_start = channel_value.get('SampleStart')
    
    if sample_start is not None and sample_start >= sample_length:
        raise FileSystemValidationError(
            f"SampleStart ({sample_start}) in {context} exceeds sample length ({sample_length})"
        )
    
    # Validate SampleEnd
    sample_end = zone_value.get('SampleEnd')
    if sample_end is None:
        sample_end = channel_value.get('SampleEnd')
    
    if sample_end is not None and sample_end > sample_length:
        raise FileSystemValidationError(
            f"SampleEnd ({sample_end}) in {context} exceeds sample length ({sample_length})"
        )


def get_sample_length(file_path):
    """
    Get the length (in samples) of a WAV file.
    
    Args:
        file_path: Path to the WAV file
        
    Returns:
        int: Sample length
    """
    try:
        with wave.open(file_path, 'rb') as wav_file:
            return wav_file.getnframes()
    except Exception:
        # If there's an error, return a sensible default
        return 0


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
                with wave.open(sample_path, 'rb') as wav_file:
                    # Calculate memory for this sample
                    channels = wav_file.getnchannels()
                    sample_width = wav_file.getsampwidth()
                    n_frames = wav_file.getnframes()
                    
                    # Memory = channels * width * frames
                    sample_bytes = channels * sample_width * n_frames
                    total_bytes += sample_bytes
            except Exception:
                # If we can't open the file, use the file size as a fallback
                total_bytes += os.path.getsize(sample_path)
    
    return total_bytes
