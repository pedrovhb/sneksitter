### Basic Building Blocks

Firstly, let's consider the basic building blocks of Tree-Sitter queries:

1. **Node**: Represents a single node in the AST. e.g., `(function_definition)`.
2. **Field**: Qualifies a child node within a parent node. e.g., `left: (identifier)`.
3. **Capture**: Associates a name with a specific node. e.g., `(identifier) @function_name`.
4. **Operator**: Quantifies nodes like `+`, `*`, `?`.

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

