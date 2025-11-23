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
    """Custom constructor for numeric values to ensure proper type conversion."""
    value = loader.construct_scalar(node)
    
    # Try to convert to float first (handles both integers and floats)
    try:
        # Remove any leading/trailing whitespace and handle signed numbers
        cleaned_value = value.strip()
        
        # Convert to float, which handles both integer and floating-point formats
        numeric_value = float(cleaned_value)
        
        # If the float is a whole number, convert to int
        if numeric_value.is_integer():
            return int(numeric_value)
        
        return numeric_value
    except ValueError:
        # If conversion fails, return the original value
        return value


# Register custom constructor
AssimPresetLoader.add_constructor('tag:yaml.org,2002:float', construct_number)
AssimPresetLoader.add_constructor('tag:yaml.org,2002:int', construct_number)


def parse_yaml_file(file_path, return_line_map=False):
    """
    Parse an Assimil8or preset YAML file, optionally returning a mapping of key paths to line numbers.
    """
    import collections
    import re

    def preprocess_assimil8or_yaml(content):
        """
        Preprocess Assimil8or YAML content to quote unquoted values starting with special characters.
        """
        def needs_quoting(value):
            # Check if value starts with special characters that need quoting
            return bool(re.match(r'^[@#:\-\?]', value))

        processed_lines = []
        for line in content.splitlines():
            # Match lines with 'key : value' pattern
            match = re.match(r'^(\s*[^:\s][^:]*)\s*:\s*(.+)$', line)
            if match:
                key, value = match.groups()
                value = value.strip()
                # If value is unquoted and needs quoting, add quotes
                if value and not (value.startswith('"') or value.startswith("'")) and needs_quoting(value):
                    # Escape existing quotes in value
                    value_escaped = value.replace('"', '\\"')
                    value = f'"{value_escaped}"'
                processed_lines.append(f"{key} : {value}")
            else:
                processed_lines.append(line)
        return "\n".join(processed_lines)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if os.path.getsize(file_path) == 0:
        raise PresetParseError(f"Empty file: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    # Preprocess content to fix unquoted special values
    preprocessed_content = preprocess_assimil8or_yaml(raw_content)

    class LineNumberLoader(AssimPresetLoader):
        def __init__(self, stream):
            super().__init__(stream)
            self.line_map = {}

        def construct_mapping(self, node, deep=False, path=()):
            mapping = {}
            for key_node, value_node in node.value:
                key = self.construct_object(key_node, deep=deep)
                # Build the full path for this key
                current_path = path + (key,)
                # Recursively construct value
                if isinstance(value_node, yaml.MappingNode):
                    value = self.construct_mapping(value_node, deep=deep, path=current_path)
                else:
                    value = self.construct_object(value_node, deep=deep)
                mapping[key] = value
                # Record line number for this key path
                self.line_map[current_path] = key_node.start_mark.line + 1
            return mapping

    try:
        loader = LineNumberLoader(preprocessed_content)
        data = loader.get_single_data()
        line_map = loader.line_map
    except yaml.YAMLError as e:
        line_info = ""
        if hasattr(e, 'problem_mark'):
            line_info = f" on line {e.problem_mark.line + 1}"
        raise YAMLSyntaxError(f"YAML syntax error{line_info}: {str(e)}")
    except Exception as e:
        line_match = re.search(r'line (\d+)', str(e))
        if line_match:
            line_info = f" on line {line_match.group(1)}"
            raise YAMLSyntaxError(f"YAML syntax error{line_info}: {str(e)}")
        raise PresetParseError(f"Error parsing file: {str(e)}")

    if not data or not any(key.startswith('Preset ') for key in data.keys()):
        raise InvalidPresetError(f"Not a valid Assimil8or preset format: {file_path}")

    if return_line_map:
        return data, line_map
    return data
