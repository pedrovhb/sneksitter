---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant -> 9d7c64d3-c964-4f73-8fcc-348a8808245f -> Tool -> 7871c14c-0813-4b57-850e-b8558bb04cdd -> Assistant -> aaa26f25-a8e5-4d20-9881-caea2489d0bc -> User -> 65a2c324-69d9-44db-a6e6-e9fcccbb110b -> Assistant
---
# Assistant

```python
# Implementing manual parsing logic instead of using `parse` library

@dataclass
class Parameter(DocElement):
    name: str
    type_hint: str
    description: str

    @classmethod
    def from_str(cls, text: str) -> 'Parameter':
        name, rest = text.split(':', 1)
        type_hint, description = rest.split('--', 1)
        return cls(name.strip(), type_hint.strip(), description.strip())
    
    def to_str(self) -> str:
        return f"{self.name}: {self.type_hint} -- {self.description}"

@dataclass
class Returns(DocElement):
    type_hint: str
    description: str

    @classmethod
    def from_str(cls, text: str) -> 'Returns':
        type_hint, description = text.split('--', 1)
        return cls(type_hint.strip(), description.strip())
    
    def to_str(self) -> str:
        return f"{self.type_hint} -- {self.description}"

@dataclass
class Raises(DocElement):
    exception: str
    description: str

    @classmethod
    def from_str(cls, text: str) -> 'Raises':
        exception, description = text.split('--', 1)
        return cls(exception.strip(), description.strip())
    
    def to_str(self) -> str:
        return f"{self.exception} -- {self.description}"

# Now re-running the Docstring class definition to keep it in sync

@dataclass
class Docstring:
    description: Description
    parameters: List[Parameter] = field(default_factory=list)
    returns: Optional[Returns] = None
    raises: List[Raises] = field(default_factory=list)
    examples: List[Example] = field(default_factory=list)
    other_sections: List[OtherSections] = field(default_factory=list)

    def to_str(self) -> str:
        sections = []
        sections.append(self.description.to_str())
        if self.parameters:
            sections.append("Args:")
            for param in self.parameters:
                sections.append(f"    {param.to_str()}")
        if self.returns:
            sections.append("Returns:")
            sections.append(f"    {self.returns.to_str()}")
        if self.raises:
            sections.append("Raises:")
            for exc in self.raises:
                sections.append(f"    {exc.to_str()}")
        if self.examples:
            sections.append("Examples:")
            for example in self.examples:
                sections.append(f"    {example.to_str()}")
        for other in self.other_sections:
            sections.append(other.to_str())
        return '\n'.join(sections)
    
    @classmethod
    def from_str(cls, text: str) -> 'Docstring':
        description = None
        parameters = []
        returns = None
        raises = []
        examples = []
        other_sections = []
        
        lines = text.strip().split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            stripped_line = line.strip()
            
            if stripped_line.endswith(':'):
                if current_section == 'Description':
                    description = Description.from_str('\n'.join(current_content))
                elif current_section == 'Args':
                    for param_text in current_content:
                        parameters.append(Parameter.from_str(param_text.strip()))
                elif current_section == 'Returns':
                    returns = Returns.from_str(current_content[0].strip())
                elif current_section == 'Raises':
                    for raise_text in current_content:
                        raises.append(Raises.from_str(raise_text.strip()))
                elif current_section == 'Examples':
                    example_text = '\n'.join(current_content).strip()
                    examples.append(Example.from_str(example_text))
                elif current_section:
                    other_sections.append(OtherSections.from_str(f"{current_section}:\n{' '.join(current_content)}"))
                    
                current_section = stripped_line[:-1]
                current_content = []
            else:
                current_content.append(stripped_line)
        
        if current_section == 'Description':
            description = Description.from_str('\n'.join(current_content))
        elif current_section == 'Args':
            for param_text in current_content:
                parameters.append(Parameter.from_str(param_text.strip()))
        elif current_section == 'Returns':
            returns = Returns.from_str(current_content[0].strip())
        elif current_section == 'Raises':
            for raise_text in current_content:
                raises.append(Raises.from_str(raise_text.strip()))
        elif current_section == 'Examples':
            example_text = '\n'.join(current_content).strip()
            examples.append(Example.from_str(example_text))
        elif current_section:
            other_sections.append(OtherSections.from_str(f"{current_section}:\n{' '.join(current_content)}"))
        
        return cls(description, parameters, returns, raises, examples, other_sections)
```

[child ⬇️](#95a4e1ea-8365-4a4f-b155-9f0fe1d7374a)

---

(other branch ⎇)
###### 95a4e1ea-8365-4a4f-b155-9f0fe1d7374a
[parent ⬆️](#65a2c324-69d9-44db-a6e6-e9fcccbb110b)
