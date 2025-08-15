from abc import ABC, abstractmethod
from typing import List, Union
from pydantic import BaseModel, Field, validator


class BaseCase(BaseModel, ABC):
    words: List[str] = Field(..., description="List of lowercase words forming the text")

    class Config:
        arbitrary_types_allowed = True  # Allow BaseCase types in constructors

    def __init__(self, text_or_obj: Union[str, "BaseCase"], **data):
        if isinstance(text_or_obj, BaseCase):
            words = text_or_obj.words
        else:
            words = self._split_into_words(text_or_obj)
        super().__init__(words=words, **data)

    @abstractmethod
    def _split_into_words(self, text: str) -> List[str]:
        """Split the input text into lowercase words."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return the text formatted in the case style."""
        pass

    def get(self) -> str:
        return str(self)

    @validator("words", pre=True)
    def _validate_words(cls, v):
        if not all(isinstance(word, str) for word in v):
            raise ValueError("All words must be strings")
        return [word.lower() for word in v]
