# Assimil8or Preset Validator

## Overview

This Python library provides comprehensive validation for Assimil8or preset YAML files. It ensures the integrity and correctness of preset configurations through multiple validation layers.

## Features

- Detailed YAML parsing
- Schema validation
- Cross-reference validation
- File system validation for sample files
- Robust error reporting
- Directory-wide preset validation script

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   # venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Validating Individual Preset Files

```python
from a8_validate.yaml_parser import parse_yaml_file
from a8_validate.schema_validator import validate_preset
from a8_validate.cross_reference_validator import validate_relationships
from a8_validate.file_system_validator import validate_sample_files

def validate_preset_file(file_path, sample_folder_path):
    try:
        # Parse the YAML file
        preset_data = parse_yaml_file(file_path)
        
        # Validate schema
        validate_preset(preset_data)
        
        # Validate cross-references
        validate_relationships(preset_data)
        
        # Validate sample files
        validate_sample_files(preset_data, sample_folder_path)
        
        print("Preset is valid!")
    except Exception as e:
        print(f"Validation failed: {e}")

# Example usage
validate_preset_file('path/to/your/preset.yml', 'path/to/sample/folder')
```

### Directory Validation Script

The `validate_directory.py` script allows you to validate multiple preset files in a directory:

```bash
# Basic usage: validate all .yml files in a directory
python validate_directory.py /path/to/presets

# Validate presets with their associated sample files
python validate_directory.py /path/to/presets --sample-dir /path/to/samples

# Verbose mode for detailed output
python validate_directory.py /path/to/presets -v
```

#### Command-line Options

- `preset_dir`: (Required) Directory containing preset .yml files to validate
- `--sample-dir`: (Optional) Directory containing sample files for validation
- `--verbose`, `-v`: Enable detailed output during validation

### Handling Specific Validation Errors

```python
from a8_validate.yaml_parser import YAMLSyntaxError, InvalidPresetError
from a8_validate.schema_validator import InvalidParameterError, InvalidValueError
from a8_validate.cross_reference_validator import CrossReferenceError
from a8_validate.file_system_validator import SampleFileNotFoundError

try:
    validate_preset_file(file_path, sample_folder_path)
except YAMLSyntaxError as e:
    print("YAML syntax error:", e)
except InvalidPresetError as e:
    print("Invalid preset structure:", e)
except InvalidParameterError as e:
    print("Invalid parameter:", e)
except InvalidValueError as e:
    print("Invalid parameter value:", e)
except CrossReferenceError as e:
    print("Cross-reference validation failed:", e)
except SampleFileNotFoundError as e:
    print("Sample file not found:", e)
```

## Running Tests

To run the test suite:

```bash
python -m pytest
```

## Validation Layers

1. **YAML Parsing**
   - Preserves original formatting
   - Handles complex YAML structures
   - Detailed error reporting

2. **Schema Validation**
   - Checks parameter names
   - Validates value types and ranges
   - Ensures required parameters are present

3. **Cross-Reference Validation**
   - Checks complex parameter relationships
   - Validates channel and zone configurations
   - Ensures logical consistency

4. **File System Validation**
   - Verifies sample file existence
   - Checks WAV file properties
   - Validates sample references

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

[Specify your license here]

## Contact

[Your contact information]
