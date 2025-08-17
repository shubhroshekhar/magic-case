import pytest

from magic_case import (
    CamelCase,
    CamelSnakeCase,
    DotCase,
    FlatCase,
    HttpHeaderCase,
    HungarianCase,
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
        (UpperCase, "hello_world", ["hello", "world"], "HELLO_WORLD"),
        (SentenceCase, "hello world", ["hello", "world"], "Hello world"),
        (TitleCase, "hello world", ["hello", "world"], "Hello World"),
        (DotCase, "hello.world", ["hello", "world"], "hello.world"),
        (SpaceCase, "hello world", ["hello", "world"], "hello world"),
        (FlatCase, "helloworld", ["helloworld"], "helloworld"),
        (CamelSnakeCase, "hello_World", ["hello", "world"], "hello_World"),
        (MacroCase, "hello_world", ["hello", "world"], "HELLO_WORLD"),
        (PascalSnakeCase, "Hello_World", ["hello", "world"], "Hello_World"),
        (PathCase, "hello/world", ["hello", "world"], "hello/world"),
        (PathCase, "hello", ["hello"], "hello"),
        (SlashTitleCase, "hello/world", ["hello", "world"], "Hello/World"),
        # SnakeCase
        (SnakeCase, "hello_world", ["hello", "world"], "hello_world"),
        (
            SnakeCase,
            "hello_world_again",
            ["hello", "world", "again"],
            "hello_world_again",
        ),
        (
            SnakeCase,
            "one_two_three_four",
            ["one", "two", "three", "four"],
            "one_two_three_four",
        ),
        # KebabCase
        (KebabCase, "hello-world", ["hello", "world"], "hello-world"),
        (
            KebabCase,
            "hello-world-again",
            ["hello", "world", "again"],
            "hello-world-again",
        ),
        (
            KebabCase,
            "one-two-three-four",
            ["one", "two", "three", "four"],
            "one-two-three-four",
        ),
        # CamelCase
        (CamelCase, "helloWorld", ["hello", "World"], "helloWorld"),
        (CamelCase, "helloWorldAgain", ["hello", "World", "Again"], "helloWorldAgain"),
        (
            CamelCase,
            "oneTwoThreeFour",
            ["one", "Two", "Three", "Four"],
            "oneTwoThreeFour",
        ),
        # PascalCase
        (PascalCase, "HelloWorld", ["Hello", "World"], "HelloWorld"),
        (PascalCase, "HelloWorldAgain", ["Hello", "World", "Again"], "HelloWorldAgain"),
        (
            PascalCase,
            "OneTwoThreeFour",
            ["One", "Two", "Three", "Four"],
            "OneTwoThreeFour",
        ),
        # UpperCase
        (UpperCase, "hello_world", ["hello", "world"], "HELLO_WORLD"),
        (
            UpperCase,
            "hello_world_again",
            ["hello", "world", "again"],
            "HELLO_WORLD_AGAIN",
        ),
        (
            UpperCase,
            "one_two_three_four",
            ["one", "two", "three", "four"],
            "ONE_TWO_THREE_FOUR",
        ),
        # SentenceCase
        (SentenceCase, "hello world", ["hello", "world"], "Hello world"),
        (
            SentenceCase,
            "hello world again",
            ["hello", "world", "again"],
            "Hello world again",
        ),
        (
            SentenceCase,
            "one two three four",
            ["one", "two", "three", "four"],
            "One two three four",
        ),
        # TitleCase
        (TitleCase, "hello world", ["hello", "world"], "Hello World"),
        (
            TitleCase,
            "hello world again",
            ["hello", "world", "again"],
            "Hello World Again",
        ),
        (
            TitleCase,
            "one two three four",
            ["one", "two", "three", "four"],
            "One Two Three Four",
        ),
        # DotCase
        (DotCase, "hello.world", ["hello", "world"], "hello.world"),
        (
            DotCase,
            "hello.world.again",
            ["hello", "world", "again"],
            "hello.world.again",
        ),
        (
            DotCase,
            "one.two.three.four",
            ["one", "two", "three", "four"],
            "one.two.three.four",
        ),
        # SpaceCase
        (SpaceCase, "hello world", ["hello", "world"], "hello world"),
        (
            SpaceCase,
            "hello world again",
            ["hello", "world", "again"],
            "hello world again",
        ),
        (
            SpaceCase,
            "one two three four",
            ["one", "two", "three", "four"],
            "one two three four",
        ),
        # FlatCase
        (FlatCase, "helloworld", ["helloworld"], "helloworld"),
        (FlatCase, "helloworldagain", ["helloworldagain"], "helloworldagain"),
        (FlatCase, "onetwothreefour", ["onetwothreefour"], "onetwothreefour"),
        # HttpHeaderCase
        (HttpHeaderCase, "Content-Type", ["Content", "Type"], "Content-Type"),
        (
            HttpHeaderCase,
            "Content-Security-Policy",
            ["Content", "Security", "Policy"],
            "Content-Security-Policy",
        ),
        (
            HttpHeaderCase,
            "X-Content-Security-Policy-Mode",
            ["X", "Content", "Security", "Policy", "Mode"],
            "X-Content-Security-Policy-Mode",
        ),
        # CamelSnakeCase
        (CamelSnakeCase, "hello_World", ["hello", "world"], "hello_World"),
        (
            CamelSnakeCase,
            "hello_World_Again",
            ["hello", "world", "again"],
            "hello_World_Again",
        ),
        (
            CamelSnakeCase,
            "one_Two_Three_Four",
            ["one", "two", "three", "four"],
            "one_Two_Three_Four",
        ),
        # MacroCase
        (MacroCase, "hello_world", ["hello", "world"], "HELLO_WORLD"),
        (
            MacroCase,
            "hello_world_again",
            ["hello", "world", "again"],
            "HELLO_WORLD_AGAIN",
        ),
        (
            MacroCase,
            "one_two_three_four",
            ["one", "two", "three", "four"],
            "ONE_TWO_THREE_FOUR",
        ),
        # PascalSnakeCase
        (PascalSnakeCase, "Hello_World", ["hello", "world"], "Hello_World"),
        (
            PascalSnakeCase,
            "Hello_World_Again",
            ["hello", "world", "again"],
            "Hello_World_Again",
        ),
        (
            PascalSnakeCase,
            "One_Two_Three_Four",
            ["one", "two", "three", "four"],
            "One_Two_Three_Four",
        ),
        # PathCase
        (PathCase, "hello/world", ["hello", "world"], "hello/world"),
        (
            PathCase,
            "hello/world/again",
            ["hello", "world", "again"],
            "hello/world/again",
        ),
        (
            PathCase,
            "one/two/three/four",
            ["one", "two", "three", "four"],
            "one/two/three/four",
        ),
        (PathCase, "hello", ["hello"], "hello"),
        # SlashTitleCase
        (SlashTitleCase, "hello/world", ["hello", "world"], "Hello/World"),
        (
            SlashTitleCase,
            "hello/world/again",
            ["hello", "world", "again"],
            "Hello/World/Again",
        ),
        (
            SlashTitleCase,
            "one/two/three/four",
            ["one", "two", "three", "four"],
            "One/Two/Three/Four",
        ),
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
    "start_cls", [SnakeCase, KebabCase, CamelCase, DotCase, SpaceCase]
)
def test_round_trip(start_cls):
    """Converting to another case and back should preserve words."""
    original = start_cls("foo_barBaz.qux")
    for target_cls in [SnakeCase, KebabCase, CamelCase, TitleCase]:
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
        (SnakeCase, "str_hello_world", HungarianCase, "strHelloWorld"),
        (SnakeCase, "hello_world", HungarianCase, "helloWorld"),
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
        # HungarianCase -> others
        (HungarianCase, "strHelloWorld", SnakeCase, "hello_world"),
        (HungarianCase, "strHelloWorld", KebabCase, "hello-world"),
        (HungarianCase, "strHelloWorld", CamelCase, "helloWorld"),
        (HungarianCase, "strHelloWorld", PascalCase, "HelloWorld"),
        (HungarianCase, "strHelloWorld", TitleCase, "Hello World"),
        (HungarianCase, "strHelloWorld", UpperCase, "HELLO_WORLD"),
    ],
)
def test_cross_case_conversion(start_cls, input_str, target_cls, expected):
    """Ensure converting between different cases works as expected."""
    converted = target_cls(start_cls(input_str))
    assert str(converted) == expected


def test_space_case_extra_whitespace():
    case = SpaceCase("   hello   world   again  ")
    assert case.words == ["hello", "world", "again"]
    assert str(case) == "hello world again"


def test_invalid_format_raises():
    with pytest.raises(ValueError):
        CamelCase("Hello_world")  # CamelCase must start with a lowercase letter


def test_path_case_double_slash():
    with pytest.raises(ValueError):
        PathCase("foo//bar")


# -----------------
# Camel / Pascal Edge Cases
# -----------------
def test_camel_case_acronyms():
    assert CamelCase("myHTTPServer").words == ["my", "HTTP", "Server"]


def test_pascal_case_acronyms():
    assert PascalCase("MyHTTPServer").words == ["My", "HTTP", "Server"]


def test_camel_case_invalid_start():
    with pytest.raises(ValueError):
        CamelCase("1testCase")  # must start with lowercase letter


# -----------------
# FlatCase behavior
# -----------------
def test_flat_case_normalization():
    assert str(FlatCase("fooBar")) == "foobar"
    assert str(FlatCase("FOO-BAR")) == "foobar"


# -----------------
# HttpHeaderCase strictness
# -----------------
def test_http_header_case_strict():
    assert str(HttpHeaderCase("Content-Type")) == "Content-Type"
    with pytest.raises(ValueError):
        HttpHeaderCase("Content--Type")  # double hyphen invalid
    with pytest.raises(ValueError):
        HttpHeaderCase("Content@Type")  # invalid char


# -----------------
# MacroCase normalization
# -----------------
def test_macro_case_normalization():
    assert str(MacroCase("foo_bar")) == "FOO_BAR"
    assert str(MacroCase("FOO_BAR")) == "FOO_BAR"


# -----------------
# SlashTitleCase strictness
# -----------------
def test_slash_title_case_strict():
    with pytest.raises(ValueError):
        SlashTitleCase("/leading")  # cannot start with slash
    with pytest.raises(ValueError):
        SlashTitleCase("trailing/")  # cannot end with slash
    with pytest.raises(ValueError):
        SlashTitleCase("double//slash")  # double slash invalid


# -----------------
# SentenceCase & TitleCase with punctuation
# -----------------
def test_title_case_with_punctuation():
    assert str(TitleCase("hello, world")) == "Hello, World"


def test_sentence_case_with_punctuation():
    assert str(SentenceCase("hello, world")) == "Hello, world"


# -----------------
# SpaceCase empty / whitespace
# -----------------
def test_space_case_whitespace_only():
    sc = SpaceCase("   ")
    assert sc.words == []
    assert str(sc) == ""


# -----------------
# Number handling inside words
# -----------------
def test_numbers_inside_words():
    assert SnakeCase("foo123_bar456").words == ["foo123", "bar456"]
