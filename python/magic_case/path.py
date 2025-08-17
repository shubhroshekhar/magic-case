import re

from .base import BaseCase


class PathCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        # Must strictly match: lowercase words separated by `/`
        if not re.fullmatch(r"(?:[a-z0-9]+)(?:/[a-z0-9]+)*", text):
            raise ValueError(f"Invalid PathCase string: {text}")

        return text.split("/")

    def __str__(self) -> str:
        # Join normalized words with slash
        return "/".join(self.words)
