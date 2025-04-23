"""Tests for the cross-reference validator component."""

import pytest

# Import the module that doesn't exist yet (this will cause the test to fail initially)
from a8_validate.cross_reference_validator import (
    validate_relationships,
    CrossReferenceError,
    ChannelModeError,
    LoopConfigurationError,
    ZoneVoltageRangeError,
    CVInputReferenceError,
)


class TestCrossReferenceValidator:
    """Test cases for the cross-reference validator component."""

    def test_validate_valid_relationships(self):
        """Test validation of a preset with valid parameter relationships."""
        valid_preset = {
            "Preset 1": {
                "Name": "Test Preset",
                "XfadeACV": "1A",
                "XfadeAWidth": 9.10,
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on
                    "LoopStart": 100,  # LoopStart provided when LoopMode is on
                    "LoopLength": 1000,  # LoopLength provided when LoopMode is on
                    "Zone 1": {
                        "Sample": "test.wav",
                        "MinVoltage": "+5.00"
                    },
                    "Zone 2": {
                        "Sample": "test2.wav",
                        "MinVoltage": "+2.50"  # Valid sequence of voltages
                    }
                },
                "Channel 2": {
                    "ChannelMode": 1,  # Link mode, which is valid since it's below a Master channel
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test3.wav"
                    }
                }
            }
        }
        
        # Validation should succeed without raising any exceptions
        validate_relationships(valid_preset)

    def test_loop_mode_without_loop_start(self):
        """Test validation of a channel with loop mode on but missing loop start."""
        preset_missing_loop_start = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on
                    # Missing LoopStart
                    "LoopLength": 1000,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise LoopConfigurationError
        with pytest.raises(LoopConfigurationError) as exc_info:
            validate_relationships(preset_missing_loop_start)
        
        # Error should mention missing LoopStart
        assert "LoopStart" in str(exc_info.value)
        assert "LoopMode" in str(exc_info.value)

    def test_loop_mode_without_loop_length(self):
        """Test validation of a channel with loop mode on but missing loop length."""
        preset_missing_loop_length = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on
                    "LoopStart": 100,
                    # Missing LoopLength
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise LoopConfigurationError
        with pytest.raises(LoopConfigurationError) as exc_info:
            validate_relationships(preset_missing_loop_length)
        
        # Error should mention missing LoopLength
        assert "LoopLength" in str(exc_info.value)
        assert "LoopMode" in str(exc_info.value)

    def test_invalid_zone_voltage_ranges(self):
        """Test validation of zones with overlapping or invalid voltage ranges."""
        preset_with_invalid_voltages = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav",
                        "MinVoltage": "+2.50"  # This voltage is lower than Zone 2's MinVoltage
                    },
                    "Zone 2": {
                        "Sample": "test2.wav",
                        "MinVoltage": "+5.00"  # This voltage is higher than Zone 1's MinVoltage
                    }
                }
            }
        }
        
        # Validation should raise ZoneVoltageRangeError
        with pytest.raises(ZoneVoltageRangeError) as exc_info:
            validate_relationships(preset_with_invalid_voltages)
        
        # Error should mention the voltage range issue
        assert "voltage" in str(exc_info.value).lower()
        assert "Zone 1" in str(exc_info.value)
        assert "Zone 2" in str(exc_info.value)

    def test_invalid_link_channel_mode(self):
        """Test validation of a Link channel without a Master channel above it."""
        preset_with_invalid_link = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "ChannelMode": 1,  # Link mode, but there's no Master channel above it
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise ChannelModeError
        with pytest.raises(ChannelModeError) as exc_info:
            validate_relationships(preset_with_invalid_link)
        
        # Error should mention the channel mode issue
        assert "Link" in str(exc_info.value)
        assert "Master" in str(exc_info.value)

    def test_invalid_cycle_channel_mode(self):
        """Test validation of a Cycle channel without a Master channel above it."""
        preset_with_invalid_cycle = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "ChannelMode": 3,  # Cycle mode, but there's no Master channel above it
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise ChannelModeError
        with pytest.raises(ChannelModeError) as exc_info:
            validate_relationships(preset_with_invalid_cycle)
        
        # Error should mention the channel mode issue
        assert "Cycle" in str(exc_info.value)
        assert "Master" in str(exc_info.value)

    def test_invalid_cv_input_reference(self):
        """Test validation of a CV input reference that doesn't exist."""
        preset_with_invalid_cv = {
            "Preset 1": {
                "Name": "Test Preset",
                "XfadeACV": "9A",  # Invalid CV input (should be 1A-8C)
                "Channel 1": {
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise CVInputReferenceError
        with pytest.raises(CVInputReferenceError) as exc_info:
            validate_relationships(preset_with_invalid_cv)
        
        # Error should mention the invalid CV input
        assert "9A" in str(exc_info.value)
        assert "XfadeACV" in str(exc_info.value)

    def test_sample_start_end_relationship(self):
        """Test validation of the relationship between sample start and end points."""
        preset_with_invalid_sample_points = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "SampleStart": 1000,  # Start point is after end point
                    "SampleEnd": 500,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise CrossReferenceError
        with pytest.raises(CrossReferenceError) as exc_info:
            validate_relationships(preset_with_invalid_sample_points)
        
        # Error should mention the sample point issue
        assert "SampleStart" in str(exc_info.value)
        assert "SampleEnd" in str(exc_info.value)
        assert "greater than" in str(exc_info.value).lower() or "after" in str(exc_info.value).lower()

    def test_crossfade_group_membership(self):
        """Test validation of crossfade group configuration."""
        # Test with a valid crossfade group (at least 2 channels)
        valid_crossfade_preset = {
            "Preset 1": {
                "Name": "Test Preset",
                "XfadeACV": "1A",
                "XfadeAWidth": 9.10,
                "Channel 1": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",  # Same crossfade group as Channel 1
                    "Zone 1": {
                        "Sample": "test2.wav"
                    }
                }
            }
        }
        
        # Validation should succeed without raising any exceptions
        validate_relationships(valid_crossfade_preset)
        
        # Test with an invalid crossfade group (only 1 channel)
        invalid_crossfade_preset = {
            "Preset 1": {
                "Name": "Test Preset",
                "XfadeACV": "1A",
                "XfadeAWidth": 9.10,
                "Channel 1": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",  # Only one channel in this group
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "B",  # Different crossfade group
                    "Zone 1": {
                        "Sample": "test2.wav"
                    }
                }
            }
        }
        
        # Validation should raise CrossReferenceError
        with pytest.raises(CrossReferenceError) as exc_info:
            validate_relationships(invalid_crossfade_preset)
        
        # Error should mention the crossfade group issue
        assert "XfadeGroup" in str(exc_info.value)
        assert "A" in str(exc_info.value)
        assert "minimum" in str(exc_info.value).lower() or "at least" in str(exc_info.value).lower()

    def test_missing_crossfade_cv(self):
        """Test validation of crossfade groups without a corresponding CV input."""
        missing_cv_preset = {
            "Preset 1": {
                "Name": "Test Preset",
                # Missing XfadeACV but channels use group A
                "Channel 1": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {
                        "Sample": "test2.wav"
                    }
                }
            }
        }
        
        # Validation should raise CrossReferenceError
        with pytest.raises(CrossReferenceError) as exc_info:
            validate_relationships(missing_cv_preset)
        
        # Error should mention the missing CV for the crossfade group
        assert "XfadeACV" in str(exc_info.value)
        assert "XfadeGroup" in str(exc_info.value)
        assert "A" in str(exc_info.value)

    def test_complex_crossfade_groups(self):
        """Test validation of multiple crossfade groups with correct configuration."""
        complex_crossfade_preset = {
            "Preset 1": {
                "Name": "Test Preset",
                "XfadeACV": "1A",
                "XfadeAWidth": 9.10,
                "XfadeBCV": "2A",
                "XfadeBWidth": 5.0,
                "Channel 1": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {
                        "Sample": "test2.wav"
                    }
                },
                "Channel 3": {
                    "Pitch": 0.00,
                    "XfadeGroup": "B",
                    "Zone 1": {
                        "Sample": "test3.wav"
                    }
                },
                "Channel 4": {
                    "Pitch": 0.00,
                    "XfadeGroup": "B",
                    "Zone 1": {
                        "Sample": "test4.wav"
                    }
                }
            }
        }
        
        # Validation should succeed without raising any exceptions
        validate_relationships(complex_crossfade_preset)
