# Development Guide

This guide explains how to set up and use the development tools for the `magic-case` project.

## Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) package manager

## Setup

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Install pre-commit hooks:**
   ```bash
   uv run pre-commit install
   ```

## Development Workflow

### Running Checks

Use the convenience script to run all checks:
```bash
python3 scripts/check.py
```

Or run individual checks:

- **Linting:** `uv run ruff check .`
- **Formatting:** `uv run ruff format .`
- **Tests:** `uv run pytest -q`

### Pre-commit Hooks

The project uses pre-commit hooks that automatically run on each commit:
- Ruff linting (with auto-fix)
- Ruff formatting

### Code Quality

- **Line length:** 88 characters (Black-compatible)
- **Python version:** 3.9+
- **Import sorting:** Automatic with isort
- **Type hints:** Modern Python syntax (`list[str]` instead of `List[str]`)

## CI/CD Pipeline

The GitHub Actions workflow runs:
- Tests on Python 3.9, 3.10, 3.11, 3.12
- Linting and formatting checks
- Matrix strategy for efficient parallel execution

## Adding New Dependencies

1. **Runtime dependencies:** Add to `[project].dependencies` in `pyproject.toml`
2. **Development dependencies:** Add to `[tool.uv].dev-dependencies`
3. **Update lock file:** `uv sync`

## Troubleshooting

- **Pre-commit fails:** Run `uv run pre-commit run --all-files` to see detailed errors
- **Linting issues:** Use `uv run ruff check --fix .` for auto-fixes
- **Formatting issues:** Use `uv run ruff format .` to reformat code
