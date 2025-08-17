from .base import BaseCase


class DotCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """
        Splits a dot-separated string into its component words.

        Examples:
        - "dot.case" -> ["dot", "case"]
        - "example.test" -> ["example", "test"]
        """
        # Split on dot
        # This handles cases like "dot.case" -> ["dot", "case"]
        # and "example.test" -> ["example", "test"]
        return text.lower().split(".")

    def __str__(self) -> str:
        return ".".join(self.words).lower()
