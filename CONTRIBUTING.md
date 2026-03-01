# Contributing to a8-validate

Thanks for helping improve the Assimil8or preset validator! This document explains how to get set up, the project conventions, and the pull request checklist.

## Local Setup

```bash
git clone https://github.com/rozling/a8-validate.git
cd a8-validate

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

We keep runtime dependencies (`requirements.txt`) lean; the `requirements-dev.txt` file installs the formatting, linting, testing, and security tooling.

## Development Workflow

1. Create a feature branch off `main`.
2. Make focused commits with clear messages.
3. Keep documentation (README, CHANGELOG) in sync with behavior changes.
4. Ensure every CLI or validation change is covered by tests.

## Formatting, Linting & Tests

**Recommended:** Install pre-commit hooks once so every commit runs black, isort, and flake8 automatically:

```bash
venv/bin/pre-commit install
```

Then before pushing, run tests:

```bash
venv/bin/pytest -v --tb=short
```

If you don’t use the hook, run formatting and lint manually before committing:

```bash
venv/bin/pre-commit run --all-files
# or individually:
venv/bin/black a8_validate/ scripts/ validate_directory.py
venv/bin/isort a8_validate/ scripts/ validate_directory.py
venv/bin/flake8 a8_validate/ scripts/ validate_directory.py
venv/bin/pytest -v --tb=short
```

## Pull Request Checklist

- [ ] Tests pass locally (`venv/bin/pytest -v --tb=short`).
- [ ] `black`, `isort`, and `flake8` pass with the repository settings (120 character columns).
- [ ] User documentation updated (README, CLI help, CHANGELOG) when behavior changes.
- [ ] No generated files or local artifacts committed.
- [ ] Include context in the PR description: what changed, why, and how it’s tested.

## Reporting Bugs & Requesting Features

- Use GitHub Issues for bugs or feature requests.
- Include sample preset files (or redacted snippets) when reporting validation problems.
- Describe the expected vs. actual validator output.

## Release Management

Before tagging a release:

1. Ensure `CHANGELOG.md` has an entry for the release.
2. Run the full test suite.
3. Verify CI workflows (Tests, Lint, Coverage, Security) are green.
4. Create a Git tag (e.g. `v1.0.0`) and push tags to GitHub.

Thanks again for contributing! If you have questions, open an issue or start a discussion on GitHub.***
