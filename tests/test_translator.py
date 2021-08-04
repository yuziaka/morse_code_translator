import pytest
from morse_code_translator.enums import Errors
from morse_code_translator.translator import translate_to_lat, translate_to_morse


@pytest.mark.parametrize(
    "input, output, errors",
    (
        (
            "Morse Code Translator!!",
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-.",
            Errors.IGNORE,
        ),
        (
            "MORSE CODE TRANSLATOR!!",
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-.",
            Errors.IGNORE,
        ),
        (
            "Morse Code Translator!!",
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-. ? ?",
            Errors.REPLACE,
        ),
        (
            "MORSE CODE TRANSLATOR!!",
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-. ? ?",
            Errors.REPLACE,
        ),
        (
            "Morse Code Translator",
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-.",
            Errors.STRICT,
        ),
        (
            "MORSE CODE TRANSLATOR",
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-.",
            Errors.STRICT,
        ),
    ),
)
def test_success_translate_to_morse(input, output, errors):
    assert translate_to_morse(input, errors=errors) == output


def test_fail_translate_to_morse():
    with pytest.raises(ValueError):
        translate_to_morse("Morse Code Translator!!", errors=Errors.STRICT)


@pytest.mark.parametrize(
    "input, output, errors",
    (
        (
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-. ..... -----",
            "morse code translator",
            Errors.IGNORE,
        ),
        (
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-. ..... -----",
            "morse code translator??",
            Errors.REPLACE,
        ),
        (
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-.",
            "morse code translator",
            Errors.STRICT,
        ),
    ),
)
def test_success_translate_to_lat(input, output, errors):
    assert translate_to_lat(input, errors=errors) == output


def test_fail_translate_to_lat():
    with pytest.raises(ValueError):
        translate_to_lat(
            "-- --- .-. ... .  -.-. --- -.. .  - .-. .- -. ... .-.. .- - --- .-. ..... -----",
            errors=Errors.STRICT,
        )
