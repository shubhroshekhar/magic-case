from .base import BaseCase


class UpperCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        return text.lower().split("_")

    def __str__(self) -> str:
        return "_".join(self.words).upper()
