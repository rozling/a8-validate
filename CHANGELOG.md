## [Unreleased]

## 13 November 2025

### Added
- GitHub Actions workflows for CI/CD
  - Test workflow: Multi-OS (Ubuntu, macOS, Windows) and multi-Python version (3.9-3.13) testing
  - Lint workflow: Code quality checks with flake8, black, and isort
  - Coverage workflow: Test coverage reporting with pytest-cov
  - Security workflow: Dependency vulnerability scanning with safety and pip-audit (runs weekly)
- Pre-commit hooks configuration
  - Automatic code formatting with black
  - Import sorting with isort
  - Linting with flake8
  - File validation (YAML, JSON, TOML)
  - Trailing whitespace and end-of-file fixes
- Development dependencies file (`requirements-dev.txt`)
  - Includes pytest-cov, black, isort, flake8, safety, pip-audit, pre-commit
- Code quality configuration files
  - `.flake8` configuration (120 char line length, compatible with black)
  - `.isort.cfg` configuration (black-compatible import sorting)
- Status badges in README.md
  - Tests, Lint, Coverage, and Security workflow badges

### Changed
- Updated YAML parsing to ensure strict numeric type conversion
  - Modified `construct_number()` in `yaml_parser.py` to convert numeric strings to actual numeric types
  - Ensures that float and integer values are parsed as their correct Python types
  - Preserves original numeric values while enforcing type consistency

### Validation Improvements
- Enhanced schema validation to require strict numeric types
  - Removed support for string representations of numbers
  - Provides clearer error messages about type requirements
  - Improves type safety for preset parameter parsing

### Fixed
- Resolved issues with numeric value parsing in Assimil8or preset files
  - Prevents validation errors caused by string-formatted numbers
  - Maintains compatibility with existing preset file formats

## 01 May 2025

- Enhanced schema validator to enforce maximum number of channels (8) and zones (8) per preset.
- Added validation to ensure channel and zone numbers are in numerical order without gaps or duplicates.
- Updated YAML parser to preprocess Assimil8or files with unquoted special-character values.
- Improved schema validator to accept numeric and special-character preset names.
- Added detailed line number reporting for schema validation errors.
- Updated tests to cover new validation rules and edge cases.

## 13 November 2025

### Fixed
- Fixed regex pattern bug in YAML parser that prevented line number extraction from error messages
- Fixed silent error masking in `get_sample_length()` - now properly raises FileSystemValidationError instead of returning 0
- Fixed error traceback output to always go to stderr instead of potentially going to output file
- Improved memory calculation fallback to skip problematic files with warnings instead of using inaccurate file size

### Changed
- Added explicit UTF-8 encoding to all file operations in YAML parser for cross-platform compatibility
- Documented data mutation behavior in validation functions (validate_preset, validate_channel, validate_zone)

### Validation Improvements
- Added validation to require at least one zone per channel (prevents invalid empty channels)
- Enhanced error handling in file system validator to properly report WAV file read errors

