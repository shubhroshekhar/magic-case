import re

from .base import BaseCase


class CamelCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        return re.sub(r"([a-z])([A-Z])", r"\1 \2", text).lower().split()

    def __str__(self) -> str:
        first, *rest = self.words
        return first + "".join(w.capitalize() for w in rest)
