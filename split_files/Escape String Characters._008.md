---
file: /home/pedro/Documents/chatgpt_export/Markdown/Escape String Characters..md
heading_stack: <root> -> f6e43f13-693f-4752-b96a-a9707c6283b5 -> System -> 1f665d95-6647-451e-aeff-9380ccf0cf4f -> System -> aaa2d32f-9183-440c-94c2-108509937911 -> User -> 9b6cd32d-f3d2-427f-a245-c7fc99148973 -> Assistant
---
# Assistant

To escape a string according to the given specification, we need to replace each character that falls outside the allowed range with its corresponding escape sequence. The escape sequence for any Unicode character in Python can be generated using the format `"\u{hex_code}"`, where `hex_code` is the hexadecimal Unicode code point of the character.

Here's a Python function that accomplishes this:

```python
def escape_string(input_str: str) -> str:
    allowed_chars = set("\t\n\r" + "".join(chr(i) for i in range(0x20, 0x7F)) + "".join(chr(i) for i in range(0xA0, 0xD800)) + "".join(chr(i) for i in range(0xE000, 0xFFFE)))
    
    escaped_str = []
    for char in input_str:
        if char in allowed_chars:
            escaped_str.append(char)
        else:
            escaped_str.append(f"\\u{ord(char):04x}")
    
    return ''.join(escaped_str)
```

This function constructs a set of allowed characters and then iterates through each character in the input string. If the character is allowed, it is appended to the result as-is. Otherwise, its Unicode code point is converted to a hexadecimal string, and the escape sequence is appended to the result.

Let's test the function.

[child ⬇️](#e0638936-0b0b-4f0b-b564-1dd301c945fe)

---

(main branch ⎇)
###### e0638936-0b0b-4f0b-b564-1dd301c945fe
[parent ⬆️](#9b6cd32d-f3d2-427f-a245-c7fc99148973)
