### Refined Hypothetical Usage with Magic Methods

```python
# Initialize a query builder
qb = QueryBuilder()

# Simple query to capture function names and calls
query = (qb['function_definition']('@function_def')
          ['identifier'](field='name', capture='@function_name')
          .or_()
          ['call_expression']('@function_call')
          ['identifier'](field='function', capture='@called_function')
          .build())

# Advanced query with anchors, wildcards, and predicates
advanced_query = (qb['assignment_expression'].start_anchor()
                   ['identifier']('@variable')
                   ['function']('@assigned_function').wildcard()
                   .predicate(lambda n: n.text == 'main')
                   .end_anchor()
                   .build())
```

