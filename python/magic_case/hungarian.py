import re
from typing import Optional

from .base import BaseCase

HUNGARIAN_PREFIXES = ["str", "lst", "arr", "psz", "i", "b", "d", "f", "ch", "n", "p"]


class HungarianCase(BaseCase):
    prefix: Optional[str] = None

    def _split_into_words(self, text: str) -> list[str]:
        """
        Split a Hungarian Notation variable into words.
        Example: 'strUserName' -> ['user', 'name']
                'iCount' -> ['count']
                'lstScores' -> ['scores']
                'bIsAdmin' -> ['is', 'admin']
        """
        # Detect Hungarian prefix
        self.prefix = None
        for p in sorted(HUNGARIAN_PREFIXES, key=len, reverse=True):
            if text.startswith(p):
                self.prefix = p
                text = text[len(p) :]  # remove prefix
                break

        # Now split CamelCase / PascalCase
        words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text).split()

        # Normalize to lowercase
        return [w.lower() for w in words]

    def __str__(self) -> str:
        # Hungarian notation: strName, intCount, boolFlag
        if not self.words:
            return ""

        # If we have a prefix, append it and capitalize it words
        if self.prefix:
            return self.prefix + "".join(word.capitalize() for word in self.words)

        # else dont capitalize the first word
        [first, *rest] = self.words
        return first + "".join(word.capitalize() for word in rest)
