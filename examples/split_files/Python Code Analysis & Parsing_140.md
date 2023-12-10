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



[child ⬇️](#99a89acb-0dd1-4ebc-a769-c8df4651d4f5)

---

(main branch ⎇)
###### 99a89acb-0dd1-4ebc-a769-c8df4651d4f5
[parent ⬆️](#3aca2368-9fa3-4c73-a9d7-1a195ceca202)
