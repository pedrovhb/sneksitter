---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant -> 9d7c64d3-c964-4f73-8fcc-348a8808245f -> Tool -> 7871c14c-0813-4b57-850e-b8558bb04cdd -> Assistant -> aaa26f25-a8e5-4d20-9881-caea2489d0bc -> User -> 65a2c324-69d9-44db-a6e6-e9fcccbb110b -> Assistant -> 95a4e1ea-8365-4a4f-b155-9f0fe1d7374a -> Tool -> 64ee804e-ca9f-4d24-9cb5-71547925086d -> Assistant -> a57a358d-1f70-48b4-9cb1-3a9843aa8b55 -> Tool -> 6eed57d3-d50a-4638-8473-366254e18a81 -> Assistant -> aaa29656-f7db-49b2-abf5-aa1e8ac5f3e0 -> User -> 429ae43b-adb5-4d66-a796-74c34d8064b2 -> Assistant -> Plan for Parsing and Unparsing Google-Style Docstrings -> Overview -> Components of a Google-Style Docstring -> Data Classes -> Approaches -> Parsing -> Unparsing -> Selected Approaches -> Parsing: Line-by-Line Parsing -> Unparsing: Dynamic Generation -> Special Cases -> Precautions -> Implementation Steps -> afb9f9af-d2fc-44ce-b165-28e3b14c760f -> Assistant -> acb3b5ad-e8fd-4ef8-acb6-6192f4c3ff9d -> Tool -> 9bae8d8f-f579-4aeb-91e9-fec92a47f131 -> Assistant -> aaa2c153-0573-4f6e-9a55-6b6865e7b855 -> User -> 36ad5f2f-cd92-4f28-b26e-a6cafed6a606 -> Assistant -> 5fc260c1-13b7-400d-bc55-5f690de1ec3c -> Tool -> 5a63389e-4e81-4419-92f6-6bc5a9307900 -> Assistant -> 89c9f9ca-4713-4df2-b40d-83df128714eb -> Assistant -> 0324f526-e41f-4b14-b3b6-3e29566e6664 -> Tool -> 6ffefeec-1e2a-4043-b2c3-9e78f9ef06ba -> Assistant -> 608c299e-da95-4ef0-a4a8-4c8419f76d52 -> Assistant -> 74e32b74-4e65-4ce4-996a-b06610bda728 -> Tool -> a0f6a357-9575-4d9e-a087-1a84f84366bd -> Assistant -> 5bbcc4e9-1192-486b-b6ac-37c7df31c2f8 -> Assistant -> c6a723e2-e589-4a5c-ba0e-efece0779f9e -> Tool -> 347c41f7-3b07-41cf-a2b5-52eb14f0ce2c -> Assistant -> aaa26bee-572b-4959-a3b8-c150034abd07 -> User -> 1ad095ba-9a79-4fb7-9a46-e1cfff153bb4 -> Assistant -> 8be439cb-3dad-4548-a1b5-d05db5011cc3 -> Tool -> 3e730538-35fe-4b02-8300-a647b26b7792 -> Assistant -> ae82f122-1710-4121-b1e8-43ec449dfe18 -> Assistant -> 55a0f313-f9c0-4f28-b20a-fd798d4c2523 -> Tool -> 1b3d164f-40e3-4bcc-9ec4-bfb45ca192fb -> Assistant -> 9fa1c18c-deeb-4449-b510-0edddae65c8b -> Assistant -> 0851a49b-3750-4879-929f-bd7e4777a87d -> Tool -> 7c03304e-8373-4e11-9d87-b37f89aab358 -> Assistant -> 7e58fe09-a299-4d4e-95a7-1a19de2f397c -> Assistant -> 8abb6a28-c5f7-4fe2-8b00-bb74bcd3409b -> Tool -> 3a488036-76c7-414d-81fa-e49127e700ac -> Assistant -> 4dfaccf8-96de-4496-80a5-74ae37604077 -> Assistant -> 4084b160-fd10-4a69-806a-9eefe3ab430a -> Tool -> 82163eae-4f46-4b90-bb7c-ff4a3af2934f -> Assistant -> 39a5040b-d81e-4fc8-9e91-c6b1f263e7d7 -> Tool -> c3bbecc5-f325-45c3-81b5-6fb251ff6a55 -> Assistant -> ae96dcab-ce6a-49fb-a2a4-89ca4c7932f1 -> Assistant -> b714dfde-8620-4cdd-bdef-d611d49157e5 -> Tool -> aac4fe5f-b481-4bb9-b0eb-51c17bfd6165 -> Assistant -> aaa23f7c-d91b-4a14-8695-54f3bccd743d -> User -> 85266a25-05af-4418-8962-7cbc12b3d38e -> Assistant -> 1b503602-4e85-42f5-b2ad-df945ea04eb6 -> Tool -> 55832e76-d248-4255-ab3d-627ba3a4a035 -> Assistant -> 06bc9948-e324-4730-974c-d45865c50a37 -> Assistant -> 5014ca08-5c99-4dd8-b71e-7e9071710a7c -> Tool -> 3ee9de71-da5a-4839-b3ed-0969e4e3c3da -> Assistant -> e8658664-7130-412b-8054-22e635029ea0 -> Assistant -> aaa20728-3897-4da8-b30f-1e74f1261ae0 -> User -> 010e2d1c-c0f6-42f5-83df-8d97ee85d7bd -> Assistant -> 91ad63fa-e600-4bae-80a0-363f8d22e1be -> Tool -> 924b9a9d-8262-416e-93fa-9fe329d9e067 -> Assistant -> f98dc4ce-39e7-4f3a-88cc-e26767b847d2 -> Assistant -> 2a0f0907-4258-438e-9095-f134aebd02c9 -> Tool -> 9f667b7a-689f-445d-b3f0-f036e65f4967 -> Assistant -> 2968f8a8-22de-4a75-8fdf-4bdca5f85b7f -> Assistant -> b02e1781-9b5e-4457-a303-552fe6626542 -> Tool -> a479df43-477b-4331-9b32-fa50bdbdf387 -> Assistant -> 69dc961f-ad87-4d02-9cd9-81a20f24768f -> Assistant
---
# Assistant

```python
# Debug the SingleExample class to identify why the expected output lines are missing

@dataclass
class SingleExample:
    code: str
    expected_output: Optional[str] = None

    @classmethod
    def from_str(cls: Type[T], lines: List[str]) -> T:
        code_lines = []
        output_lines = []
        is_output = False
        for line in lines:
            if line.startswith(">>> "):
                is_output = False
                code_lines.append(line[4:])
            elif line.startswith("... "):
                code_lines.append(line[4:])
            elif is_output:
                output_lines.append(line)
            
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

# Test parsing and unparsing just the Example class
example_text = """
>>> print("hello")
hello

>>> print("world")
world

>>> for i in range(3):
...     print(i)
0
1
2
"""

parsed_example_section = ExampleSection.from_str(example_text)
print("Parsed Examples:")
for example in parsed_example_section.examples:
    print(f"Code: {example.code}, Expected Output: {example.expected_output}")

unparsed_example_section = parsed_example_section.to_str()
print("Unparsed Example Section:")
print(unparsed_example_section)
```

[child ⬇️](#2b038bef-9f56-46f2-a631-4dde2f0ef29d)

---

(main branch ⎇)
###### 2b038bef-9f56-46f2-a631-4dde2f0ef29d
[parent ⬆️](#69dc961f-ad87-4d02-9cd9-81a20f24768f)
