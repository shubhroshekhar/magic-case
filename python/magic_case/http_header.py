import re

from .base import BaseCase


class HttpHeaderCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """
        Splits a string into words suitable for HTTP header capitalization.
        Must strictly match Http-Header-Case format.
        """
        if not text:
            raise ValueError("Input cannot be empty")

        # Must strictly match: Word-Word-Word (each Word starts uppercase, then lowercase/digits)
        if not re.fullmatch(r"(?:[A-Z][a-z0-9]*)(?:-[A-Z][a-z0-9]*)*", text):
            raise ValueError(f"Invalid HttpHeaderCase string: {text}")

        # Split by hyphen and normalize internally
        return text.split("-")

    def __str__(self) -> str:
        """
        Converts words back to HTTP Header Case (Title-Cased).
        Example: content-type -> Content-Type
        """
        return "-".join(w.capitalize() for w in self.words)
