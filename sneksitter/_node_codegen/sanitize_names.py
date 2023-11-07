import keyword
import re
import unicodedata
from typing import List, Set

SPECIAL_CHARS = {
    ">": "Gt",
    "<": "Lt",
    "=": "Eq",
    "+": "Plus",
    "-": "Dash",
    "*": "Star",
    "/": "Slash",
    "!": "Bang",
    "@": "At",
    "#": "Hash",
    "$": "Dollar",
    "%": "Percent",
    "^": "Caret",
    "&": "And",
    "(": "LParen",
    ")": "RParen",
    "[": "LBracket",
    "]": "RBracket",
    "{": "LBrace",
    "}": "RBrace",
    "|": "Pipe",
    ";": "Semicolon",
    ":": "Colon",
    ",": "Comma",
    ".": "Dot",
    "?": "Question",
    " ": "Space",
    # "_": "Underscore",
    "~": "Tilde",
    "`": "Backtick",
    "'": "SingleQuote",
    '"': "DoubleQuote",
    "\\": "Backslash",
    "\n": "Newline",
    "\t": "Tab",
    "\r": "CarriageReturn",
    "\f": "FormFeed",
    "\v": "VerticalTab",
    "\0": "Null",
}


def tokenize(chars: str) -> List[str]:
    # Split string based on:
    #  - Contiguous ASCII characters that are all alphanumeric are a token
    #  - Non-ASCII characters are a single token
    #  - PascalCase/camelCase tokens are split into multiple tokens
    # Examples:
    # "hello world" -> ["hello", " ", "world"]
    # "hello_world" -> ["hello", "_", "world"]
    # ">=" -> [">", "="]
    # ">>=" -> [">", ">=", "="]
    # "one~twoçThree" -> ["one", "~", "two", "ç", "Three"]
    # "camelCase" -> ["camel", "Case"]

    re_word = re.compile(r"[a-zA-Z0-9]+|[^a-zA-Z0-9\s]+")
    re_camel = re.compile(r"[a-z]+|[A-Z][^A-Z]*")

    tokens = []
    i = 0
    while i < len(chars):
        if chars[i].isascii() and chars[i].isalnum():
            # Alphanumeric ASCII character
            match = re_word.match(chars, i)
            if match is None:
                raise RuntimeError("This should never happen")

            # If we have a camelCase token, split it
            camel_match = re_camel.findall(match.group(0))
            if camel_match:
                tokens.extend(camel_match)
            else:
                tokens.append(match.group(0))

            i = match.end()
        elif chars[i].isascii():
            # Non-alphanumeric ASCII character
            tokens.append(chars[i])
            i += 1
        else:
            # Non-ASCII character
            tokens.append(chars[i])
            i += 1

    return tokens


def unicode_transform(token: str) -> List[str]:
    token_name = unicodedata.name(token)
    token_name = token_name.removesuffix(" SIGN")
    token_name = token_name.removesuffix(" MARK")
    token_name = token_name.removesuffix(" LETTER")
    token_name = token_name.removesuffix(" SYMBOL")
    token_name = token_name.replace(" ", "_")
    token_name = token_name.replace("-", "_")
    tokens = token_name.lower().split("_")
    return tokens


def join_tokens(tokens: List[str], for_class: bool) -> str:
    if for_class:
        return "".join([t.capitalize() for t in tokens])
    else:
        return "_".join([t.lower() for t in tokens])


# Main function
def sanitize_identifier(
    input_str: str,
    for_class: bool = True,
    additional_reserved_names: Set[str] | None = None,
) -> str:
    if not input_str:
        return "Empty" if for_class else "empty"
    if all(ch == " " for ch in input_str):
        return "Space" * len(input_str) if for_class else "_".join("space" for _ in input_str)
    if all(ch == "\n" for ch in input_str):
        return "Newline" * len(input_str) if for_class else "_".join("newline" for _ in input_str)
    if all(ch == "_" for ch in input_str):
        return (
            "Underscore" * len(input_str)
            if for_class
            else "_".join("underscore" for _ in input_str)
        )

    tokens = tokenize(input_str)
    transformed_tokens = []
    for token in tokens:
        if token in {" ", "_"}:
            continue
        if token in SPECIAL_CHARS:
            transformed_tokens.append(SPECIAL_CHARS[token])
        elif not token.isascii():
            transformed_tokens.extend(unicode_transform(token))
        else:
            transformed_tokens.append(token)

    result = join_tokens(transformed_tokens, for_class)

    forbidden_names = set(keyword.kwlist) | (additional_reserved_names or set())

    if result[0].isdigit():
        result = "_" + result

    while result in forbidden_names:
        result += "_"

    return result


if __name__ == "__main__":
    # Testing
    test_cases = [
        ("", True),  # empty string, class
        ("", False),  # empty string, variable
        (" ", True),  # single space, class
        (" ", False),  # single space, variable
        ("some text", True),  # normal text, class
        ("some text", False),  # normal text, variable
        (">= ", True),  # special characters, class
        (">= ", False),  # special characters, variable
        ("import", True),  # Python keyword, class
        ("import", False),  # Python keyword, variable
        ("123abc", True),  # Starts with a number, class
        ("123abc", False),  # Starts with a number, variable
        ("uniçode", True),  # Unicode characters, class
        ("uniçode", False),  # Unicode characters, variable
        ("€", True),  # Euro Sign, class
        ("€", False),  # Euro Sign, variable
        ("αβγ", True),  # Greek letters, class
        ("αβγ", False),  # Greek letters, variable
    ]

    test_results = [(case, sanitize_identifier(*case)) for case in test_cases]
    for res in test_results:
        print(res)
