#### 4. Borrowing from Art: Lambda Functions for Predicates

Inspired by Pandas, we could use lambda functions for adding predicates to the query, allowing for more dynamic and complex conditions.

```python
# Simple
QueryBuilder().node("function_definition")

# Advanced
QueryBuilder().node("function_definition").where(lambda x: x.type == "main")
```

