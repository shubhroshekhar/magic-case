import re

from .base import BaseCase


class CamelCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """
        Splits a CamelCase or PascalCase string into its component words.

        Examples:
        - "camelCase" -> ["camel", "Case"]
        - "PascalCase" -> ["Pascal", "Case"]
        - "HTTPResponse" -> ["HTTP", "Response"]
        """
        # This regex handles:
        # 1. Lowercase followed by uppercase: camelCase -> camel Case
        # 2. Uppercase followed by uppercase + lowercase: HTTPResponse -> HTTP Response

        pattern = r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])"
        return re.split(pattern, text)

    def __str__(self) -> str:
        first, *rest = self.words
        return first + "".join(w.capitalize() for w in rest)
