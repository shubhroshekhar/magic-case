## Magic Case

Lightweight utilities for converting strings between common cases, built on a simple `BaseCase` abstraction.

- **Cases**: `SnakeCase`, `CamelCase`, `PascalCase`, `KebabCase`, `UpperCase`, `SentenceCase`, `TitleCase`, `DotCase`, `SpaceCase`, `FlatCase`, `HttpHeaderCase`, `CamelSnakeCase`, `HungarianCase`, `MacroCase`, `PascalSnakeCase`, `PathCase`, `SlashTitleCase`
- **Composable**: Construct from raw strings or from another case class
- **Zero deps**: No runtime dependencies

### Installation
Using uv:
```bash
uv add magic-case
```

Standard pip:
```bash
pip install "magic-case"
```

### Quick start
```python
from magic_case import (
    SnakeCase,
    CamelCase,
    PascalCase,
    KebabCase,
    UpperCase,
    SentenceCase,
    TitleCase,
    DotCase,
    SpaceCase,
    FlatCase,
    HttpHeaderCase,
    CamelSnakeCase,
    HungarianCase,
    MacroCase,
    PascalSnakeCase,
    PathCase,
    SlashTitleCase,
)

# Convert a string to different cases
snake = SnakeCase('hello_world')
print(snake.get())  # hello_world
```

### Convert between cases

Construct from another case to re-render with a different style:
```python
from magic_case import SnakeCase, KebabCase, PascalCase

snake = SnakeCase("hello_world")

kebab = KebabCase(snake)
print(kebab)  # hello-world

pascal = PascalCase(snake)
print(pascal)  # HelloWorld
```

### Round-trip conversion example
```python
from magic_case import SnakeCase, KebabCase, CamelCase

original = SnakeCase("hello_world_example")
converted = KebabCase(original)
print(converted)  # hello-world-example

back_to_snake = SnakeCase(converted)
print(back_to_snake)  # hello_world_example
assert back_to_snake.words == original.words
```
Case Examples Table
| Case            | Input               | Output              |
| --------------- | ------------------- | ------------------- |
| SnakeCase       | `helloWorldAgain`   | `hello_world_again` |
| KebabCase       | `helloWorldAgain`   | `hello-world-again` |
| CamelCase       | `hello_world_again` | `helloWorldAgain`   |
| PascalCase      | `hello_world_again` | `HelloWorldAgain`   |
| UpperCase       | `hello_world_again` | `HELLO_WORLD_AGAIN` |
| SentenceCase    | `hello_world_again` | `Hello world again` |
| TitleCase       | `hello_world_again` | `Hello World Again` |
| DotCase         | `helloWorldAgain`   | `hello.world.again` |
| SpaceCase       | `helloWorldAgain`   | `hello world again` |
| FlatCase        | `helloWorldAgain`   | `helloworldagain`   |
| HttpHeaderCase  | `helloWorldAgain`   | `Hello-World-Again` |
| CamelSnakeCase  | `helloWorldAgain`   | `hello_World_Again` |
| HungarianCase   | `strHelloWorld`     | `str_hello_world`   |
| MacroCase       | `helloWorldAgain`   | `HELLO_WORLD_AGAIN` |
| PascalSnakeCase | `HelloWorldAgain`   | `Hello_World_Again` |
| PathCase        | `helloWorldAgain`   | `hello/world/again` |
| SlashTitleCase  | `helloWorldAgain`   | `Hello/World/Again` |


### API
- **`BaseCase`**
  - `words: List[str]` normalized to lowercase
  - `get() -> str` returns the rendered string (same as `str(instance)`)
  - Subclasses implement:
    - `_split_into_words(text: str) -> List[str]`
    - `__str__(self) -> str`
- **Concrete cases**
  - `SnakeCase`, `CamelCase`, `PascalCase`, `KebabCase`, `UpperCase`, `SentenceCase`, `TitleCase`, `DotCase`, `SpaceCase`, `FlatCase`, `HttpHeaderCase`, `CamelSnakeCase`, `HungarianCase`, `MacroCase`, `PascalSnakeCase`, `PathCase`, `SlashTitleCase`

### Requirements
- Python 3.8+

### Contributing

If you find a bug, unexpected behavior, or have ideas to improve magic-case, please report it via the [GitHub issues page](https://github.com/shubhroshekhar/magic-case). Your feedback helps make it better!


### License
MIT 