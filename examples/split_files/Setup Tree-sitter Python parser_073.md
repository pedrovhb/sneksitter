### Example Usage

Here's how you could build a query for function calls:

```python
qb = QueryBuilder()
query = (qb.add_node(Node('call_expression'))
           .add_node(Node('identifier', field='function', capture='@function_name'))
           .build())
```

This would generate the S-expression `"(call_expression function: (identifier) @function_name)"`.

