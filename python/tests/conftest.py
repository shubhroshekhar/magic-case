"""
Shared fixtures and utilities for magic-case tests.

This file provides common test fixtures and utilities that can be used
across all test modules.
"""

import pytest

from magic_case import (
    BaseCase,
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


@pytest.fixture(scope="session")
def all_case_classes() -> list[type[BaseCase]]:
    """All available case classes for testing."""
    return [
        SnakeCase,
        KebabCase,
        CamelCase,
        PascalCase,
        UpperCase,
        SentenceCase,
        TitleCase,
        DotCase,
        SpaceCase,
        FlatCase,
        HttpHeaderCase,
        CamelSnakeCase,
        MacroCase,
        PascalSnakeCase,
        PathCase,
        SlashTitleCase,
        HungarianCase,
    ]


@pytest.fixture(scope="session")
def sample_texts() -> dict[str, str]:
    """Common test texts for various case conversions."""
    return {
        "simple": "hello_world",
        "multi_word": "hello_world_again",
        "with_numbers": "hello123_world456",
        "acronyms": "myHTTPServer",
        "single_word": "hello",
        "empty": "",
        "whitespace": "   hello   world   ",
        "punctuation": "hello, world!",
        "path_like": "foo/bar/baz",
        "http_header": "Content-Type",
        "hungarian": "strHelloWorld",
        "complex": "user_profile_settings_2024",
        "mixed_case": "Hello_World-again.test",
        "with_underscores": "test_case_string",
        "api_endpoint": "user_authentication_service",
        "db_column": "last_modified_timestamp",
        "file_path": "src/components/user_profile",
    }


@pytest.fixture(scope="session")
def case_conversion_examples() -> list[tuple]:
    """Examples of case conversions for comprehensive testing."""
    return [
        # (input_text, snake_case, kebab_case, camel_case, pascal_case, title_case)
        (
            "hello_world",
            "hello_world",
            "hello-world",
            "helloWorld",
            "HelloWorld",
            "Hello World",
        ),
        (
            "user_profile",
            "user_profile",
            "user-profile",
            "userProfile",
            "UserProfile",
            "User Profile",
        ),
        (
            "api_endpoint",
            "api_endpoint",
            "api-endpoint",
            "apiEndpoint",
            "ApiEndpoint",
            "Api Endpoint",
        ),
        (
            "database_column",
            "database_column",
            "database-column",
            "databaseColumn",
            "DatabaseColumn",
            "Database Column",
        ),
        (
            "file_path_name",
            "file_path_name",
            "file-path-name",
            "filePathName",
            "FilePathName",
            "File Path Name",
        ),
    ]


@pytest.fixture(scope="session")
def edge_case_texts() -> dict[str, str]:
    """Texts that test edge cases and boundary conditions."""
    return {
        "empty": "",
        "single_char": "a",
        "single_word": "hello",
        "whitespace_only": "   ",
        "leading_whitespace": "  hello",
        "trailing_whitespace": "hello  ",
        "mixed_whitespace": "  hello   world  ",
        "numbers_only": "123",
        "mixed_numbers": "hello123world",
        "special_chars": "hello@world#test",
        "unicode": "café_naïve",
        "very_long": "_".join([f"word{i}" for i in range(100)]),
    }


@pytest.fixture(scope="session")
def invalid_inputs() -> list:
    """Invalid inputs that should raise exceptions."""
    return [
        123,
        None,
        [],
        {},
        True,
        False,
        3.14,
        b"bytes",
    ]


@pytest.fixture(scope="session")
def performance_test_data() -> dict[str, str]:
    """Data for performance and stress testing."""
    return {
        "small": "hello_world",
        "medium": "_".join([f"word{i}" for i in range(100)]),
        "large": "_".join([f"word{i}" for i in range(1000)]),
        "very_large": "_".join([f"word{i}" for i in range(10000)]),
    }


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "performance: marks tests as performance tests")
    config.addinivalue_line("markers", "edge_case: marks tests as edge case tests")
    config.addinivalue_line(
        "markers", "error_handling: marks tests as error handling tests"
    )


def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their names and classes."""
    for item in items:
        # Mark performance tests
        if "performance" in item.name.lower() or "Performance" in item.cls.__name__:
            item.add_marker(pytest.mark.performance)

        # Mark integration tests
        if "integration" in item.name.lower() or "Integration" in item.cls.__name__:
            item.add_marker(pytest.mark.integration)

        # Mark edge case tests
        if "edge" in item.name.lower() or "Edge" in item.cls.__name__:
            item.add_marker(pytest.mark.edge_case)

        # Mark error handling tests
        if "error" in item.name.lower() or "Error" in item.cls.__name__:
            item.add_marker(pytest.mark.error_handling)
