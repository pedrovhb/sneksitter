# Test the Function model using the existing parser object
test_code = """
def example_function(param1: int, param2: str = 'default') -> None:
    '''This is a docstring.'''
    print(param1, param2)
"""

tree = parser.parse(bytes(test_code, 'utf8'))
root_node = tree.root_node
function_node = [n for n in root_node.children if n.type == 'function_definition'][0]

parsed_function = Function.from_node(function_node)
parsed_function.dict()
== Output ==
{'name': b'',
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
 'body': b"'''This is a docstring.'''\n    print(param1, param2)"}



[child ⬇️](#28ceffdf-4d67-488a-be57-e6174c7768cd)

---

(main branch ⎇)
###### 28ceffdf-4d67-488a-be57-e6174c7768cd
[parent ⬆️](#622cf93a-3101-4cae-9862-48762dbe74d9)
