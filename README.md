## Assimil8or Preset Validator (a8-validate)

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
git clone https://github.com/yourusername/a8-validate.git
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

## Changelog
- 23 April 2025: Refactored the `find_yml_files` function to ignore system files:
  - folderprefs.yml, lastfolder.yml, lastpreset.yml, midi*.yml, and hidden files starting with ._.

### Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
