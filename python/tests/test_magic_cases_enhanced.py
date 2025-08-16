import pytest

from magic_case import (
    CamelCase,
    CamelSnakeCase,
    DotCase,
    FlatCase,
    HttpHeaderCase,
    KebabCase,
    MacroCase,
    PascalCase,
    PascalSnakeCase,
    PathCase,
    SentenceCase,
    SlashTitleCase,
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
        (SpaceCase, "hello world", ["hello", "world"], "hello world"),
        (FlatCase, "helloworld", ["helloworld"], "helloworld"),
        (HttpHeaderCase, "Content-Type", ["content", "type"], "Content-Type"),
        (CamelSnakeCase, "hello_World", ["hello", "world"], "hello_World"),
        (MacroCase, "hello_world", ["hello", "world"], "HELLO_WORLD"),
        (PascalSnakeCase, "Hello_World", ["hello", "world"], "Hello_World"),
        (PathCase, "hello/world", ["hello", "world"], "hello/world"),
        (PathCase, "hello", ["hello"], "hello"),
        (SlashTitleCase, "hello/world", ["hello", "world"], "Hello/World"),
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


@pytest.mark.parametrize(
    "start_cls, input_str, target_cls, expected",
    [
        # SnakeCase -> others
        (SnakeCase, "hello_world", KebabCase, "hello-world"),
        (SnakeCase, "hello_world", CamelCase, "helloWorld"),
        (SnakeCase, "hello_world", PascalCase, "HelloWorld"),
        (SnakeCase, "hello_world", TitleCase, "Hello World"),
        (SnakeCase, "hello_world", UpperCase, "HELLO_WORLD"),
        (SnakeCase, "hello_world", DotCase, "hello.world"),
        # KebabCase -> others
        (KebabCase, "hello-world", SnakeCase, "hello_world"),
        (KebabCase, "hello-world", PascalCase, "HelloWorld"),
        (KebabCase, "hello-world", CamelCase, "helloWorld"),
        (KebabCase, "hello-world", UpperCase, "HELLO_WORLD"),
        # CamelCase -> others
        (CamelCase, "helloWorld", SnakeCase, "hello_world"),
        (CamelCase, "helloWorld", KebabCase, "hello-world"),
        (CamelCase, "helloWorld", PascalCase, "HelloWorld"),
        (CamelCase, "helloWorld", DotCase, "hello.world"),
        # PascalCase -> others
        (PascalCase, "HelloWorld", SnakeCase, "hello_world"),
        (PascalCase, "HelloWorld", KebabCase, "hello-world"),
        (PascalCase, "HelloWorld", TitleCase, "Hello World"),
        # TitleCase -> others
        (TitleCase, "hello world", SnakeCase, "hello_world"),
        (TitleCase, "hello world", CamelCase, "helloWorld"),
        (TitleCase, "hello world", PascalCase, "HelloWorld"),
        # DotCase -> others
        (DotCase, "hello.world", SnakeCase, "hello_world"),
        (DotCase, "hello.world", KebabCase, "hello-world"),
        (DotCase, "hello.world", PascalCase, "HelloWorld"),
        # UpperCase (macro style) -> others
        (UpperCase, "HELLO_WORLD", SnakeCase, "hello_world"),
        (UpperCase, "HELLO_WORLD", KebabCase, "hello-world"),
        (UpperCase, "HELLO_WORLD", PascalCase, "HelloWorld"),
        # FlatCase -> others
        (FlatCase, "helloworld", SnakeCase, "helloworld"),
        (FlatCase, "helloworld", PascalCase, "Helloworld"),
    ],
)
def test_cross_case_conversion(start_cls, input_str, target_cls, expected):
    """Ensure converting between different cases works as expected."""
    converted = target_cls(start_cls(input_str))
    assert str(converted) == expected
