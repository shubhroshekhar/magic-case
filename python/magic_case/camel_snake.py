from .base import BaseCase


class CamelSnakeCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        import re

        # Split on common separators: underscore, hyphen, dot, slash, backslash, space
        words = re.split(r"[_\-\.,\/\\\s]+", text)
        return [word.lower() for word in words if word.strip()]

    def __str__(self) -> str:
        # Camel case with underscores: Hello_World
        if not self.words:
            return ""
        result = self.words[0].capitalize()
        for word in self.words[1:]:
            result += "_" + word.capitalize()
        return result
