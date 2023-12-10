### Query Serialization

Once the `Node` tree is built, a separate function or method can be used to serialize it into the S-expression syntax that Tree-Sitter expects. This ensures a clean separation between the query building and query execution stages.

```python
def serialize(node: Node) -> str:
    ...
```

