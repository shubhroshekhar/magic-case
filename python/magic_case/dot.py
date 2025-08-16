from .base import BaseCase


class DotCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        return text.lower().split(".")

    def __str__(self) -> str:
        return ".".join(self.words)
