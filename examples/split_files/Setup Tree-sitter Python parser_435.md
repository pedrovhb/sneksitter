# Assistant

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class DecoratorInfo:
    name: str
    args: Optional[str] = None

@dataclass
class FunctionInfo:
    name: str
    parameters: List[str]
    decorators: List[DecoratorInfo] = field(default_factory=list)

# Initialize list to hold parsed function information
parsed_functions = []

# Helper function to extract text from a node
extract_text = lambda node: source_code[node.start_byte:node.end_byte].decode()

# Iterate through the captures and populate the dataclasses
current_function = None
current_decorator = None

for node, capture in quantified_captures:
    if capture == 'function.name':
        if current_function:
            parsed_functions.append(current_function)
        current_function = FunctionInfo(name=extract_text(node), parameters=[])
    elif capture == 'parameter':
        if current_function:
            current_function.parameters.append(extract_text(node))
    elif capture == 'decorator':
        current_decorator = DecoratorInfo(name=extract_text(node))
        if current_function:
            current_function.decorators.append(current_decorator)

# Append the last function if any
if current_function:
    parsed_functions.append(current_function)

parsed_functions
```

[child ⬇️](#38ae3dbe-3b28-4cc0-bba8-98b882a2445d)

---

(main branch ⎇)
###### 38ae3dbe-3b28-4cc0-bba8-98b882a2445d
[parent ⬆️](#c56cff40-3c53-4e97-847e-e0533f358787)
