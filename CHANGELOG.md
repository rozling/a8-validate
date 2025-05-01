## [Unreleased]

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
