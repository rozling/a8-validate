# AGENTS.md

## Cursor Cloud specific instructions

This is a pure-Python CLI tool (no web server, no database, no Docker). See `README.md` and `CONTRIBUTING.md` for standard commands.

### Quick reference

- **Tests:** `venv/bin/pytest -v --tb=short` (52 tests, ~0.1s)
- **Lint:** `venv/bin/flake8 a8_validate/ scripts/ validate_directory.py --max-line-length=120 --extend-ignore=E203,W503`
- **Format check:** `venv/bin/black --check a8_validate/ scripts/ validate_directory.py`
- **Import sort check:** `venv/bin/isort --check-only a8_validate/ scripts/ validate_directory.py`
- **Run CLI:** `venv/bin/python validate_directory.py <directory> --verbose`

### Non-obvious caveats

- The system package `python3.12-venv` must be installed before creating the venv (not present by default on Ubuntu 24.04 minimal images).
- `scripts/generate_preset_ranges.py` requires `PYTHONPATH=/workspace` (or equivalent) to resolve the `a8_validate` package; the main CLI entry point (`validate_directory.py`) does not need this.
- Pre-existing flake8 docstring warnings (D-series) and one black formatting delta exist in the repo; these are not regressions.
- The `wave` module is part of the Python standard library — never add it to `requirements.txt`.
