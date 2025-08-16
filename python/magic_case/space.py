from .base import BaseCase


class SpaceCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """
        Splits a space-separated string into its component words.

        Examples:
        - "hello world" -> ["hello", "world"]
        - "this is a test" -> ["this", "is", "a", "test"]
        - "  leading and trailing spaces  " -> ["leading", "and", "trailing", "spaces"]
        """
        # Split by spaces and filter out empty strings
        words = text.split(" ")
        return [word.lower() for word in words if word.strip()]

    def __str__(self) -> str:
        return " ".join(self.words)
