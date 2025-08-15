## Magic Case

Lightweight utilities for converting strings between common cases, built on a simple `BaseCase` abstraction.

- **Cases**: `SnakeCase`, `CamelCase`, `PascalCase`, `KebabCase`, `UpperCase`, `SentenceCase`, `TitleCase`
- **Composable**: Construct from raw strings or from another case class
- **Zero deps**: No runtime dependencies

### Installation
Using uv (recommended):
```bash
uv add magic-case>=0.2.0
```

Standard pip:
```bash
pip install "magic-case>=0.2.0"
```

### Quick start
```python
from magic_case import SnakeCase, CamelCase, PascalCase, KebabCase, UpperCase, SentenceCase, TitleCase

print(SnakeCase('hello_world').get())     # hello_world
print(CamelCase('helloWorld').get())      # helloWorld
print(PascalCase('HelloWorld').get())     # HelloWorld
print(KebabCase('hello-world').get())     # hello-world
print(UpperCase('hello_world').get())     # HELLO_WORLD
print(SentenceCase('hello world').get())  # Hello world
print(TitleCase('hello world').get())     # Hello World
```

### Convert between cases
Construct from another case to re-render with a different style:
```python
from magic_case import SnakeCase, CamelCase, PascalCase

snake = SnakeCase('hello_world')
print(CamelCase(snake).get())   # helloWorld
print(PascalCase(snake).get())  # HelloWorld
```

### API
- **`BaseCase`**
  - `words: List[str]` normalized to lowercase
  - `get() -> str` returns the rendered string (same as `str(instance)`)
  - Subclasses implement:
    - `_split_into_words(text: str) -> List[str]`
    - `__str__(self) -> str`
- **Concrete cases**
  - `SnakeCase`, `CamelCase`, `PascalCase`, `KebabCase`, `UpperCase`, `SentenceCase`, `TitleCase`

### Requirements
- Python 3.8+

### License
MIT 