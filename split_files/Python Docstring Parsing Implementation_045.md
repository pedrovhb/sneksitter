---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant -> 9d7c64d3-c964-4f73-8fcc-348a8808245f -> Tool -> 7871c14c-0813-4b57-850e-b8558bb04cdd -> Assistant -> aaa26f25-a8e5-4d20-9881-caea2489d0bc -> User -> 65a2c324-69d9-44db-a6e6-e9fcccbb110b -> Assistant -> 95a4e1ea-8365-4a4f-b155-9f0fe1d7374a -> Tool -> 64ee804e-ca9f-4d24-9cb5-71547925086d -> Assistant -> a57a358d-1f70-48b4-9cb1-3a9843aa8b55 -> Tool -> 6eed57d3-d50a-4638-8473-366254e18a81 -> Assistant -> aaa29656-f7db-49b2-abf5-aa1e8ac5f3e0 -> User -> 429ae43b-adb5-4d66-a796-74c34d8064b2 -> Assistant -> Plan for Parsing and Unparsing Google-Style Docstrings -> Overview -> Components of a Google-Style Docstring -> Data Classes -> Approaches -> Parsing -> Unparsing -> Selected Approaches -> Parsing: Line-by-Line Parsing -> Unparsing: Dynamic Generation -> Special Cases -> Precautions -> Implementation Steps -> afb9f9af-d2fc-44ce-b165-28e3b14c760f -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field
from typing import List, Optional, Type, TypeVar, Union, ClassVar, Pattern
import re

T = TypeVar("T")

@dataclass
class ShortSummary:
    text: str
    
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
        return cls(text.strip())
    
    def to_str(self) -> str:
        return self.text

@dataclass
class LongDescription:
    text: str
    
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
        return cls(text.strip())
    
    def to_str(self) -> str:
        return self.text

@dataclass
class Arg:
    name: str
    type: str
    description: str
    
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
        name_type, description = text.split(":", 1)
        name, type_ = name_type.strip().split(" ", 1)
        return cls(name, type_, description.strip())
    
    def to_str(self) -> str:
        return f"{self.name} ({self.type}): {self.description}"

@dataclass
class Return:
    type: str
    description: str
    
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
        type_, description = text.split(":", 1)
        return cls(type_.strip(), description.strip())
    
    def to_str(self) -> str:
        return f"{self.type}: {self.description}"

@dataclass
class Raises:
    exception: str
    description: str
    
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
        exception, description = text.split(":", 1)
        return cls(exception.strip(), description.strip())
    
    def to_str(self) -> str:
        return f"{self.exception}: {self.description}"

@dataclass
class Example:
    code: str
    expected_output: Optional[str] = None
    
    INDENT_PATTERN: ClassVar[Pattern] = re.compile(r"^\s+")
    
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
        # Split the text into lines and analyze the indent level for example code
        lines = text.strip().split("\n")
        indent_match = cls.INDENT_PATTERN.match(lines[0])
        if not indent_match:
            raise ValueError("Invalid indentation in example")
        
        indent_level = len(indent_match.group())
        
        code_lines = []
        output_lines = []
        is_output = False
        for line in lines:
            if line.startswith(" " * indent_level + ">>> "):
                is_output = False
                code_lines.append(line[indent_level + 4 :])
            elif is_output:
                output_lines.append(line[indent_level:])
            else:
                code_lines.append(line[indent_level:])

            if line.strip() == "":
                is_output = True

        code = "\n".join(code_lines)
        expected_output = "\n".join(output_lines) if output_lines else None
        return cls(code, expected_output)
    
    def to_str(self) -> str:
        lines = []
        for code_line in self.code.split("\n"):
            lines.append(f"    >>> {code_line}")
        if self.expected_output:
            lines.append("")
            lines.extend([f"    {line}" for line in self.expected_output.split("\n")])
        return "\n".join(lines)
```

[child ⬇️](#acb3b5ad-e8fd-4ef8-acb6-6192f4c3ff9d)

---

(main branch ⎇)
###### acb3b5ad-e8fd-4ef8-acb6-6192f4c3ff9d
[parent ⬆️](#afb9f9af-d2fc-44ce-b165-28e3b14c760f)
