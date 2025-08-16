from .base import BaseCase


class PascalSnakeCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        import re

        # Split on common separators: underscore, hyphen, dot, slash, backslash, space
        words = re.split(r"[_\-\.,\/\\\s]+", text)
        return [word.lower() for word in words if word.strip()]

    def __str__(self) -> str:
        # Pascal case with underscores: Hello_World
        return "_".join(word.capitalize() for word in self.words)
