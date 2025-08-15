from .base import BaseCase


class HungarianCase(BaseCase):
    def _split_into_words(self, text: str) -> list[str]:
        import re

        # Split on common separators: underscore, hyphen, dot, slash, backslash, space
        words = re.split(r"[_\-\.,\/\\\s]+", text)
        return [word.lower() for word in words if word.strip()]

    def __str__(self) -> str:
        # Hungarian notation: strName, intCount, boolFlag
        if not self.words:
            return ""

        # Simple type inference based on word content
        first_word = self.words[0]
        if first_word in ["string", "str", "text", "name", "title", "message"]:
            prefix = "str"
        elif first_word in ["number", "num", "count", "index", "id", "size", "length"]:
            prefix = "int"
        elif first_word in ["boolean", "bool", "flag", "is", "has", "can", "should"]:
            prefix = "bool"
        elif first_word in ["array", "list", "collection", "items"]:
            prefix = "arr"
        elif first_word in ["object", "obj", "data", "item"]:
            prefix = "obj"
        else:
            prefix = "var"

        # Capitalize first letter of the name part
        name_part = "".join(word.capitalize() for word in self.words)
        return prefix + name_part
