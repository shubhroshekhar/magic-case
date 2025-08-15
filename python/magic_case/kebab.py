from typing import List
from .base import BaseCase


class KebabCase(BaseCase):
    def _split_into_words(self, text: str) -> List[str]:
        return text.lower().split("-")

    def __str__(self) -> str:
        return "-".join(self.words) 