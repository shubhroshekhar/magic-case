import re

from .base import BaseCase


class HttpHeaderCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """
        Splits a string into words suitable for HTTP header capitalization.
        Handles camelCase, PascalCase, snake_case, and acronyms.
        """
        # Must strictly match HttpHeaderCase: "Word-Word-Word"
        if not re.fullmatch(r"(?:[A-Z][a-z0-9]*)(?:-[A-Z][a-z0-9]*)*", text):
            raise ValueError(f"Invalid HttpHeaderCase string: {text}")

        # Split by hyphen and lowercase for internal representation
        words = text.split("-")
        return [word.lower() for word in words]

    def __str__(self) -> str:
        """
        Converts the words to HTTP Header Case:
        Capitalize first letter of each word, separated by hyphens.
        """
        return "-".join(w.capitalize() for w in self.words)
