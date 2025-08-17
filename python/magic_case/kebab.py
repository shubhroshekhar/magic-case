from .base import BaseCase


class KebabCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        """Splits a kebab-case string into its constituent words.

        Args:
            text (str): The kebab-case string to split.

        Returns:
            list[str]: A list of words in lowercase.

        Examples:
            - "kebab-case" -> ["kebab", "case"]
            - "example-text" -> ["example", "text"]
        """
        return text.lower().split("-")

    def __str__(self) -> str:
        return "-".join(self.words).lower()
