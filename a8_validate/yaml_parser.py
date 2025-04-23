"""YAML Parser module for Assimil8or preset files."""

import os
import yaml
import re


class PresetParseError(Exception):
    """Base exception for parse errors."""
    pass


class YAMLSyntaxError(PresetParseError):
    """Exception raised for YAML syntax errors."""
    pass


class InvalidPresetError(PresetParseError):
    """Exception raised for files that are not valid Assimil8or presets."""
    pass


# Custom YAML loader to preserve string formatting for specific types of values
class AssimPresetLoader(yaml.SafeLoader):
    """Custom YAML loader for Assimil8or presets."""
    pass


# Custom constructor for numbers to preserve original format
def construct_number(loader, node):
    """Custom constructor for numeric values to preserve format."""
    value = loader.construct_scalar(node)
    
    # Check if the value is formatted as a float with + or - prefix
    if re.match(r'^[+-]?\d+\.\d+$', value):
        # Return as-is to preserve the original format
        return value
    
    # Check if value is an integer
    if re.match(r'^[+-]?\d+$', value):
        try:
            return int(value)
        except ValueError:
            return value
        
    # Try to convert to float if appropriate
    try:
        if '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return value


# Register custom constructor
AssimPresetLoader.add_constructor('tag:yaml.org,2002:float', construct_number)
AssimPresetLoader.add_constructor('tag:yaml.org,2002:int', construct_number)


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
            data = yaml.load(content, Loader=AssimPresetLoader)
    except yaml.YAMLError as e:
        # Try to extract line number information
        line_info = ""
        if hasattr(e, 'problem_mark'):
            line_info = f" on line {e.problem_mark.line + 1}"
        raise YAMLSyntaxError(f"YAML syntax error{line_info}: {str(e)}")
    except Exception as e:
        # Check if the error message contains line information
        line_match = re.search(r'line (\d+)', str(e))
        if line_match:
            line_info = f" on line {line_match.group(1)}"
            raise YAMLSyntaxError(f"YAML syntax error{line_info}: {str(e)}")
        raise PresetParseError(f"Error parsing file: {str(e)}")
    
    # Validate that it's an Assimil8or preset file
    if not data or not any(key.startswith('Preset ') for key in data.keys()):
        raise InvalidPresetError(f"Not a valid Assimil8or preset format: {file_path}")
    
    return data
