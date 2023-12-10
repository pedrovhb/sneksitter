---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant
---
# Assistant

To accomplish the task of recursively parsing and unparsing Python Google-style docstrings, we'll start by defining the necessary data classes for various sections of a Google-style docstring. These data classes will be:

1. `Docstring`: The root object that represents the entire docstring.
2. `Description`: Handles the short and long description.
3. `Parameter`: Handles individual parameters.
4. `Returns`: Handles the return value description.
5. `Raises`: Handles exceptions that the function can raise.
6. `Example`: Handles examples.
7. `OtherSections`: Handles any other section not explicitly defined here.

Each data class will have two methods:

- `from_str(cls, text: str) -> T`: A class method to parse from a string.
- `to_str(self) -> str`: An instance method to unparse back to a docstring.

Finally, we'll use the `parse` library to define the parsing format and Python's string `Template` class for unparsing.

Let's get started.

[child ⬇️](#7a848fb4-fafb-4120-84f6-6725ea253bc6)

---

(other branch ⎇)
###### 7a848fb4-fafb-4120-84f6-6725ea253bc6
[parent ⬆️](#7d012bc2-71e8-4e41-929e-ddebce0ccb7f)
