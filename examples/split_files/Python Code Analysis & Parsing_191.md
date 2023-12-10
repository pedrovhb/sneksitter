# Re-run the test for the Function model using the existing parser object
tree = parser.parse(bytes(test_code, 'utf8'))
root_node = tree.root_node
function_node = [n for n in root_node.children if n.type == 'function_definition'][0]

parsed_function = Function.from_node(function_node)
parsed_function.dict()
== Output ==
{'name': 'example_function',
 'parameters': [{'name': b'param1',
   'type': b'int',
   'default': None,
   'description': None,
   'is_vararg': False,
   'is_kwarg': False,
   'is_positional_only': False,
   'is_keyword_only': False},
  {'name': b'param2',
   'type': b'str',
   'default': b"'default'",
   'description': None,
   'is_vararg': False,
   'is_kwarg': False,
   'is_positional_only': False,
   'is_keyword_only': False}],
 'return_type': None,
 'docstring': None,
 'body': 'print(param1, param2)'}



[child ⬇️](#084d511f-2118-492c-b56f-fe49e1837531)

---

(main branch ⎇)
###### 084d511f-2118-492c-b56f-fe49e1837531
[parent ⬆️](#e21695f3-3745-4434-ba96-4d32c8b5511e)
