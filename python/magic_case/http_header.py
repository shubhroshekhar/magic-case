import re

from .base import BaseCase


class HttpHeaderCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """
        Splits a string into words suitable for HTTP header capitalization.
        Handles camelCase, PascalCase, snake_case, and acronyms.
        """
        # Replace underscores with spaces first (for snake_case)
        text = text.replace("_", " ")

        # Split camelCase / PascalCase / acronyms
        pattern = r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])"
        words = re.split(pattern, text)

        # Split on spaces to handle snake_case or existing spaces
        final_words = []
        for w in words:
            final_words.extend(w.split())

        return final_words

    def __str__(self) -> str:
        """
        Converts the words to HTTP Header Case:
        Capitalize first letter of each word, separated by hyphens.
        """
        return "-".join(w.capitalize() for w in self.words)
