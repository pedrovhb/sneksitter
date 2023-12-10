---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (14).md
heading_stack: <root> -> b421fd60-2b52-4eee-9122-5a7806574998 -> System -> 0e0de881-5a7b-4301-9643-ccff084a4ddf -> System -> aaa24362-c889-42c5-afec-aae36a2536d8 -> User -> 5e125b51-4948-41c1-bdf3-93b510bdb1af -> Assistant -> Ideal API Design -> Helper Classes -> Class -> Decorator -> AnnotatedAttribute -> BaseClass -> CodeBlock -> Recursive Code Generation -> Handling Indentation -> Example Implementation -> aaa2b636-9271-4157-9924-1a308fab5317 -> User -> 3c3b81e1-8cd2-4341-91c2-7b030a68f9a1 -> Assistant -> Leveraging Dataclasses
---
### Leveraging Dataclasses

Using dataclasses can indeed reduce boilerplate and make the code more maintainable. Here's how the classes might look with dataclasses:

```python
from dataclasses import dataclass, field
from typing import List, Union, Any

@dataclass
class CodeBlock:
    indent: int = 0
    lines: List[str] = field(default_factory=list)

    def add_line(self, line: str):
        self.lines.append(" " * self.indent + line)

    def generate_code(self) -> str:
        return "\n".join(self.lines)

@dataclass
class Decorator:
    name: str
    args: List[Any] = field(default_factory=list)
    kwargs: dict
```

---

(main branch ⎇)
###### aaa2a536-29ee-411d-9f01-afe2796f7425
[parent ⬆️](#5e125b51-4948-41c1-bdf3-93b510bdb1af)
