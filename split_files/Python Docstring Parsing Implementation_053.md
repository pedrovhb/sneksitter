---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant -> 9d7c64d3-c964-4f73-8fcc-348a8808245f -> Tool -> 7871c14c-0813-4b57-850e-b8558bb04cdd -> Assistant -> aaa26f25-a8e5-4d20-9881-caea2489d0bc -> User -> 65a2c324-69d9-44db-a6e6-e9fcccbb110b -> Assistant -> 95a4e1ea-8365-4a4f-b155-9f0fe1d7374a -> Tool -> 64ee804e-ca9f-4d24-9cb5-71547925086d -> Assistant -> a57a358d-1f70-48b4-9cb1-3a9843aa8b55 -> Tool -> 6eed57d3-d50a-4638-8473-366254e18a81 -> Assistant -> aaa29656-f7db-49b2-abf5-aa1e8ac5f3e0 -> User -> 429ae43b-adb5-4d66-a796-74c34d8064b2 -> Assistant -> Plan for Parsing and Unparsing Google-Style Docstrings -> Overview -> Components of a Google-Style Docstring -> Data Classes -> Approaches -> Parsing -> Unparsing -> Selected Approaches -> Parsing: Line-by-Line Parsing -> Unparsing: Dynamic Generation -> Special Cases -> Precautions -> Implementation Steps -> afb9f9af-d2fc-44ce-b165-28e3b14c760f -> Assistant -> acb3b5ad-e8fd-4ef8-acb6-6192f4c3ff9d -> Tool -> 9bae8d8f-f579-4aeb-91e9-fec92a47f131 -> Assistant -> aaa2c153-0573-4f6e-9a55-6b6865e7b855 -> User -> 36ad5f2f-cd92-4f28-b26e-a6cafed6a606 -> Assistant
---
# Assistant

```python
from typing import Dict

@dataclass
class ParsedDocstring:
    short_summary: ShortSummary
    long_description: Optional[LongDescription] = None
    args: List[Arg] = field(default_factory=list)
    returns: Optional[Return] = None
    raises: List[Raises] = field(default_factory=list)
    examples: List[Example] = field(default_factory=list)
    
    @classmethod
    def from_str(cls: Type[T], docstring: str) -> T:
        lines = docstring.strip().split("\n")
        short_summary = ShortSummary.from_str(lines.pop(0))
        current_section = None
        section_lines = []
        parsed_sections: Dict[str, Union[str, List[str]]] = {}
        
        for line in lines:
            if line.strip().endswith(":"):
                # New section starts
                if current_section and section_lines:
                    parsed_sections[current_section] = "\n".join(section_lines)
                current_section = line.strip()[:-1]
                section_lines = []
            else:
                section_lines.append(line)
                
        if current_section and section_lines:
            parsed_sections[current_section] = "\n".join(section_lines)
        
        long_description = LongDescription.from_str(parsed_sections.get("Long Description", "")) if "Long Description" in parsed_sections else None
        args = [Arg.from_str(arg) for arg in parsed_sections.get("Args", "").split("\n") if arg.strip()] if "Args" in parsed_sections else []
        returns = Return.from_str(parsed_sections.get("Returns", "")) if "Returns" in parsed_sections else None
        raises = [Raises.from_str(raise_) for raise_ in parsed_sections.get("Raises", "").split("\n") if raise_.strip()] if "Raises" in parsed_sections else []
        examples = [Example.from_str(example) for example in parsed_sections.get("Examples", "").split("\n\n") if example.strip()] if "Examples" in parsed_sections else []
        
        return cls(short_summary, long_description, args, returns, raises, examples)
    
    def to_str(self) -> str:
        sections = []
        sections.append(self.short_summary.to_str())
        
        if self.long_description:
            sections.append(self.long_description.to_str())
        
        if self.args:
            args_section = ["Args:"]
            for arg in self.args:
                args_section.append(f"    {arg.to_str()}")
            sections.append("\n".join(args_section))
        
        if self.returns:
            sections.append(f"Returns:\n    {self.returns.to_str()}")
        
        if self.raises:
            raises_section = ["Raises:"]
            for raise_ in self.raises:
                raises_section.append(f"    {raise_.to_str()}")
            sections.append("\n".join(raises_section))
            
        if self.examples:
            examples_section = ["Examples:"]
            for example in self.examples:
                examples_section.append(example.to_str())
            sections.append("\n".join(examples_section))
        
        return "\n\n".join(sections)

# Test parsing and unparsing
sample_docstring = """
This is a summary.

Long Description:
    This function does something very important.

Args:
    arg1 (int): This is arg1.
    arg2 (str): This is arg2.

Returns:
    bool: True if successful, False otherwise.

Raises:
    ValueError: If something bad happens.

Examples:
    >>> print("hello")
    hello
"""

parsed = ParsedDocstring.from_str(sample_docstring)
unparsed = parsed.to_str()
print("Unparsed Docstring:")
print(unparsed)
```

[child ⬇️](#5fc260c1-13b7-400d-bc55-5f690de1ec3c)

---

(main branch ⎇)
###### 5fc260c1-13b7-400d-bc55-5f690de1ec3c
[parent ⬆️](#36ad5f2f-cd92-4f28-b26e-a6cafed6a606)
