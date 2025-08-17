import re

from .base import BaseCase


class PascalCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        if not text:
            raise ValueError("Input cannot be empty")

        if not text[0].isupper():
            raise ValueError(
                f"Invalid PascalCase: must start with an uppercase letter → {text}"
            )

        # Regex handles:
        # - lowercase→uppercase: MyClass → My Class
        # - acronym→word: HTTPServer → HTTP Server
        pattern = r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])"
        return re.split(pattern, text)

    def __str__(self) -> str:
        return "".join(w.capitalize() for w in self.words)
