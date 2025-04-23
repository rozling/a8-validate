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
