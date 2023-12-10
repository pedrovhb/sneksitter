# Assistant

```python
from dataclasses import dataclass, field
from typing import List, Optional, Union

@dataclass
class FunctionInfo:
    name: str
    parameters: str
    decorators: Optional[List[str]] = field(default_factory=list)

# Helper function to extract the text from a Node
def extract_text(node: Node) -> str:
    return node.text.decode()

# Parse the captures into dataclasses
function_infos = []
current_function = None

for node, capture in incremental_captures_with_decorator_fixed:
    if capture == 'function_name':
        if current_function:
            function_infos.append(current_function)
        current_function = FunctionInfo(name=extract_text(node), parameters='', decorators=[])
    elif capture == 'function_parameters':
        if current_function:
            current_function.parameters = extract_text(node)
    # elif capture == 'function_decorator':
    #     if current_function:
    #         current_function.decorators.append(extract_text(node))

# Append the last function if any
if current_function:
    function_infos.append(current_function)

function_infos
```

[child ⬇️](#39bd675e-4ad4-4c3f-b640-d873f3f61c46)

---

(main branch ⎇)
###### 39bd675e-4ad4-4c3f-b640-d873f3f61c46
[parent ⬆️](#7d1fb529-53e2-4995-a214-ce800d720af5)
