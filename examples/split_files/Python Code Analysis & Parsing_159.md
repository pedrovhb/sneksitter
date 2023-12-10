# Re-run the test for the Function model using the existing parser object
tree = parser.parse(bytes(test_code, 'utf8'))
root_node = tree.root_node
function_node = [n for n in root_node.children if n.type == 'function_definition'][0]

parsed_function = Function.from_node(function_node)
parsed_function.dict()
== Output ==
{'name': '',
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
 'docstring': 'def',
 'body': "'''This is a docstring.'''\n    print(param1, param2)"}



[child ⬇️](#a759a1b8-639a-4388-b457-37f556a4c6c5)

---

(main branch ⎇)
###### a759a1b8-639a-4388-b457-37f556a4c6c5
[parent ⬆️](#1212270f-c102-4519-962f-5fd0a77512dc)
