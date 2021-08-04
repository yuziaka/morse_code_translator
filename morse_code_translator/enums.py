from enum import Enum


class Errors(Enum):
    """Response when encoding fails.

    strict - default response which raises a UnicodeDecodeError exception on failure
    ignore - ignores the unencodable unicode from the result
    replace - replaces the unencodable unicode to a question mark `?`
    """

    IGNORE = "ignore"
    REPLACE = "replace"
    STRICT = "strict"
