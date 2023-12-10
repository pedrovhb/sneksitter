#### 2. Advanced: Overloaded Operators

We could use Python's operator overloading to construct queries in a more intuitive manner. For example, the `|` could be used to signify OR conditions.

```python
# Simple
query = QueryBuilder()["function_definition"]

# Advanced
query = QueryBuilder()["function_definition" | "call_expression"]
```

