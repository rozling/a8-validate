"""Tests for the YAML parser component."""

import os
import tempfile
from unittest import mock

import pytest

# Import the module that doesn't exist yet (this will cause the test to fail initially)
from a8_validate.yaml_parser import InvalidPresetError, PresetParseError, YAMLSyntaxError, parse_yaml_file


class TestYAMLParser:
    """Test cases for the YAML parser component."""

    def test_parse_valid_preset_file(self):
        """Test parsing a valid Assimil8or preset file."""
        valid_yaml = """Preset 1 :
  Name : Test Preset
  Channel 1 :
    Pitch : 0.00
    Zone 1 :
      Sample : test.wav
"""
        # Create a temporary file with valid YAML content
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp.write(valid_yaml)
            temp_path = temp.name

        try:
            # Parse the file
            result = parse_yaml_file(temp_path)

            # Check that parsing was successful
            assert result is not None
            assert isinstance(result, dict)

            # Check that the content was parsed correctly
            assert "Preset 1" in result
            assert result["Preset 1"]["Name"] == "Test Preset"
            assert "Channel 1" in result["Preset 1"]
            assert result["Preset 1"]["Channel 1"]["Pitch"] == 0.0  # Check as float now
            assert "Zone 1" in result["Preset 1"]["Channel 1"]
            assert result["Preset 1"]["Channel 1"]["Zone 1"]["Sample"] == "test.wav"
        finally:
            # Clean up
            os.unlink(temp_path)

    def test_yaml_syntax_error(self):
        """Test handling of YAML syntax errors."""
        invalid_yaml = """Preset 1 :
  Name : Test Preset
  Channel 1 :
    Pitch : 0.00
    Zone 1 :
      Sample : test.wav
  This line has improper indentation
    This is another improperly indented line
"""
        # Create a temporary file with invalid YAML content
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp.write(invalid_yaml)
            temp_path = temp.name

        try:
            # Parsing should raise a YAMLSyntaxError
            with pytest.raises(YAMLSyntaxError) as exc_info:
                parse_yaml_file(temp_path)

            # The error should contain line number information
            assert "line" in str(exc_info.value).lower()
            assert "indentation" in str(exc_info.value).lower()
        finally:
            # Clean up
            os.unlink(temp_path)

    def test_invalid_preset_structure(self):
        """Test handling of files that don't have a valid Assimil8or preset structure."""
        non_preset_yaml = """SomeOtherFormat:
  Key1: Value1
  Key2: Value2
"""
        # Create a temporary file with non-preset YAML content
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp.write(non_preset_yaml)
            temp_path = temp.name

        try:
            # Parsing should raise an InvalidPresetError
            with pytest.raises(InvalidPresetError) as exc_info:
                parse_yaml_file(temp_path)

            # The error should mention the preset format
            assert "preset" in str(exc_info.value).lower()
            assert "format" in str(exc_info.value).lower()
        finally:
            # Clean up
            os.unlink(temp_path)

    def test_empty_file(self):
        """Test handling of empty files."""
        # Create an empty temporary file
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp_path = temp.name

        try:
            # Parsing should raise a PresetParseError
            with pytest.raises(PresetParseError) as exc_info:
                parse_yaml_file(temp_path)

            # The error should mention the file is empty
            assert "empty" in str(exc_info.value).lower()
        finally:
            # Clean up
            os.unlink(temp_path)

    def test_file_not_found(self):
        """Test handling of non-existent files."""
        # Generate a path to a file that doesn't exist
        nonexistent_path = tempfile.mktemp()

        # Parsing should raise a FileNotFoundError
        with pytest.raises(FileNotFoundError):
            parse_yaml_file(nonexistent_path)

    def test_line_number_preservation(self):
        """Test that line numbers are preserved for error reporting."""
        yaml_with_error_on_line_5 = """Preset 1 :
  Name : Test Preset
  Channel 1 :
    Pitch : 0.00
    This is an error on line 5
    Zone 1 :
      Sample : test.wav
"""
        # Create a temporary file with YAML content that has an error on line 5
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp.write(yaml_with_error_on_line_5)
            temp_path = temp.name

        try:
            # Mock the YAML parser to raise an exception with line information
            with mock.patch("yaml.safe_load", side_effect=Exception("Error on line 5")):
                # Parsing should raise a YAMLSyntaxError
                with pytest.raises(YAMLSyntaxError) as exc_info:
                    parse_yaml_file(temp_path)

                # The error should contain the line number
                assert "line 5" in str(exc_info.value)
        finally:
            # Clean up
            os.unlink(temp_path)

    def test_complex_preset_structure(self):
        """Test parsing a more complex Assimil8or preset file with multiple channels and zones."""
        complex_yaml = """Preset 7 :
  Name : Spectral Percussion Morphology
  XfadeACV : 1A
  XfadeAWidth : 9.10
  Channel 1 :
    Pitch : -12.00
    Level : -3.0
    PitchCV : 0A 0.50
    Zone 1 :
      Sample : BD_Thump_1.wav
      MinVoltage : +5.00
    Zone 2 :
      Sample : BD_Elec_1.wav
      MinVoltage : +2.50
  Channel 2 :
    ChannelMode : 1
    Pitch : +7.00
    Level : -6.0
    Zone 1 :
      Sample : Acid_1.wav
      LoopMode : 1
      LoopStart : 100
      LoopLength : 1000
"""
        # Create a temporary file with complex YAML content
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp.write(complex_yaml)
            temp_path = temp.name

        try:
            # Parse the file
            result = parse_yaml_file(temp_path)

            # Check that parsing was successful
            assert result is not None
            assert isinstance(result, dict)

            # Check that the complex structure was parsed correctly
            preset = result["Preset 7"]
            assert preset["Name"] == "Spectral Percussion Morphology"
            assert preset["XfadeACV"] == "1A"
            assert abs(preset["XfadeAWidth"] - 9.10) < 1e-6  # Check as float

            # Check Channel 1
            channel1 = preset["Channel 1"]
            assert abs(float(channel1["Pitch"]) + 12.00) < 1e-6  # Check as float
            assert abs(float(channel1["Level"]) + 3.0) < 1e-6  # Check as float
            assert channel1["PitchCV"] == "0A 0.50"

            # Check Zones in Channel 1
            assert channel1["Zone 1"]["Sample"] == "BD_Thump_1.wav"
            assert abs(float(channel1["Zone 1"]["MinVoltage"]) - 5.0) < 1e-6
            assert channel1["Zone 2"]["Sample"] == "BD_Elec_1.wav"
            assert abs(float(channel1["Zone 2"]["MinVoltage"]) - 2.5) < 1e-6

            # Check Channel 2
            channel2 = preset["Channel 2"]
            assert channel2["ChannelMode"] == 1  # This should remain an integer
            assert abs(float(channel2["Pitch"]) - 7.0) < 1e-6  # Check as float
            assert abs(float(channel2["Level"]) + 6.0) < 1e-6  # Check as float

            # Check Zone in Channel 2
            assert channel2["Zone 1"]["Sample"] == "Acid_1.wav"
            assert channel2["Zone 1"]["LoopMode"] == 1  # This should remain an integer
            assert channel2["Zone 1"]["LoopStart"] == 100  # This should remain an integer
            assert channel2["Zone 1"]["LoopLength"] == 1000  # This should remain an integer
        finally:
            # Clean up
            os.unlink(temp_path)

    def test_cv_input_parsing(self):
        """Test parsing of CV input specifications like '1A 0.50'."""
        yaml_with_cv_inputs = """Preset 1 :
  Name : CV Test
  Channel 1 :
    PitchCV : 1A 0.50
    LinFM : 2B -0.18
    PhaseCV : Off 0.00
    PMIndexMod : 3C 1.00
"""
        # Create a temporary file with YAML content containing CV inputs
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp.write(yaml_with_cv_inputs)
            temp_path = temp.name

        try:
            # Parse the file
            result = parse_yaml_file(temp_path)

            # Check that parsing was successful
            assert result is not None

            # Check that CV inputs were parsed correctly as strings (not parsed into components yet)
            channel = result["Preset 1"]["Channel 1"]
            assert channel["PitchCV"] == "1A 0.50"
            assert channel["LinFM"] == "2B -0.18"
            assert channel["PhaseCV"] == "Off 0.00"
            assert channel["PMIndexMod"] == "3C 1.00"
        finally:
            # Clean up
            os.unlink(temp_path)
