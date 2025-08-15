## Magic Case

Monorepo for case-conversion utilities.

- **Python package**: `python/` (published to PyPI as `magic-case`)
- **JavaScript package**: `js/` (reserved; add when ready)

### Repo layout
```text
/
  README.md            # This file
  python/              # Python project root (uv + Hatchling)
    pyproject.toml
    README.md          # PyPI-focused usage/API docs
    magic_case/
      __init__.py
      base.py
      snake.py
      camel.py
      pascal.py
      kebab.py
      upper.py
      sentence.py
      title.py
  js/                  # JS project root (future)
```

### Prerequisites
- Python 3.8+
- `uv` (`pip install uv` or see `https://docs.astral.sh/uv/`)

### Develop the Python package
```bash
# From repo root
cd python
uv sync
```

Run a quick smoke test:
```bash
uv run python - <<'PY'
from magic_case import SnakeCase, CamelCase, PascalCase, KebabCase, UpperCase, SentenceCase, TitleCase
cases=[
    SnakeCase('hello_world').get(),
    CamelCase('helloWorld').get(),
    PascalCase('HelloWorld').get(),
    KebabCase('hello-world').get(),
    UpperCase('hello_world').get(),
    SentenceCase('hello world').get(),
    TitleCase('hello world').get(),
]
exp=['hello_world','helloWorld','HelloWorld','hello-world','HELLO_WORLD','Hello world','Hello World']
assert cases==exp, (cases, exp)
print('OK:', cases)
PY
```

Build and publish (requires credentials):
```bash
cd python
uv build
uv publish
```

### Package usage/API
See `python/README.md` for PyPI install instructions, examples, and API notes. 