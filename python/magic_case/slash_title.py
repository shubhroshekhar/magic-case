from .base import BaseCase


class SlashTitleCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        import re

        # Split on common separators: underscore, hyphen, dot, slash, backslash, space
        words = re.split(r"[_\-\.,\/\\\s]+", text)
        return [word.lower() for word in words if word.strip()]

    def __str__(self) -> str:
        # Slash title case: Hello/World (same as Path case)
        return "/".join(word.capitalize() for word in self.words)
