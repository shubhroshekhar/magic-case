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

## Release Management

### Version Management

Use the release script to manage versions:

```bash
# Check current version
python3 scripts/release.py check

# Bump version (auto-increment)
python3 scripts/release.py bump --type patch    # 0.2.0 → 0.2.1
python3 scripts/release.py bump --type minor    # 0.2.0 → 0.3.0
python3 scripts/release.py bump --type major    # 0.2.0 → 1.0.0

# Set specific version
python3 scripts/release.py bump --version 0.2.1

# Create release (runs checks, creates tag, pushes)
python3 scripts/release.py release
```

### Release Process

1. **Update version** in `pyproject.toml` (or use the bump script)
2. **Create release** using the release script
3. **GitHub Actions** automatically:
   - Runs tests and linting
   - Creates a GitHub release
   - Builds and uploads the package
   - **Publishes to PyPI** (if configured)

### PyPI Publishing

The project includes automatic PyPI publishing workflows:

#### **Automatic Publishing**
- **Release workflow** (`release.yml`): Publishes to PyPI when creating releases
- **PyPI workflow** (`pypi-publish.yml`): Dedicated PyPI publishing with test options

#### **Manual Publishing**
```bash
# Via GitHub Actions UI:
# 1. Go to Actions → Publish to PyPI
# 2. Enter version (e.g., "0.2.0")
# 3. Choose dry_run: true for TestPyPI, false for PyPI
# 4. Run workflow
```

#### **PyPI Configuration**
To enable PyPI publishing, add these secrets to your GitHub repository:

1. **Go to:** Settings → Secrets and variables → Actions
2. **Add secret:** `PYPI_API_TOKEN`
3. **Value:** Your PyPI API token from https://pypi.org/manage/account/token/

#### **TestPyPI (Optional)**
For testing before production:
- Use `dry_run: true` in the PyPI workflow
- Publishes to TestPyPI instead of PyPI
- Safe for testing package builds and uploads

### Automatic Tagging

The CI/CD pipeline automatically creates git tags when:
- Merging to `main`, `master`, or `prod` branches
- Pushing tags manually
- Using the manual workflow dispatch

## CI/CD Pipeline

The GitHub Actions workflow runs:
- Tests on Python 3.9, 3.10, 3.11, 3.12
- Linting and formatting checks
- Matrix strategy for efficient parallel execution
- Automatic tag creation on production branches
- Release creation on tag push

## Adding New Dependencies

1. **Runtime dependencies:** Add to `[project].dependencies` in `pyproject.toml`
2. **Development dependencies:** Add to `[tool.uv].dev-dependencies`
3. **Update lock file:** `uv sync`

## Troubleshooting

- **Pre-commit fails:** Run `uv run pre-commit run --all-files` to see detailed errors
- **Linting issues:** Use `uv run ruff check --fix .` for auto-fixes
- **Formatting issues:** Use `uv run ruff format .` to reformat code
- **Release fails:** Check that version in `pyproject.toml` matches the tag version
