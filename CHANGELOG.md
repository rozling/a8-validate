## [Unreleased]

## 23 November 2025

### Added
- Added missing channel parameters to schema:
  - `PanMod` (cv_input_with_amount format, e.g., "0A 1.00")
  - `AutoTrigger` (integer, 0 or 1)
  - `LinAMisExtEnv` (integer, 0 or 1)
  - `LoopLengthIsEnd` (integer, 0 or 1)
- Updated `PMSource` validation to accept values 0-10:
  - 0-7: channels
  - 8: left input
  - 9: right input
  - 10: select CV
- Added `validate_all_subdirs.py` utility script for validating large preset collections
- CI/CD optimizations:
  - Added concurrency groups to cancel outdated workflow runs
  - Reduced PR test matrix (Ubuntu + Windows for PRs, all OSes for main)
  - Skip workflows on draft PRs
  - Parallel test execution with pytest-xdist
  - Cache lint dependencies

### Changed
- Allow non-sequential channels in presets (e.g., channels 1, 4, 7)
  - Channels must still be in ascending order
  - Channels must be in valid range (1-8)
- Allow `LoopLength` without `LoopStart` (LoopStart defaults to 0)
  - `LoopStart` still requires `LoopLength` to be defined
- Removed validation for `SampleEnd` exceeding sample length
  - Assimil8or automatically clamps SampleEnd to file length internally
  - This was causing false positive errors

### Fixed
- Fixed linting errors in `validate_all_subdirs.py` script
- All 49 tests passing with updated validation rules

## 23 November 2025 (Earlier)

### Added
- Created `.cursorrules` file to ensure Cursor AI always uses the virtual environment
- Added VS Code workspace settings (`.vscode/settings.json`) for Python development:
  - Automatic virtual environment activation
  - Format on save with black
  - Import sorting with isort
  - Linting configuration with flake8
  - Pytest testing configuration
- Added public-facing documentation and policies:
  - `LICENSE` (MIT)
  - `CONTRIBUTING.md`
  - `CODE_OF_CONDUCT.md`
  - `SECURITY.md`
- Added GitHub issue templates:
  - Bug report template
  - Feature request template
  - Validation issue template (for false positives/negatives)
- Added Dependabot configuration for automated dependency updates:
  - Weekly updates for Python dependencies (pip)
  - Weekly updates for GitHub Actions
  - Grouped updates for production and dev dependencies

### Fixed
- Removed `wave` package from `requirements.txt` (it's a standard library module in Python)
  - Fixed dependency installation failures in CI/CD workflows
  - The PyPI `wave` package was pulling in incompatible Python 2 dependencies

### Changed
- Fixed all linting issues to pass CI/CD checks:
  - Removed unused imports (`os`, `Dict`, `Any` from `validate_directory.py`; `re`, `collections` from `yaml_parser.py`)
  - Fixed line length violations (wrapped long lines to comply with 120 character limit)
  - Removed unused variables (`channel_loop_start`, `channel_loop_length`, `channel_number`, `zone_number`, `n_frames`)
  - Formatted all code with `black` and `isort`
- Rewrote README with concise setup/usage instructions and added a direct link to `CHANGELOG.md`
- Extended `.cursorrules` Git workflow rules to enforce changelog updates with every behavior or documentation change
- Removed the vendor `assimil8or.md` manual from the repository to avoid redistributing copyrighted material
- Moved `pytest` out of `requirements.txt` (runtime dependencies) and ensured `requirements-dev.txt` includes `-r requirements.txt`
- Added an explicit “use at your own risk” warning to the README to clarify there are no warranties
- All 49 tests still passing after code cleanup

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

