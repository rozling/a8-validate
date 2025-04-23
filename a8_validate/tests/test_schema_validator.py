"""Tests for the schema validator component."""

import pytest

# Import the module that doesn't exist yet (this will cause the test to fail initially)
from a8_validate.schema_validator import (
    validate_preset,
    validate_channel,
    validate_zone,
    SchemaValidationError,
    InvalidParameterError,
    InvalidValueError,
    MissingRequiredParameterError,
)


class TestSchemaValidator:
    """Test cases for the schema validator component."""

    def test_validate_valid_preset(self):
        """Test validation of a valid preset structure."""
        valid_preset = {
            "Preset 1": {
                "Name": "Test Preset",
                "Data2asCV": "1A",
                "XfadeACV": "1A",
                "XfadeAWidth": 9.10,
                "Channel 1": {
                    "Pitch": 0.00,
                    "Level": -3.0,
                    "ChannelMode": 1,
                    "Zone 1": {
                        "Sample": "test.wav",
                        "MinVoltage": "+5.00"
                    }
                }
            }
        }
        
        # Validation should succeed without raising any exceptions
        validate_preset(valid_preset)

    def test_missing_required_parameter(self):
        """Test validation of a preset missing a required parameter."""
        # Missing Name parameter, which is required
        preset_missing_name = {
            "Preset 1": {
                "XfadeACV": "1A",
                "Channel 1": {
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise MissingRequiredParameterError
        with pytest.raises(MissingRequiredParameterError) as exc_info:
            validate_preset(preset_missing_name)
        
        # Error should mention the missing parameter
        assert "Name" in str(exc_info.value)

    def test_invalid_parameter_name(self):
        """Test validation of a preset with an invalid parameter name."""
        preset_with_invalid_param = {
            "Preset 1": {
                "Name": "Test Preset",
                "InvalidParameter": "Some Value",
                "Channel 1": {
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise InvalidParameterError
        with pytest.raises(InvalidParameterError) as exc_info:
            validate_preset(preset_with_invalid_param)
        
        # Error should mention the invalid parameter
        assert "InvalidParameter" in str(exc_info.value)

    def test_invalid_parameter_value_type(self):
        """Test validation of a preset with a parameter value of the wrong type."""
        preset_with_wrong_type = {
            "Preset 1": {
                "Name": "Test Preset",
                "XfadeAWidth": "9.10",  # Should be a float, not a string
                "Channel 1": {
                    "Pitch": 0.00,
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise InvalidValueError
        with pytest.raises(InvalidValueError) as exc_info:
            validate_preset(preset_with_wrong_type)
        
        # Error should mention the parameter name and expected type
        assert "XfadeAWidth" in str(exc_info.value)
        assert "float" in str(exc_info.value).lower()

    def test_value_out_of_range(self):
        """Test validation of a parameter value that is outside the allowed range."""
        preset_with_out_of_range = {
            "Preset 1": {
                "Name": "Test Preset",
                "Channel 1": {
                    "Pitch": 100.00,  # Should be between -96.00 and +60.00
                    "Zone 1": {
                        "Sample": "test.wav"
                    }
                }
            }
        }
        
        # Validation should raise InvalidValueError
        with pytest.raises(InvalidValueError) as exc_info:
            validate_preset(preset_with_out_of_range)
        
        # Error should mention the parameter name and value range
        assert "Pitch" in str(exc_info.value)
        assert "range" in str(exc_info.value).lower()

    def test_validate_channel(self):
        """Test validation of a channel structure."""
        valid_channel = {
            "Pitch": 0.00,
            "Level": -3.0,
            "ChannelMode": 1,
            "PitchCV": "1A 0.50",
            "Zone 1": {
                "Sample": "test.wav",
                "MinVoltage": "+5.00"
            }
        }
        
        # Validation should succeed without raising any exceptions
        validate_channel(valid_channel, channel_number=1)

    def test_invalid_channel_mode(self):
        """Test validation of an invalid channel mode value."""
        channel_with_invalid_mode = {
            "Pitch": 0.00,
            "ChannelMode": 5,  # Should be 0, 1, 2, or 3
            "Zone 1": {
                "Sample": "test.wav"
            }
        }
        
        # Validation should raise InvalidValueError
        with pytest.raises(InvalidValueError) as exc_info:
            validate_channel(channel_with_invalid_mode, channel_number=1)
        
        # Error should mention the parameter name and allowed values
        assert "ChannelMode" in str(exc_info.value)
        assert "5" in str(exc_info.value)  # The invalid value
        
    def test_validate_zone(self):
        """Test validation of a zone structure."""
        valid_zone = {
            "Sample": "test.wav",
            "MinVoltage": "+5.00",
            "LevelOffset": -3.0,
            "PitchOffset": 12.00,
            "LoopStart": 100,
            "LoopLength": 1000
        }
        
        # Validation should succeed without raising any exceptions
        validate_zone(valid_zone, channel_number=1, zone_number=1)

    def test_missing_required_sample(self):
        """Test validation of a zone missing the required Sample parameter."""
        zone_missing_sample = {
            "MinVoltage": "+5.00",
            "LevelOffset": -3.0
        }
        
        # Validation should raise MissingRequiredParameterError
        with pytest.raises(MissingRequiredParameterError) as exc_info:
            validate_zone(zone_missing_sample, channel_number=1, zone_number=1)
        
        # Error should mention the Sample parameter
        assert "Sample" in str(exc_info.value)

    def test_invalid_voltage_format(self):
        """Test validation of an invalid voltage format."""
        zone_with_invalid_voltage = {
            "Sample": "test.wav",
            "MinVoltage": "5V"  # Should be in format like "+5.00" or "-3.50"
        }
        
        # Validation should raise InvalidValueError
        with pytest.raises(InvalidValueError) as exc_info:
            validate_zone(zone_with_invalid_voltage, channel_number=1, zone_number=1)
        
        # Error should mention the parameter name and format
        assert "MinVoltage" in str(exc_info.value)
        assert "format" in str(exc_info.value).lower()

    def test_validate_cv_input_format(self):
        """Test validation of CV input format."""
        # Test valid CV inputs in a channel
        valid_cv_inputs = {
            "Pitch": 0.00,
            "PitchCV": "1A 0.50",
            "LinFM": "Off 0.00",
            "PhaseCV": "3C 1.00",
            "Zone 1": {
                "Sample": "test.wav"
            }
        }
        
        # Validation should succeed without raising any exceptions
        validate_channel(valid_cv_inputs, channel_number=1)
        
        # Test invalid CV input format
        invalid_cv_format = {
            "Pitch": 0.00,
            "PitchCV": "X1 0.50",  # Invalid format, should be like "1A 0.50"
            "Zone 1": {
                "Sample": "test.wav"
            }
        }
        
        # Validation should raise InvalidValueError
        with pytest.raises(InvalidValueError) as exc_info:
            validate_channel(invalid_cv_format, channel_number=1)
        
        # Error should mention the CV format
        assert "PitchCV" in str(exc_info.value)
        assert "format" in str(exc_info.value).lower()

    def test_nested_structure_validation(self):
        """Test validation of the entire nested structure of a preset."""
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
                }
            }
        }
        
        # Validation should succeed without raising any exceptions
        validate_preset(complex_preset)
        
        # Now introduce an error deep in the structure
        complex_preset["Preset 7"]["Channel 1"]["Zone 2"]["MinVoltage"] = "+6.00"  # Out of range
        
        # Validation should raise InvalidValueError
        with pytest.raises(InvalidValueError) as exc_info:
            validate_preset(complex_preset)
        
        # Error should contain context about where the error occurred
        assert "MinVoltage" in str(exc_info.value)
        assert "Channel 1" in str(exc_info.value)
        assert "Zone 2" in str(exc_info.value)
