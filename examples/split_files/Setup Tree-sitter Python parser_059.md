### Support for Complex Queries

So far, the design is simple but limited. For example, it doesn't yet support predicates, quantifiers, or alternations. These could be added as properties of the `Node` class, or as specialized subclasses.

```python
@dataclass
class PredicateNode(Node):
    predicate: str
    args: List[Union[str, Node]]
```

```python
@dataclass
class QuantifiedNode(Node):
    quantifier: str  # Could be '+', '*', '?'
```

