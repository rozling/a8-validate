# Assimil8or Preset Validator (a8-validate)

> Python validator for Assimil8or preset YAML files. Ensures schema compliance, validates cross-references, and checks WAV file compatibility.

[![Tests](https://github.com/rozling/a8-validate/workflows/Tests/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/test.yml)
[![Lint](https://github.com/rozling/a8-validate/workflows/Lint/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/lint.yml)
[![Coverage](https://github.com/rozling/a8-validate/workflows/Coverage/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/coverage.yml)
[![Security](https://github.com/rozling/a8-validate/workflows/Security/badge.svg)](https://github.com/rozling/a8-validate/actions/workflows/security.yml)

### Features

This is a python library / set of programs which:
- Parse Assimil8or `.yml` preset files
- Enforce the preset schema (inferred from existing A8 presets)
- Check channel/zone cross-references
- Validate referenced WAV files exist and are compatible:
  - File format (valid WAV)
  - Channels: 1-2
  - Sample rates: 44.1/48/96/192kHz
  - Sample width: 8/16/24/32 bits
  - Loop/start/end positions don't exceed file length

Use it to:
- Run before copying presets to your card so you catch problems immediately.
- Validate presets created by another program or AI

### Background

- This stemmed from one day asking AI to come up with some cool preset ideas.
- The ideas were great but when it came to creating the actual presets of course it hallucinated the format / features etc.
- These tools should help any person / program creating A8 presets to ensure they are as correct as possible.

### Warning!

This tool is provided “as is”, without any warranties.
Always keep backups of your presets and samples.
The authors are not responsible for any data loss, corrupted files, or equipment damage resulting from its use.

---

### Installation

```bash
git clone https://github.com/rozling/a8-validate.git
cd a8-validate

python3 -m venv venv          # or reuse your preferred venv location
source venv/bin/activate
pip install -e .              # editable install (includes a8-validate CLI)
# or: pip install -e ".[dev]"  # with dev dependencies for testing/linting
```

Alternatively, `pip install -r requirements.txt` still works for running `python validate_directory.py`.

**Before committing:** install pre-commit so lint/format run automatically and CI stays green:

```bash
pip install pre-commit   # or use venv/bin/pre-commit
pre-commit install
```

---

### How to use

Validate a Preset Folder:

```bash
a8-validate /path/to/presets --verbose
```

Or with the script directly: `python validate_directory.py /path/to/presets --verbose`

Useful flags:

- `--output results.txt` – also write run output to a file
- `--verbose` – log each preset as it is processed
- `--help` – list all CLI options

The script scans for `.yml` presets (system files are skipped), validates schema + cross references, and checks every referenced sample. Successful run:

```
Found 12 preset files. Starting validation...
✓ VALID
...
Validation complete: 12/12 files valid
```

Failures pinpoint the preset/channel/zone and the exact parameter or sample path that broke the rules.

---

### Validate All Subdirectories

To validate all subdirectories in a parent directory (useful for large preset collections):

```bash
python scripts/validate_all_subdirs.py /path/to/parent/directory
```

This script recursively validates all subdirectories and provides a summary of valid presets and any issues found.

### Generate Boundary Reference Presets

Need to see the min/max values allowed by the schema?

```bash
python scripts/generate_preset_ranges.py
```

This writes `preset_min_values.yml` and `preset_max_values.yml`. Use them as documentation, regression fixtures, or template presets.

---

### Run the Test Suite

```bash
venv/bin/pytest -v --tb=short
```

49 tests cover schema validation, YAML parsing, cross-reference logic, and file-system checks. Run them before pushing or opening PRs whenever validation code changes.

---

### Repository Layout

| Path                     | Purpose                                   |
|--------------------------|-------------------------------------------|
| `a8_validate/`           | Core validators (schema, cross-ref, I/O) |
| `validate_directory.py`  | CLI entry point                          |
| `scripts/`               | Helper utilities (e.g., preset ranges)   |
| `a8_validate/tests/`     | Pytest suite                             |

---

### Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, code style guidelines, and the pull request process.

Additional resources:
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations
- [SECURITY.md](SECURITY.md) for responsible disclosure instructions
- [CHANGELOG.md](CHANGELOG.md) for release history

Licensed under the MIT License.
