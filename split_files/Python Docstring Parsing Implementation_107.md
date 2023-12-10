---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant -> 9d7c64d3-c964-4f73-8fcc-348a8808245f -> Tool -> 7871c14c-0813-4b57-850e-b8558bb04cdd -> Assistant -> aaa26f25-a8e5-4d20-9881-caea2489d0bc -> User -> 65a2c324-69d9-44db-a6e6-e9fcccbb110b -> Assistant -> 95a4e1ea-8365-4a4f-b155-9f0fe1d7374a -> Tool -> 64ee804e-ca9f-4d24-9cb5-71547925086d -> Assistant -> a57a358d-1f70-48b4-9cb1-3a9843aa8b55 -> Tool -> 6eed57d3-d50a-4638-8473-366254e18a81 -> Assistant -> aaa29656-f7db-49b2-abf5-aa1e8ac5f3e0 -> User -> 429ae43b-adb5-4d66-a796-74c34d8064b2 -> Assistant -> Plan for Parsing and Unparsing Google-Style Docstrings -> Overview -> Components of a Google-Style Docstring -> Data Classes -> Approaches -> Parsing -> Unparsing -> Selected Approaches -> Parsing: Line-by-Line Parsing -> Unparsing: Dynamic Generation -> Special Cases -> Precautions -> Implementation Steps -> afb9f9af-d2fc-44ce-b165-28e3b14c760f -> Assistant -> acb3b5ad-e8fd-4ef8-acb6-6192f4c3ff9d -> Tool -> 9bae8d8f-f579-4aeb-91e9-fec92a47f131 -> Assistant -> aaa2c153-0573-4f6e-9a55-6b6865e7b855 -> User -> 36ad5f2f-cd92-4f28-b26e-a6cafed6a606 -> Assistant -> 5fc260c1-13b7-400d-bc55-5f690de1ec3c -> Tool -> 5a63389e-4e81-4419-92f6-6bc5a9307900 -> Assistant -> 89c9f9ca-4713-4df2-b40d-83df128714eb -> Assistant -> 0324f526-e41f-4b14-b3b6-3e29566e6664 -> Tool -> 6ffefeec-1e2a-4043-b2c3-9e78f9ef06ba -> Assistant -> 608c299e-da95-4ef0-a4a8-4c8419f76d52 -> Assistant -> 74e32b74-4e65-4ce4-996a-b06610bda728 -> Tool -> a0f6a357-9575-4d9e-a087-1a84f84366bd -> Assistant -> 5bbcc4e9-1192-486b-b6ac-37c7df31c2f8 -> Assistant -> c6a723e2-e589-4a5c-ba0e-efece0779f9e -> Tool -> 347c41f7-3b07-41cf-a2b5-52eb14f0ce2c -> Assistant -> aaa26bee-572b-4959-a3b8-c150034abd07 -> User -> 1ad095ba-9a79-4fb7-9a46-e1cfff153bb4 -> Assistant -> 8be439cb-3dad-4548-a1b5-d05db5011cc3 -> Tool -> 3e730538-35fe-4b02-8300-a647b26b7792 -> Assistant -> ae82f122-1710-4121-b1e8-43ec449dfe18 -> Assistant -> 55a0f313-f9c0-4f28-b20a-fd798d4c2523 -> Tool -> 1b3d164f-40e3-4bcc-9ec4-bfb45ca192fb -> Assistant -> 9fa1c18c-deeb-4449-b510-0edddae65c8b -> Assistant -> 0851a49b-3750-4879-929f-bd7e4777a87d -> Tool -> 7c03304e-8373-4e11-9d87-b37f89aab358 -> Assistant -> 7e58fe09-a299-4d4e-95a7-1a19de2f397c -> Assistant -> 8abb6a28-c5f7-4fe2-8b00-bb74bcd3409b -> Tool -> 3a488036-76c7-414d-81fa-e49127e700ac -> Assistant -> 4dfaccf8-96de-4496-80a5-74ae37604077 -> Assistant -> 4084b160-fd10-4a69-806a-9eefe3ab430a -> Tool -> 82163eae-4f46-4b90-bb7c-ff4a3af2934f -> Assistant
---
# Assistant

```python
# Update the Example class to fix the indentation and handle multiple multi-line examples

@dataclass
class Example:
    code: str
    expected_output: Optional[str] = None
    
    INDENT_PATTERN: ClassVar[Pattern] = re.compile(r"^\s*")
    
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
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

# Update the ParsedDocstring class to handle multiple multi-line examples

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

# Test parsing and unparsing with multiple multi-line examples
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

    >>> print("world")
    world
"""

parsed = ParsedDocstring.from_str(sample_docstring)
unparsed = parsed.to_str()
print("Unparsed Docstring:")
print(unparsed)
```

[child ⬇️](#39a5040b-d81e-4fc8-9e91-c6b1f263e7d7)

---

(main branch ⎇)
###### 39a5040b-d81e-4fc8-9e91-c6b1f263e7d7
[parent ⬆️](#82163eae-4f46-4b90-bb7c-ff4a3af2934f)