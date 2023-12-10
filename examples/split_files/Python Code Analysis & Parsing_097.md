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



[child ⬇️](#80ae8cf5-d2ae-4579-8baf-7ec77a47c294)

---

(main branch ⎇)
###### 80ae8cf5-d2ae-4579-8baf-7ec77a47c294
[parent ⬆️](#51cb4061-e6af-44b2-a166-8f5743c955ed)
