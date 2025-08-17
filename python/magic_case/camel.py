import re

from .base import BaseCase


class CamelCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """
        Splits a CamelCase string into its component words.

        Rules:
        - Must start with a lowercase letter.
        - Split before uppercase letters.
        """
        if not text:
            raise ValueError("Input cannot be empty")

        if not text[0].islower():
            raise ValueError(
                f"Invalid CamelCase: must start with a lowercase letter → {text}"
            )

        # Split rules:
        # - lowercase → uppercase boundary: testCase → test Case
        # - acronym before normal word: HTTPServer → HTTP Server
        pattern = r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])"
        return re.split(pattern, text)

    def __str__(self) -> str:
        first, *rest = self.words
        return first.lower() + "".join(w.capitalize() for w in rest)
