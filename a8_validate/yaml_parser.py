"""YAML Parser module for Assimil8or preset files."""

import os
import yaml


class PresetParseError(Exception):
    """Base exception for parse errors."""
    pass


class YAMLSyntaxError(PresetParseError):
    """Exception raised for YAML syntax errors."""
    pass


class InvalidPresetError(PresetParseError):
    """Exception raised for files that are not valid Assimil8or presets."""
    pass


def parse_yaml_file(file_path):
    """
    Parse an Assimil8or preset YAML file.
    
    Args:
        file_path: Path to the YAML file to parse
        
    Returns:
        dict: Parsed preset data
        
    Raises:
        FileNotFoundError: If the file does not exist
        YAMLSyntaxError: If the file contains invalid YAML syntax
        InvalidPresetError: If the file is not a valid Assimil8or preset
        PresetParseError: For other parsing errors
    """
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if file is empty
    if os.path.getsize(file_path) == 0:
        raise PresetParseError(f"Empty file: {file_path}")
    
    # Read and parse the file
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            data = yaml.safe_load(content)
    except yaml.YAMLError as e:
        # Try to extract line number information
        line_info = ""
        if hasattr(e, 'problem_mark'):
            line_info = f" on line {e.problem_mark.line + 1}"
        raise YAMLSyntaxError(f"YAML syntax error{line_info}: {str(e)}")
    except Exception as e:
        raise PresetParseError(f"Error parsing file: {str(e)}")
    
    # Validate that it's an Assimil8or preset file
    if not data or not any(key.startswith('Preset ') for key in data.keys()):
        raise InvalidPresetError(f"Not a valid Assimil8or preset format: {file_path}")
    
    return data
