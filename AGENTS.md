# AGENTS.md

Instructions for AI agents (e.g. Cursor Cloud) working on this repository.

This is a **pure-Python CLI tool** — no web server, database, or Docker. See `README.md` for usage and `CONTRIBUTING.md` for contributor workflow.

---

## Quick reference

| Task | Command |
|------|---------|
| **Run tests** | `venv/bin/pytest -v --tb=short` (52 tests, ~0.1s) |
| **Lint** | `venv/bin/flake8 a8_validate/ scripts/ validate_directory.py --max-line-length=120 --extend-ignore=E203,W503,D` |
| **Format (check)** | `venv/bin/black --check a8_validate/ scripts/ validate_directory.py` |
| **Format (apply)** | `venv/bin/black a8_validate/ scripts/ validate_directory.py` |
| **Imports (check)** | `venv/bin/isort --check-only a8_validate/ scripts/ validate_directory.py` |
| **Imports (apply)** | `venv/bin/isort a8_validate/ scripts/ validate_directory.py` |
| **Run CLI** | `venv/bin/a8-validate <directory> --verbose` or `venv/bin/python validate_directory.py <directory> --verbose` |
| **Validate subdirs** | `venv/bin/python scripts/validate_all_subdirs.py <directory>` |
| **Generate ranges** | `PYTHONPATH=/workspace venv/bin/python scripts/generate_preset_ranges.py` |

---

## Before committing

1. Run tests: `venv/bin/pytest -v --tb=short`
2. Run lint: flake8 (see table above)
3. Run format check: black and isort (or use `venv/bin/pre-commit run`)
4. Add a `CHANGELOG.md` entry for any behavior, docs, or tooling change

---

## Non-obvious caveats

- **Venv setup:** `python3.12-venv` must be installed before creating the venv (not present by default on Ubuntu 24.04 minimal images).
- **PYTHONPATH:** `scripts/generate_preset_ranges.py` requires `PYTHONPATH=/workspace` (or equivalent) to resolve the `a8_validate` package. The main CLI (`validate_directory.py`) does not need this.
- **Flake8 config:** D-series (docstrings) and black-related deltas are ignored via `extend-ignore` so pre-commit passes.
- **wave module:** Part of the Python standard library — never add it to `requirements.txt`.

---

## File layout

| Path | Purpose |
|------|---------|
| `a8_validate/` | Core validation logic (schema, cross-ref, WAV checks) |
| `validate_directory.py` | CLI script (also exposed as `a8-validate` via pyproject.toml) |
| `pyproject.toml` | Package metadata, dependencies, console script entrypoint |
| `scripts/` | Utilities: `validate_all_subdirs.py`, `generate_preset_ranges.py` |
| `a8_validate/tests/` | Pytest suite |

---

## Common agent tasks

- **Validate presets:** Run the CLI on a directory; use `--verbose` and `--output` as needed.
- **Change validation logic:** Update code in `a8_validate/`, add or adjust tests in `a8_validate/tests/`.
- **Fix formatting:** Run `black` and `isort` with apply mode (no `--check-only`).

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: No module named 'a8_validate'` when running a script | Set `PYTHONPATH=/workspace` (or equivalent) before running. |
| Pre-commit fails on flake8/black/isort | Run the apply commands from the quick reference table; ensure extend-ignore for flake8. |
| Venv creation fails on minimal Ubuntu | Install `python3.12-venv` first. |
