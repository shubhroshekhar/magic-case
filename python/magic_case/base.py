from __future__ import annotations

from abc import ABC, abstractmethod


class BaseCase(ABC):
    """Abstract base for all case transformers.

    Holds a normalized list of lowercase words and renders them according to
    the specific case in subclasses.
    """

    words: list[str]

    def __init__(self, text_or_obj: str | BaseCase):
        if isinstance(text_or_obj, BaseCase):
            words = text_or_obj.words
        elif isinstance(text_or_obj, str):
            words = self._split_into_words(text_or_obj)
        else:
            raise TypeError("BaseCase expects a string or another BaseCase instance")

        if not all(isinstance(word, str) for word in words):
            raise ValueError("All words must be strings")

        self.words = [word.lower() for word in words]

    @abstractmethod
    def _split_into_words(self, text: str) -> list[str]:
        """Split the input text into lowercase words."""
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """Return the text formatted in the case style."""
        raise NotImplementedError

    def get(self) -> str:
        return str(self)
