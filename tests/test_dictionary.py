import random

from morse_code_translator.dictionary import lat_to_morse, morse_dictionary, morse_to_lat


def test_dictionary_len():
    assert len(morse_dictionary) == len(lat_to_morse) == len(morse_to_lat)


def test_dictionary_map():
    random_element = random.choice(morse_dictionary)
    assert lat_to_morse[random_element[0]] == random_element[1]
    assert morse_to_lat[random_element[1]] == random_element[0]
