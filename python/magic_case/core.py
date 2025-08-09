# magic_case/core.py

def to_upper_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()


def to_lower_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.lower()


def to_camel_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    parts = text.split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])


def to_pascal_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return ''.join(word.capitalize() for word in text.split())


def to_snake_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return '_'.join(text.lower().split())


def to_kebab_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return '-'.join(text.lower().split())
