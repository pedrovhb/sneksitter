---
file: /home/pedro/Documents/chatgpt_export/Markdown/Escape String Characters..md
heading_stack: <root> -> f6e43f13-693f-4752-b96a-a9707c6283b5 -> System -> 1f665d95-6647-451e-aeff-9380ccf0cf4f -> System -> aaa2d32f-9183-440c-94c2-108509937911 -> User -> 9b6cd32d-f3d2-427f-a245-c7fc99148973 -> Assistant -> e0638936-0b0b-4f0b-b564-1dd301c945fe -> Assistant
---
# Assistant

```python
def escape_string(input_str: str) -> str:
    allowed_chars = set(
        "\t\n\r" +
        "".join(chr(i) for i in range(0x20, 0x7F)) +
        "".join(chr(i) for i in range(0xA0, 0xD800)) +
        "".join(chr(i) for i in range(0xE000, 0xFFFE))
    )
    
    escaped_str = []
    for char in input_str:
        if char in allowed_chars:
            escaped_str.append(char)
        else:
            escaped_str.append(f"\\u{ord(char):04x}")
    
    return ''.join(escaped_str)

# Test cases
test_strings = [
    "Hello, world!",
    "This is a tab:\tDone.",
    "\u00E9",  # Latin small letter e with acute
    "\u007F",  # DEL
    "\uFFFE"   # Not allowed
]

escaped_strings = [escape_string(s) for s in test_strings]
escaped_strings
```

[child ⬇️](#394b99c7-5b5b-42d3-9bb3-32187e22af1a)

---

(main branch ⎇)
###### 394b99c7-5b5b-42d3-9bb3-32187e22af1a
[parent ⬆️](#e0638936-0b0b-4f0b-b564-1dd301c945fe)
