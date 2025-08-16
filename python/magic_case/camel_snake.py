import re

from .base import BaseCase


class CamelSnakeCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        # Split on underscores or camel humps
        words = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])", text.replace("_", " "))
        return [word.lower() for word in words if word]

    def __str__(self) -> str:
        if not self.words:
            return ""
        first = self.words[0].lower()
        rest = [w.capitalize() for w in self.words[1:]]
        return "_".join([first] + rest)
