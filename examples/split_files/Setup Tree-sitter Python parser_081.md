# Assistant

Certainly, a more concrete design that incorporates advanced features is warranted. Let's start by envisioning how an ideal interface would look from the user's perspective, using a design-by-contract style.

### Hypothetical Usage

```python
# Create a new query builder instance
qb = QueryBuilder()

# Simple query for capturing function definitions and calls
query = (qb.node('function_definition')
           .capture_as('function_def')
           .node('identifier')
           .field('name')
           .capture_as('function_name')
           .end()
         .node('call_expression')
           .capture_as('function_call')
           .node('identifier')
           .field('function')
           .capture_as('called_function')
           .end()
         .build())

# Advanced query with anchors, wildcards, and predicates
advanced_query = (qb.node('assignment_expression')
                    .anchor_start()
                    .node('identifier')
                    .capture_as('variable')
                    .end()
                  .node('function')
                    .capture_as('assigned_function')
                    .wildcard()
                    .predicate('eq?', '@assigned_function', 'main')
                    .end()
                  .anchor_end()
                  .build())
```

### API Design

#### Node Construction and Capture

The `.node()` method will initiate the construction of a new node. The `.capture_as()` method would be used to specify the capture name for the preceding node or field.

```python
def node(self, type: str) -> 'QueryBuilder':
    ...

def capture_as(self, name: str) -> 'QueryBuilder':
    ...
```

#### Field Qualification

To add a field to a node, we'll use the `.field()` method.

```python
def field(self, name: str) -> 'QueryBuilder':
    ...
```

#### Grouping and Nesting

The `.end()` method will signify the end of a nested query, essentially "closing" a node or a field, allowing you to continue with the parent query.

```python
def end(self) -> 'QueryBuilder':
    ...
```

#### Anchors and Wildcards

Anchors and wildcards can be added using `.anchor_start()`, `.anchor_end()`, and `.wildcard()` methods.

```python
def anchor_start(self) -> 'QueryBuilder':
    ...

def anchor_end(self) -> 'QueryBuilder':
    ...

def wildcard(self) -> 'QueryBuilder':
    ...
```

#### Predicates

Predicates like `eq?` can be added using the `.predicate()` method, which takes the predicate name and its arguments.

```python
def predicate(self, name: str, *args) -> 'QueryBuilder':
    ...
```

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

### Query Builder Class

The `QueryBuilder` class will maintain an internal list of nodes, manage the nesting levels, and construct the final S-expression.

```python
class QueryBuilder:
    def __init__(self):
        self.query = []
        self.nesting_level = 0
```

### Query Validation and Building

The `.build()` method would validate and transform the internal representation into the final S-expression.

```python
def build(self) -> str:
    # Validate and build the S-expression
```

### Summary

This design aims to provide a cohesive, fluent, and type-safe API for building Tree-Sitter queries. It allows for the construction of both simple and complex queries, incorporating advanced features like anchors, wildcards, and predicates seamlessly. The usage of Python dataclasses and type hints will ensure that the interface is both robust and user-friendly.

[child ⬇️](#aaa22527-f7af-4d58-9cde-1ff0cf27b18f)

---

(main branch ⎇)
###### aaa22527-f7af-4d58-9cde-1ff0cf27b18f
[parent ⬆️](#e39c17cd-eb8c-44f0-921c-f747f586900f)
