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

