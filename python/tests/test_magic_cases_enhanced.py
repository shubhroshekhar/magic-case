import pytest

from magic_case import (
    CamelCase,
    DotCase,
    FlatCase,
    HttpHeaderCase,
    KebabCase,
    MacroCase,
    PascalCase,
    PascalSnakeCase,
    SentenceCase,
    SnakeCase,
    SpaceCase,
    TitleCase,
    UpperCase,
)


@pytest.mark.parametrize(
    "cls, input_str, expected_words, expected_str",
    [
        (SnakeCase, "hello_world", ["hello", "world"], "hello_world"),
        (KebabCase, "hello-world", ["hello", "world"], "hello-world"),
        (CamelCase, "helloWorld", ["hello", "world"], "helloWorld"),
        (PascalCase, "HelloWorld", ["hello", "world"], "HelloWorld"),
        (UpperCase, "hello_world", ["hello", "world"], "HELLO_WORLD"),
        (SentenceCase, "hello world", ["hello", "world"], "Hello world"),
        (TitleCase, "hello world", ["hello", "world"], "Hello World"),
        (DotCase, "hello.world", ["hello", "world"], "hello.world"),
        # (SpaceCase, "hello world", ["hello", "world"], "hello world"),
        (FlatCase, "helloworld", ["helloworld"], "helloworld"),
        (HttpHeaderCase, "hello-world", ["hello", "world"], "Hello-World"),
        # (CamelSnakeCase, "hello_World", ["hello", "world"], "hello_World"),
        (MacroCase, "hello_world", ["hello", "world"], "HELLO_WORLD"),
        (PascalSnakeCase, "Hello_World", ["hello", "world"], "Hello_World"),
        # (PathCase, "hello/world", ["hello", "world"], "hello/world"),
        # (SlashTitleCase, "hello/world", ["hello", "world"], "Hello/World"),
    ],
)
def test_basic_cases(cls, input_str, expected_words, expected_str):
    case = cls(input_str)
    assert case.words == expected_words
    assert str(case) == expected_str
    assert case.get() == expected_str


def test_cross_conversion_chaining():
    assert str(KebabCase(SnakeCase("hello_world"))) == "hello-world"
    assert str(SnakeCase(KebabCase("hello-world"))) == "hello_world"
    assert str(PascalCase(CamelCase("helloWorld"))) == "HelloWorld"
    assert str(UpperCase(TitleCase("hello world"))) == "HELLO_WORLD"


@pytest.mark.parametrize(
    "start_cls", [SnakeCase, KebabCase, CamelCase, PascalCase, DotCase, SpaceCase]
)
def test_round_trip(start_cls):
    """Converting to another case and back should preserve words."""
    original = start_cls("foo_barBaz.qux")
    for target_cls in [SnakeCase, KebabCase, CamelCase, PascalCase, TitleCase]:
        converted = target_cls(original)
        back = start_cls(converted)
        assert back.words == original.words


def test_single_word_and_empty_string():
    assert str(CamelCase("hello")) == "hello"
    assert str(SnakeCase("")) == ""


def test_numbers_in_words():
    s = SnakeCase("hello123_world456")
    assert s.words == ["hello123", "world456"]


def test_invalid_input_type_raises():
    with pytest.raises(TypeError):
        SnakeCase(123)  # type: ignore[arg-type]


def test_non_string_word_raises():
    class BadCase(SnakeCase):
        def _split_into_words(self, text):
            return ["ok", 123]  # bad: int inside list

    with pytest.raises(ValueError):
        BadCase("ok123")
