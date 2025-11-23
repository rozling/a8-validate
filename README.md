## Assimil8or Preset Validator (a8-validate)

[![Tests](https://github.com/rozling/a8-validate/workflows/Tests/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/test.yml)
[![Lint](https://github.com/rozling/a8-validate/workflows/Lint/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/lint.yml)
[![Coverage](https://github.com/rozling/a8-validate/workflows/Coverage/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/coverage.yml)
[![Security](https://github.com/rozling/a8-validate/workflows/Security/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/security.yml)

### Overview
A validation tool for Assimil8or preset files, ensuring they meet the required schema and cross-reference constraints.

### Recent Updates
- Improved numeric type parsing in YAML files
- Enhanced schema validation for stricter type checking
- Resolved parsing issues with numeric values in preset files

### Features
- YAML parsing with strict type conversion
- Schema validation for preset parameters
- Cross-reference validation between preset components
- Comprehensive error reporting

### Installation
```bash
git clone https://github.com/rozling/a8-validate.git
cd a8-validate
pip install -r requirements.txt
```

### Usage

#### Validate Preset Files
```bash
python validate_directory.py /path/to/presets --sample-dir /path/to/samples
```

#### Generate Reference Preset Files
The `scripts/generate_preset_ranges.py` utility generates example preset files showing the minimum and maximum allowed values for all parameters based on the validation schema:

```bash
python scripts/generate_preset_ranges.py
```

This creates two reference files:
- `preset_min_values.yml` - All parameters set to their minimum allowed values
- `preset_max_values.yml` - All parameters set to their maximum allowed values

These files serve as:
- **Documentation** - Quick reference for valid parameter ranges
- **Testing** - Example presets for validation tests
- **Development** - Understanding the schema without reading code

The script extracts min/max values from the schema definitions (`PRESET_SCHEMA`, `CHANNEL_SCHEMA`, `ZONE_SCHEMA`) and generates complete preset examples with all parameters set to their boundary values.

## TODO

### Code Improvements
- **Issue 2**: Fix misleading error message in `schema_validator.py` line 351 - The error message says "String representations are not allowed" for float types, but the code actually allows and converts string representations for integers and floats (lines 295-306). The error message should be updated to reflect the actual behavior.

- **Issue 3**: Review YAML loader usage in `yaml_parser.py` line 122 - Currently passing a string directly to `LineNumberLoader`. PyYAML loaders typically expect a stream. Consider using `io.StringIO` or `yaml.load()` with string input to ensure compatibility and follow best practices.

- **Issue 4**: Add validation for invalid XfadeGroup values in `cross_reference_validator.py` line 98 - If `XfadeGroup` is not 'A', 'B', 'C', or 'D', it's silently ignored. While schema validation should catch this, the cross-reference validator should also explicitly validate and report invalid group values.

### Changelog
See [CHANGELOG.md](CHANGELOG.md) for a detailed list of changes and updates.

### Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
