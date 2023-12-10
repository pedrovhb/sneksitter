---
file: /home/pedro/Documents/chatgpt_export/Markdown/Refactored Python `gen_class` Function.md
heading_stack: <root> -> 479c6063-4851-4e28-b58d-1485da871bb9 -> System -> e2715e40-56c8-4c79-9c73-82243a61a7a8 -> System -> aaa2565e-9a67-4751-adfd-dcd1e2555de6 -> User -> 8e8a47c4-949f-4209-b8cf-827490f09d7b -> Assistant -> aaa2aeb3-345c-4930-b543-3c60fd3fc1b7 -> User -> cca9954d-8802-442a-b3d1-267c0d293e08 -> Assistant
---
# Assistant

```python
# Defining the refactored function
from typing import Sequence, Optional

def gen_class(
    cls_name: str,
    docstring: Optional[str] = None,
    bases: Optional[Sequence[str]] = None,
    members: Optional[Sequence[str]] = None,
) -> str:
    bases_str = f"({', '.join(bases)})" if bases else ""
    members_str = "\n".join(members) if members else ""
    docstring_str = f'"""{docstring}"""' if docstring else ""
    
    body_parts = [part for part in [docstring_str, members_str] if part]
    body = "\n".join(body_parts) if body_parts else "pass"

    # Add indentation
    indented_body = "\n    ".join(body.split("\n"))

    return (
        f"class {cls_name}{bases_str}:\n    "
        f"{indented_body}"
    ).strip()

# Testing the function
test_cases = [
    {"cls_name": "Person", "docstring": "A simple Person class.", "bases": ["object"], "members": ["def __init__(self, name):", "    self.name = name"]},
    {"cls_name": "Employee", "docstring": None, "bases": ["Person"], "members": ["def __init__(self, name, id):", "    super().__init__(name)", "    self.id = id"]},
    {"cls_name": "Animal", "docstring": None, "bases": None, "members": None},
]

generated_classes = [gen_class(**test_case) for test_case in test_cases]
generated_classes
```

[child ⬇️](#adead8b7-703f-426d-b5f4-7e5b075f4b36)

---

(main branch ⎇)
###### adead8b7-703f-426d-b5f4-7e5b075f4b36
[parent ⬆️](#cca9954d-8802-442a-b3d1-267c0d293e08)
