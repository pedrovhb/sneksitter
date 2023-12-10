# Re-run the test for the Function model using the existing parser object
tree = parser.parse(bytes(test_code, 'utf8'))
root_node = tree.root_node
function_node = [n for n in root_node.children if n.type == 'function_definition'][0]

parsed_function = Function.from_node(function_node)
parsed_function.dict()
== Output ==
```
{ 'ename': 'ValidationError',
  'evalue': '5 validation errors for Function\n'
            'body\n'
            '  extra fields not permitted (type=value_error.extra)\n'
            'docstring\n'
            '  extra fields not permitted (type=value_error.extra)\n'
            'name\n'
            '  extra fields not permitted (type=value_error.extra)\n'
            'parameters\n'
            '  extra fields not permitted (type=value_error.extra)\n'
            'return_type\n'
            '  extra fields not permitted (type=value_error.extra)'}
```



[child ⬇️](#e51b521b-e7d8-419f-b3ba-1e10341833db)

---

(main branch ⎇)
###### e51b521b-e7d8-419f-b3ba-1e10341833db
[parent ⬆️](#4d468123-cf5b-4e33-8917-3ec219ef5cc3)
