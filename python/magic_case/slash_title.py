from .base import BaseCase


class SlashTitleCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        if not text:
            raise ValueError("Input cannot be empty")

        if text.startswith("/") or text.endswith("/"):
            raise ValueError(
                f"Invalid SlashTitleCase: cannot start or end with slash → {text}"
            )

        words = text.split("/")

        # Check for consecutive slashes → empty segments
        if any(not word.strip() for word in words):
            raise ValueError(
                f"Invalid SlashTitleCase: consecutive slashes not allowed → {text}"
            )

        return words

    def __str__(self) -> str:
        # TitleCase each part and join with slash
        return "/".join(word.capitalize() for word in self.words)
