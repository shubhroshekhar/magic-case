import re

from .base import BaseCase


class PascalCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        return re.sub(r"([a-z])([A-Z])", r"\1 \2", text).lower().split()

    def __str__(self) -> str:
        return "".join(w.capitalize() for w in self.words)
