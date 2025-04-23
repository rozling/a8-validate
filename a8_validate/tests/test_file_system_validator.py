"""Tests for the file system validator component."""

import os
import pytest
import tempfile

# Import the module that doesn't exist yet (this will cause the test to fail initially)
from a8_validate.file_system_validator import (
    validate_sample_files,
    FileSystemValidationError,
    SampleFileNotFoundError,
    InvalidSampleFormatError,
    MemoryLimitExceededError,
    get_sample_length,
    calculate_total_memory
)


class TestFileSystemValidator:
    """Test cases for the file system validator component."""

    def test_validate_existing_sample_files(self):
        """Test validation of a preset with existing sample files."""
        # Create temporary WAV files to simulate samples
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sample files
            sample1_path = os.path.join(temp_dir, "test1.wav")
            sample2_path = os.path.join(temp_dir, "test2.wav")
            
            with open(sample1_path, "wb") as f:
                # Write a minimal WAV file header (not a real WAV, just for testing)
                f.write(b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xAC\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00")
            
            with open(sample2_path, "wb") as f:
                # Write a minimal WAV file header
                f.write(b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xAC\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00")
            
            # Create a preset referencing these files
            preset = {
                "Preset 1": {
                    "Name": "Test Preset",
                    "Channel 1": {
                        "Pitch": 0.00,
                        "Zone 1": {
                            "Sample": "test1.wav"
                        }
                    },
                    "Channel 2": {
                        "Pitch": 0.00,
                        "Zone 1": {
                            "Sample": "test2.wav"
                        }
                    }
                }
            }
            
            # Validation should succeed without raising any exceptions
            validate_sample_files(preset, temp_dir)

    def test_nonexistent_sample_file(self):
        """Test validation of a preset with a non-existent sample file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a preset referencing a non-existent file
            preset = {
                "Preset 1": {
                    "Name": "Test Preset",
                    "Channel 1": {
                        "Pitch": 0.00,
                        "Zone 1": {
                            "Sample": "nonexistent.wav"
                        }
                    }
                }
            }
            
            # Validation should raise SampleFileNotFoundError
            with pytest.raises(SampleFileNotFoundError) as exc_info:
                validate_sample_files(preset, temp_dir)
            
            # Error should mention the missing file
            assert "nonexistent.wav" in str(exc_info.value)
            assert "not found" in str(exc_info.value).lower()

    def test_invalid_sample_format(self):
        """Test validation of a preset with a non-WAV sample file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a non-WAV file
            invalid_sample_path = os.path.join(temp_dir, "test.txt")
            
            with open(invalid_sample_path, "w") as f:
                f.write("This is not a WAV file")
            
            # Create a preset referencing this file
            preset = {
                "Preset 1": {
                    "Name": "Test Preset",
                    "Channel 1": {
                        "Pitch": 0.00,
                        "Zone 1": {
                            "Sample": "test.txt"
                        }
                    }
                }
            }
            
            # Validation should raise InvalidSampleFormatError
            with pytest.raises(InvalidSampleFormatError) as exc_info:
                validate_sample_files(preset, temp_dir)
            
            # Error should mention the invalid format
            assert "test.txt" in str(exc_info.value)
            assert "format" in str(exc_info.value).lower()

    def test_total_memory_validation(self, monkeypatch):
        """Test validation of total memory usage for all samples."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Mock large sample files by having the validator calculate their size differently
            large_samples = []
            
            # Create 10 sample files that would total more than the 422MB limit
            for i in range(10):
                sample_path = os.path.join(temp_dir, f"large_sample_{i}.wav")
                with open(sample_path, "wb") as f:
                    # Write a minimal WAV file header
                    f.write(b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xAC\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00")
                large_samples.append(f"large_sample_{i}.wav")
            
            # Create a preset referencing these files
            preset = {
                "Preset 1": {
                    "Name": "Test Preset"
                }
            }
            
            # Add channels with these samples
            for i, sample in enumerate(large_samples):
                channel_number = i + 1
                preset["Preset 1"][f"Channel {channel_number}"] = {
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": sample
                    }
                }
            
            # Mock the calculate_total_memory function to return a value greater than the limit
            # This is needed because our dummy WAV files are actually tiny
            monkeypatch.setattr("a8_validate.file_system_validator.calculate_total_memory", 
                                lambda preset, folder: 500 * 1024 * 1024)
            
            # Validation should raise MemoryLimitExceededError
            with pytest.raises(MemoryLimitExceededError) as exc_info:
                validate_sample_files(preset, temp_dir)
            
            # Error should mention the memory limit
            assert "422MB" in str(exc_info.value) or "422 MB" in str(exc_info.value)
            assert "memory" in str(exc_info.value).lower()

    def test_sample_length_validation(self, monkeypatch):
        """Test validation of sample length against referenced positions."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a sample file
            sample_path = os.path.join(temp_dir, "test.wav")
            
            with open(sample_path, "wb") as f:
                # Write a minimal WAV file header with a short length
                f.write(b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xAC\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00")
            
            # Create a preset referencing this file with loop points beyond its length
            preset = {
                "Preset 1": {
                    "Name": "Test Preset",
                    "Channel 1": {
                        "Pitch": 0.00,
                        "LoopMode": 1,
                        "LoopStart": 1000000,  # Way beyond the actual file length
                        "LoopLength": 1000,
                        "Zone 1": {
                            "Sample": "test.wav"
                        }
                    }
                }
            }
            
            # Mock the get_sample_length function to return a specific length
            monkeypatch.setattr("a8_validate.file_system_validator.get_sample_length", 
                               lambda file_path: 100000)
            
            # Validation should raise FileSystemValidationError
            with pytest.raises(FileSystemValidationError) as exc_info:
                validate_sample_files(preset, temp_dir)
            
            # Error should mention the loop points and sample length
            assert "LoopStart" in str(exc_info.value)
            assert "exceeds" in str(exc_info.value).lower()
            assert "length" in str(exc_info.value).lower()

    def test_complex_preset_validation(self, monkeypatch):
        """Test validation of a complex preset with multiple samples and zones."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create multiple sample files
            sample_files = ["BD_Thump_1.wav", "BD_Elec_1.wav", "Acid_1.wav", "Noise.wav"]
            
            for sample in sample_files:
                sample_path = os.path.join(temp_dir, sample)
                with open(sample_path, "wb") as f:
                    # Write a minimal WAV file header
                    f.write(b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xAC\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00")
            
            # Create a preset referencing these files
            complex_preset = {
                "Preset 7": {
                    "Name": "Spectral Percussion Morphology",
                    "XfadeACV": "1A",
                    "XfadeAWidth": 9.10,
                    "Channel 1": {
                        "Pitch": -12.00,
                        "Level": -3.0,
                        "PitchCV": "0A 0.50",
                        "Zone 1": {
                            "Sample": "BD_Thump_1.wav",
                            "MinVoltage": "+5.00"
                        },
                        "Zone 2": {
                            "Sample": "BD_Elec_1.wav",
                            "MinVoltage": "+2.50"
                        }
                    },
                    "Channel 2": {
                        "ChannelMode": 1,
                        "Pitch": 7.00,
                        "Level": -6.0,
                        "Zone 1": {
                            "Sample": "Acid_1.wav",
                            "LoopMode": 1,
                            "LoopStart": 100,
                            "LoopLength": 1000
                        }
                    },
                    "Channel 3": {
                        "Pitch": 12.00,
                        "Level": -9.0,
                        "Zone 1": {
                            "Sample": "Noise.wav"
                        }
                    }
                }
            }
            
            # Mock the get_sample_length function to return a specific length
            monkeypatch.setattr("a8_validate.file_system_validator.get_sample_length", 
                               lambda file_path: 10000)
            
            # Validation should succeed without raising any exceptions
            validate_sample_files(complex_preset, temp_dir)
            
            # Now add a missing sample to test failure case
            complex_preset["Preset 7"]["Channel 4"] = {
                "Pitch": 0.00,
                "Zone 1": {
                    "Sample": "missing.wav"
                }
            }
            
            # Validation should raise SampleFileNotFoundError
            with pytest.raises(SampleFileNotFoundError) as exc_info:
                validate_sample_files(complex_preset, temp_dir)
            
            # Error should mention the missing file
            assert "missing.wav" in str(exc_info.value)
            assert "Channel 4" in str(exc_info.value)
