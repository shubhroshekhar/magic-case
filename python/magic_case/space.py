from .base import BaseCase


class SpaceCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        # Handle various separators and convert to space-separated
        import re

        # Split on common separators: underscore, hyphen, dot, slash, backslash
        words = re.split(r"[_\-\.,\/\\]+", text)
        return [word.lower() for word in words if word.strip()]

    def __str__(self) -> str:
        return " ".join(self.words)
