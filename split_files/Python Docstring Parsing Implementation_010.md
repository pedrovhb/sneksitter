---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field
from typing import List, TypeVar, Type, Optional
from parse import parse

T = TypeVar('T', bound='DocElement')

@dataclass
class DocElement:
    @classmethod
    def from_str(cls: Type[T], text: str) -> T:
        raise NotImplementedError()
        
    def to_str(self) -> str:
        raise NotImplementedError()

@dataclass
class Description(DocElement):
    short_desc: str
    long_desc: Optional[str] = None

    @classmethod
    def from_str(cls, text: str) -> 'Description':
        lines = text.strip().split('\n')
        short_desc = lines[0].strip()
        long_desc = '\n'.join(lines[1:]).strip() if len(lines) > 1 else None
        return cls(short_desc, long_desc)
    
    def to_str(self) -> str:
        if self.long_desc:
            return f"{self.short_desc}\n\n{self.long_desc}"
        return self.short_desc

@dataclass
class Parameter(DocElement):
    name: str
    type_hint: str
    description: str

    @classmethod
    def from_str(cls, text: str) -> 'Parameter':
        parsed = parse("{name}: {type_hint} -- {description}", text)
        return cls(parsed['name'], parsed['type_hint'], parsed['description'])
    
    def to_str(self) -> str:
        return f"{self.name}: {self.type_hint} -- {self.description}"

@dataclass
class Returns(DocElement):
    type_hint: str
    description: str

    @classmethod
    def from_str(cls, text: str) -> 'Returns':
        parsed = parse("{type_hint} -- {description}", text)
        return cls(parsed['type_hint'], parsed['description'])
    
    def to_str(self) -> str:
        return f"{self.type_hint} -- {self.description}"

@dataclass
class Raises(DocElement):
    exception: str
    description: str

    @classmethod
    def from_str(cls, text: str) -> 'Raises':
        parsed = parse("{exception} -- {description}", text)
        return cls(parsed['exception'], parsed['description'])
    
    def to_str(self) -> str:
        return f"{self.exception} -- {self.description}"

@dataclass
class Example(DocElement):
    code: str
    expected_output: Optional[str] = None

    @classmethod
    def from_str(cls, text: str) -> 'Example':
        parts = text.strip().split('\n\n')
        code = parts[0]
        expected_output = parts[1] if len(parts) > 1 else None
        return cls(code, expected_output)
    
    def to_str(self) -> str:
        if self.expected_output:
            return f"{self.code}\n\n{self.expected_output}"
        return self.code

@dataclass
class OtherSections(DocElement):
    name: str
    content: str

    @classmethod
    def from_str(cls, text: str) -> 'OtherSections':
        lines = text.strip().split('\n')
        name = lines[0].strip()
        content = '\n'.join(lines[1:]).strip()
        return cls(name, content)
    
    def to_str(self) -> str:
        return f"{self.name}\n{self.content}"

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
        # Initialize empty data structures
        description = None
        parameters = []
        returns = None
        raises = []
        examples = []
        other_sections = []
        
        # Split the docstring into lines and initialize variables
        lines = text.strip().split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            stripped_line = line.strip()
            
            # Check if this line is a section header
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
        
        # Process the last section
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

[child ⬇️](#9d7c64d3-c964-4f73-8fcc-348a8808245f)

---

(other branch ⎇)
###### 9d7c64d3-c964-4f73-8fcc-348a8808245f
[parent ⬆️](#7a848fb4-fafb-4120-84f6-6725ea253bc6)
