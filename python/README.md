# Magic Case - Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A magical text case converter for Python that provides simple and intuitive functions to transform strings between different case formats.

## Features

- **Simple API**: Clean, easy-to-use functions for case conversion
- **Type Safe**: Full type hints for better IDE support and type checking
- **Error Handling**: Proper error handling with descriptive messages
- **Lightweight**: No external dependencies
- **Python 3.7+**: Compatible with modern Python versions

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/magic-case.git
cd magic-case/python

# Install the package
pip install .
```

### For Development

```bash
# Clone and install in development mode
git clone https://github.com/yourusername/magic-case.git
cd magic-case/python
pip install -e .
```

## Usage

```python
from magic_case import (
    to_upper_case,
    to_lower_case,
    to_camel_case,
    to_pascal_case,
    to_snake_case,
    to_kebab_case,
)

# Basic case conversions
text = "hello world example"

print(to_upper_case(text))    # "HELLO WORLD EXAMPLE"
print(to_lower_case(text))    # "hello world example"
print(to_camel_case(text))    # "helloWorldExample"
print(to_pascal_case(text))   # "HelloWorldExample"
print(to_snake_case(text))    # "hello_world_example"
print(to_kebab_case(text))    # "hello-world-example"
```

## API Reference

### `to_upper_case(text: str) -> str`

Converts text to UPPERCASE.

```python
to_upper_case("hello world")  # "HELLO WORLD"
```

### `to_lower_case(text: str) -> str`

Converts text to lowercase.

```python
to_lower_case("HELLO WORLD")  # "hello world"
```

### `to_camel_case(text: str) -> str`

Converts text to camelCase (first word lowercase, subsequent words capitalized).

```python
to_camel_case("hello world")  # "helloWorld"
to_camel_case("user profile settings")  # "userProfileSettings"
```

### `to_pascal_case(text: str) -> str`

Converts text to PascalCase (all words capitalized, no spaces).

```python
to_pascal_case("hello world")  # "HelloWorld"
to_pascal_case("user profile settings")  # "UserProfileSettings"
```

### `to_snake_case(text: str) -> str`

Converts text to snake_case (lowercase words separated by underscores).

```python
to_snake_case("hello world")  # "hello_world"
to_snake_case("User Profile Settings")  # "user_profile_settings"
```

### `to_kebab_case(text: str) -> str`

Converts text to kebab-case (lowercase words separated by hyphens).

```python
to_kebab_case("hello world")  # "hello-world"
to_kebab_case("User Profile Settings")  # "user-profile-settings"
```

## Error Handling

All functions include proper error handling and will raise a `TypeError` if the input is not a string:

```python
try:
    result = to_camel_case(123)  # This will raise TypeError
except TypeError as e:
    print(e)  # "Input must be a string"
```

## Examples

### Common Use Cases

```python
from magic_case import to_snake_case, to_camel_case, to_kebab_case

# Converting API responses
api_field = "firstName"
db_column = to_snake_case(api_field)  # "first_name"

# Converting database fields to frontend
db_field = "user_profile_image"
js_property = to_camel_case(db_field)  # "userProfileImage"

# Converting for CSS classes
component_name = "User Profile Card"
css_class = to_kebab_case(component_name)  # "user-profile-card"

# Converting form labels
form_field = "email_address"
label_text = form_field.replace('_', ' ').title()  # "Email Address"
```

### Chaining Conversions

```python
# You can chain conversions for complex transformations
original = "HelloWorldExample"
result = to_kebab_case(to_snake_case(original))  # "hello-world-example"
```

## Development

### Setting Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e .
pip install pytest pytest-cov black isort mypy
```

### Running Tests

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=magic_case

# Run type checking
mypy magic_case/
```

### Code Formatting

```bash
# Format code
black magic_case/
isort magic_case/
```

### Building the Package

```bash
# Build source and wheel distributions
python -m build

# The built packages will be in the dist/ directory
ls dist/
# magic_case-0.0.1-py3-none-any.whl
# magic_case-0.0.1.tar.gz
```

## Requirements

- Python 3.7 or higher
- No external dependencies for runtime

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

**Shubhro Shekhar** - [shubhroshekhar@gmail.com](mailto:shubhroshekhar@gmail.com)

## Changelog

### v0.0.1 (Initial Release)
- Basic case conversion functions
- Type hints and error handling
- Comprehensive test coverage
- Documentation and examples
