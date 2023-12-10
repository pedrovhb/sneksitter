### Hypothetical Simplified Usage

Here's how one might use an ideal, simplified API:

```python
# Initialize a query builder
qb = QueryBuilder()

# Simple query to capture function names and calls
query = qb.match('function_definition', capture='function_def')
          .child('identifier', field='name', capture='function_name')
          .or_()
          .match('call_expression', capture='function_call')
          .child('identifier', field='function', capture='called_function')
          .build()

# Advanced query with anchors, wildcards, and predicates
advanced_query = qb.match('assignment_expression')
                   .start_anchor()
                   .child('identifier', capture='variable')
                   .child('function', capture='assigned_function')
                   .wildcard()
                   .predicate('eq?', 'assigned_function', 'main')
                   .end_anchor()
                   .build()
```

