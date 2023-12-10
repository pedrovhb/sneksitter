### Base Classes and Data Models

Let's start by defining the basic elements of a query: nodes, fields, predicates, and operations. These can be implemented as dataclasses.

```python
from dataclasses import dataclass
from typing import Union, List

@dataclass
class Node:
    type: str
    children: List['Node'] = None
    field: str = None
    negated_field: str = None
    capture: str = None
```

