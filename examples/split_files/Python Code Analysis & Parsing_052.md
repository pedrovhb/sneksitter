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


[child ⬇️](#a59776f9-4514-473e-b473-809ba0e07a1c)

---

(main branch ⎇)
###### a59776f9-4514-473e-b473-809ba0e07a1c
[parent ⬆️](#c20c6649-739b-4ec4-8885-46c3be7a10b1)
