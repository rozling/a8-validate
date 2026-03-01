"""Tests for the cross-reference validator component."""

import pytest

# Import the module that doesn't exist yet (this will cause the test to fail initially)
from a8_validate.cross_reference_validator import (
    ChannelModeError,
    CrossReferenceError,
    CVInputReferenceError,
    LoopConfigurationError,
    ZoneVoltageRangeError,
    validate_relationships,
)
from a8_validate.schema_validator import validate_preset


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
                    "Zone 1": {"Sample": "test.wav", "MinVoltage": "+5.00"},
                    "Zone 2": {
                        "Sample": "test2.wav",
                        "MinVoltage": "+2.50",  # Valid sequence of voltages
                    },
                },
                "Channel 2": {
                    "ChannelMode": 1,  # Link mode, which is valid since it's below a Master channel
                    "Pitch": 0.00,
                    "Zone 1": {"Sample": "test3.wav"},
                },
            }
        }

        # Validation should succeed without raising any exceptions
        validate_relationships(valid_preset)

    def test_partial_loop_parameters(self):
        """Test validation of partial loop parameter definitions."""
        # Test with only LoopStart (should fail - LoopStart requires LoopLength)
        preset_with_only_start = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on
                    "LoopStart": 100,  # Only LoopStart provided
                    "Zone 1": {"Sample": "test.wav"},
                },
            }
        }

        # Validation should raise LoopConfigurationError
        with pytest.raises(LoopConfigurationError) as exc_info:
            validate_relationships(preset_with_only_start)

        # Error should mention that LoopStart requires LoopLength
        assert "LoopStart" in str(exc_info.value)
        assert "LoopLength" in str(exc_info.value)

        # Test with only LoopLength (should pass - LoopStart defaults to 0)
        preset_with_only_length = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on
                    "LoopLength": 1000,  # Only LoopLength provided (LoopStart defaults to 0)
                    "Zone 1": {"Sample": "test.wav"},
                },
            }
        }

        # Validation should pass - LoopLength alone is allowed
        validate_relationships(preset_with_only_length)

    def test_loop_mode_with_default_full_sample_loop(self):
        """Test validation of a channel with loop mode on but no explicit loop parameters."""
        preset_with_default_loop = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on
                    # No explicit LoopStart or LoopLength
                    "Zone 1": {"Sample": "test.wav"},
                },
            }
        }

        # Validation should succeed without raising exceptions
        validate_relationships(preset_with_default_loop)

    def test_loop_mode_flag_consistency(self):
        """Test validation of LoopLengthIsEnd flag consistency with LoopMode."""
        # Test LoopMode 1 (Start/End) with incorrect LoopLengthIsEnd
        preset_mode1_incorrect_flag = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Start/End mode
                    "LoopLengthIsEnd": 0,  # Incorrect flag
                    "LoopStart": 100,
                    "LoopLength": 1000,
                    "Zone 1": {"Sample": "test.wav"},
                },
            }
        }

        # Validation should raise LoopConfigurationError
        with pytest.raises(LoopConfigurationError) as exc_info:
            validate_relationships(preset_mode1_incorrect_flag)

        # Error should mention LoopMode and LoopLengthIsEnd
        assert "LoopMode 1" in str(exc_info.value)
        assert "LoopLengthIsEnd" in str(exc_info.value)

        # Test LoopMode 2 (Start/Length) with incorrect LoopLengthIsEnd
        preset_mode2_incorrect_flag = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 2,  # Start/Length mode
                    "LoopLengthIsEnd": 1,  # Incorrect flag
                    "LoopStart": 100,
                    "LoopLength": 1000,
                    "Zone 1": {"Sample": "test.wav"},
                },
            }
        }

        # Validation should raise LoopConfigurationError
        with pytest.raises(LoopConfigurationError) as exc_info:
            validate_relationships(preset_mode2_incorrect_flag)

        # Error should mention LoopMode and LoopLengthIsEnd
        assert "LoopMode 2" in str(exc_info.value)
        assert "LoopLengthIsEnd" in str(exc_info.value)

    def test_invalid_zone_voltage_ranges(self):
        """Test validation of zones with overlapping or invalid voltage ranges."""
        preset_with_invalid_voltages = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav",
                        "MinVoltage": "+2.50",  # This voltage is lower than Zone 2's MinVoltage
                    },
                    "Zone 2": {
                        "Sample": "test2.wav",
                        "MinVoltage": "+5.00",  # This voltage is higher than Zone 1's MinVoltage
                    },
                },
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
                    "Zone 1": {"Sample": "test.wav"},
                },
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
                    "Zone 1": {"Sample": "test.wav"},
                },
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
                "Channel 1": {"Pitch": 0.00, "Zone 1": {"Sample": "test.wav"}},
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
                    "Zone 1": {"Sample": "test.wav"},
                },
            }
        }

        # Validation should raise CrossReferenceError
        with pytest.raises(CrossReferenceError) as exc_info:
            validate_relationships(preset_with_invalid_sample_points)

        # Error should mention the sample point issue
        assert "SampleStart" in str(exc_info.value)
        assert "SampleEnd" in str(exc_info.value)
        assert (
            "greater than" in str(exc_info.value).lower()
            or "after" in str(exc_info.value).lower()
        )

    def test_sample_start_end_as_strings(self):
        """Ensure numeric strings are properly validated for sample boundaries."""
        preset_with_string_values = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "SampleStart": "1000",
                    "SampleEnd": "500",
                    "Zone 1": {"Sample": "test.wav"},
                },
            }
        }

        # validate_preset converts numbers but previously didn't propagate them
        validate_preset(preset_with_string_values)

        with pytest.raises(CrossReferenceError):
            validate_relationships(preset_with_string_values)

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
                    "Zone 1": {"Sample": "test.wav"},
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",  # Same crossfade group as Channel 1
                    "Zone 1": {"Sample": "test2.wav"},
                },
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
                    "Zone 1": {"Sample": "test.wav"},
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "B",  # Different crossfade group
                    "Zone 1": {"Sample": "test2.wav"},
                },
            }
        }

        # Validation should raise CrossReferenceError
        with pytest.raises(CrossReferenceError) as exc_info:
            validate_relationships(invalid_crossfade_preset)

        # Error should mention the crossfade group issue
        assert "XfadeGroup" in str(exc_info.value)
        assert "A" in str(exc_info.value)
        assert (
            "minimum" in str(exc_info.value).lower()
            or "at least" in str(exc_info.value).lower()
        )

    def test_missing_crossfade_cv(self):
        """Test validation of crossfade groups without a corresponding CV input."""
        missing_cv_preset = {
            "Preset 1": {
                "Name": "Test Preset",
                # Missing XfadeACV but channels use group A
                "Channel 1": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {"Sample": "test.wav"},
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {"Sample": "test2.wav"},
                },
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
                    "Zone 1": {"Sample": "test.wav"},
                },
                "Channel 2": {
                    "Pitch": 0.00,
                    "XfadeGroup": "A",
                    "Zone 1": {"Sample": "test2.wav"},
                },
                "Channel 3": {
                    "Pitch": 0.00,
                    "XfadeGroup": "B",
                    "Zone 1": {"Sample": "test3.wav"},
                },
                "Channel 4": {
                    "Pitch": 0.00,
                    "XfadeGroup": "B",
                    "Zone 1": {"Sample": "test4.wav"},
                },
            }
        }

        # Validation should succeed without raising any exceptions
        validate_relationships(complex_crossfade_preset)

    def test_loop_mode_with_loop_parameters_in_zone(self):
        """Test validation of a channel with loop mode on but loop parameters defined in a zone."""
        preset_with_loop_params_in_zone = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on at channel level
                    # No LoopStart or LoopLength at channel level
                    "Zone 1": {
                        "Sample": "test.wav",
                        "LoopStart": 100,  # LoopStart defined in zone
                        "LoopLength": 1000,  # LoopLength defined in zone
                    },
                },
            }
        }

        # Validation should succeed without raising exceptions
        validate_relationships(preset_with_loop_params_in_zone)

    def test_loop_mode_with_no_loop_parameters_anywhere(self):
        """Test validation of a channel with loop mode on but no loop parameters defined anywhere."""
        preset_with_no_loop_params = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopMode": 1,  # Loop mode on at channel level
                    # No LoopStart or LoopLength at channel level
                    "Zone 1": {
                        "Sample": "test.wav"
                        # No LoopStart or LoopLength in zone either
                    },
                },
            }
        }

        # Validation should succeed without raising exceptions
        validate_relationships(preset_with_no_loop_params)

    def test_zone_level_loop_mode_with_zone_parameters(self):
        """Test validation of a zone with its own loop mode and loop parameters."""
        preset_with_zone_loop_mode = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    # No LoopMode at channel level
                    "Zone 1": {
                        "Sample": "test.wav",
                        "LoopMode": 1,  # Loop mode on at zone level
                        "LoopStart": 100,  # LoopStart defined in same zone
                        "LoopLength": 1000,  # LoopLength defined in same zone
                    },
                },
            }
        }

        # Validation should succeed without raising exceptions
        validate_relationships(preset_with_zone_loop_mode)

    def test_zone_level_loop_mode_with_channel_parameters(self):
        """Test validation of a zone with loop mode that inherits loop parameters from channel."""
        preset_with_inherited_params = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    "LoopStart": 100,  # LoopStart defined at channel level
                    "LoopLength": 1000,  # LoopLength defined at channel level
                    "Zone 1": {
                        "Sample": "test.wav",
                        "LoopMode": 1,  # Loop mode on at zone level, should inherit parameters
                    },
                },
            }
        }

        # Validation should succeed without raising exceptions
        validate_relationships(preset_with_inherited_params)

    def test_zone_level_loop_mode_with_no_parameters(self):
        """Test validation of a zone with loop mode but no loop parameters anywhere."""
        preset_with_zone_no_params = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 0.00,
                    # No LoopStart or LoopLength at channel level
                    "Zone 1": {
                        "Sample": "test.wav",
                        "LoopMode": 1,  # Loop mode on at zone level
                        # No LoopStart or LoopLength in zone
                    },
                },
            }
        }

        # Validation should raise LoopConfigurationError
        with pytest.raises(LoopConfigurationError) as exc_info:
            validate_relationships(preset_with_zone_no_params)

        # Error should mention missing loop parameters for zone
        assert "Zone" in str(exc_info.value)
        assert "LoopStart" in str(exc_info.value) or "LoopLength" in str(exc_info.value)

    def test_mixed_parameter_inheritance(self):
        """Test validation with mixed inheritance of loop parameters."""
        preset_with_mixed_inheritance = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "LoopMode": 1,  # Loop mode on at channel level
                    "LoopStart": 100,  # LoopStart at channel level
                    # No LoopLength at channel level
                    "Zone 1": {
                        "Sample": "test.wav",
                        "LoopLength": 1000,  # LoopLength in zone, should complement channel LoopStart
                    },
                },
            }
        }

        # Validation should raise LoopConfigurationError
        with pytest.raises(LoopConfigurationError) as exc_info:
            validate_relationships(preset_with_mixed_inheritance)

        # Error should mention missing LoopLength
        assert "LoopLength" in str(exc_info.value)
