from typing import Dict

from morse_code_translator.dictionary import lat_to_morse, morse_to_lat
from morse_code_translator.enums import Errors

__all__ = ("translate_to_morse", "translate_to_lat")


def _translate_char(char: str, dictionary: Dict, errors: Errors = Errors.STRICT) -> str:
    char = char.lower()

    try:
        return dictionary[char]
    except KeyError:
        if errors == Errors.STRICT:
            raise ValueError

        if errors == Errors.REPLACE:
            return "?"

        # Errors.IGNORE
        return ""


def _translate_char_to_morse(char: str, errors: Errors = Errors.STRICT):
    return _translate_char(char=char, dictionary=lat_to_morse, errors=errors)


def _translate_char_to_lat(char: str, errors: Errors = Errors.STRICT):
    return _translate_char(char=char, dictionary=morse_to_lat, errors=errors)


def translate_to_morse(text: str, errors: Errors = Errors.STRICT):
    """Translating Latin letters into Morse code."""

    return " ".join(
        _translate_char_to_morse(char=char, errors=errors) if char != " " else ""
        for char in text
        if char
    ).strip(" ")


def translate_to_lat(text: str, errors: Errors = Errors.STRICT):
    """Translating Morse code into Latin letters."""

    result = "".join(
        _translate_char_to_lat(char=char, errors=errors) if char != "" else " "
        for char in text.split(" ")
    )

    return result.replace("  ", " ")
