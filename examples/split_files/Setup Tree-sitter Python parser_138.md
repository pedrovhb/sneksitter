#### 1. Classic and Straightforward: Method Chaining

We could use a simplified method chaining pattern, much like SQLAlchmey or Django ORM, where each method adds an element to the query.

```python
# Simple
QueryBuilder().node("function_definition").capture("func_def").build()

# Advanced with predicates
QueryBuilder().node("function_definition").predicate(lambda x: x.type == "main").build()
```

