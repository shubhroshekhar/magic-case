import pytest

from magic_case import (
    CamelCase,
    KebabCase,
    PascalCase,
    SentenceCase,
    SnakeCase,
    TitleCase,
    UpperCase,
)


def test_snake_case_basic():
    s = SnakeCase("hello_world")
    assert s.words == ["hello", "world"]
    assert str(s) == "hello_world"
    assert s.get() == "hello_world"


def test_kebab_case_basic():
    k = KebabCase("hello-world")
    assert k.words == ["hello", "world"]
    assert k.get() == "hello-world"


def test_camel_case_basic():
    c = CamelCase("helloWorld")
    assert c.words == ["hello", "world"]
    assert c.get() == "helloWorld"


def test_pascal_case_basic():
    p = PascalCase("HelloWorld")
    assert p.words == ["hello", "world"]
    assert p.get() == "HelloWorld"


def test_upper_case_basic():
    u = UpperCase("hello_world")
    assert u.words == ["hello", "world"]
    assert u.get() == "HELLO_WORLD"


def test_sentence_case_basic():
    s = SentenceCase("hello world")
    assert s.words == ["hello", "world"]
    assert s.get() == "Hello world"


def test_title_case_basic():
    t = TitleCase("hello world")
    assert t.words == ["hello", "world"]
    assert t.get() == "Hello World"


def test_cross_conversion_from_snake():
    snake = SnakeCase("hello_world")
    assert CamelCase(snake).get() == "helloWorld"
    assert PascalCase(snake).get() == "HelloWorld"
    assert KebabCase(snake).get() == "hello-world"
    assert UpperCase(snake).get() == "HELLO_WORLD"
    assert SentenceCase(snake).get() == "Hello world"
    assert TitleCase(snake).get() == "Hello World"


def test_invalid_input_type_raises():
    with pytest.raises(TypeError):
        # @ts-ignore - intentionally wrong type
        SnakeCase(123)  # type: ignore[arg-type]
