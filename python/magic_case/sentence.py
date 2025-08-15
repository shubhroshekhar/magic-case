from typing import List
from .base import BaseCase


class SentenceCase(BaseCase):
    def _split_into_words(self, text: str) -> List[str]:
        return text.lower().split(" ")

    def __str__(self) -> str:
        sentence = " ".join(self.words)
        return sentence.capitalize() 