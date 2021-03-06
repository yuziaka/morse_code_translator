morse_dictionary = (
    ("a", ".-"),
    ("b", "-..."),
    ("c", "-.-."),
    ("d", "-.."),
    ("e", "."),
    ("f", "..-."),
    ("g", "--."),
    ("h", "...."),
    ("i", ".."),
    ("j", ".---"),
    ("k", "-.-"),
    ("l", ".-.."),
    ("m", "--"),
    ("n", "-."),
    ("o", "---"),
    ("p", ".--."),
    ("q", "--.-"),
    ("r", ".-."),
    ("s", "..."),
    ("t", "-"),
    ("u", "..-"),
    ("v", "...-"),
    ("w", ".--"),
    ("x", "-..-"),
    ("y", "-.--"),
    ("z", "--.."),
)

lat_to_morse = {lat: morse for lat, morse in morse_dictionary}
morse_to_lat = {morse: lat for lat, morse in morse_dictionary}
