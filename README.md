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
```bash
python validate_directory.py /path/to/presets --sample-dir /path/to/samples
```

### Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
