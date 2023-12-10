#### Dataclasses for Basic Blocks

We can use Python dataclasses to represent each of these components. For example, the `Node` can be represented as:

```python
from dataclasses import dataclass

@dataclass
class Node:
    type: str
    capture: str = None
    field: str = None
    operator: str = None
```

