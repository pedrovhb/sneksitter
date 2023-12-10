### Data Structures

Nodes, fields, and captures can be represented as Python dataclasses.

```python
from dataclasses import dataclass
from typing import List, Union

@dataclass
class Node:
    type: str
    capture: str = None
    field: str = None
    anchor: str = None
    wildcard: bool = False
    predicates: List[str] = None
```

