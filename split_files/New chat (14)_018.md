---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (14).md
heading_stack: <root> -> b421fd60-2b52-4eee-9122-5a7806574998 -> System -> 0e0de881-5a7b-4301-9643-ccff084a4ddf -> System -> aaa24362-c889-42c5-afec-aae36a2536d8 -> User -> 5e125b51-4948-41c1-bdf3-93b510bdb1af -> Assistant -> Ideal API Design -> Helper Classes -> Class -> Decorator -> AnnotatedAttribute -> BaseClass -> CodeBlock -> Recursive Code Generation -> Handling Indentation -> Example Implementation
---
### Example Implementation

Here's a skeleton code example to illustrate some of these ideas:

```python
from typing import List, Union

class CodeBlock:
    def __init__(self, indent=0):
        self.indent = indent
        self.lines = []

    def add_line(self, line):
        self.lines.append(" " * self.indent + line)

    def generate_code(self):
        return "\n".join(self.lines)

class Decorator:
    def __init__(self, name, args=None, kwargs=None):
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def generate_code(self, code_block):
        # Generate decorator code here
        pass

class AnnotatedAttribute:
    def __init__(self, name, type, default=None):
        self.name = name
        self.type = type
        self.default =
```

[child 1 ⬇️](#aaa2b636-9271-4157-9924-1a308fab5317) | [child 2 ⬇️](#aaa2a536-29ee-411d-9f01-afe2796f7425)

---

(other branch ⎇)
###### aaa2b636-9271-4157-9924-1a308fab5317
[parent ⬆️](#5e125b51-4948-41c1-bdf3-93b510bdb1af)
