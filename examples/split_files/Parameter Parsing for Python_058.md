# Assistant

```python
# Using the tree_sitter_languages library to get the Python parser as specified
parser = tree_sitter_languages.get_parser("python")

# Sample Python code with complex function definition
source_code = '''
def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
    """This is a docstring."""
    pass
'''

# Parse the source code
tree = parser.parse(source_code.encode())

# Extract the parameters node for testing
root_node = tree.root_node
function_node = [child for child in root_node.children if child.type == 'function_definition'][0]
parameters_node = [child for child in function_node.children if child.type == 'parameters'][0]

# Test the from_node_parameters method
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters
```

[child ⬇️](#7b89084c-52ee-48c4-a6f0-0763da4405b9)

---

(main branch ⎇)
###### 7b89084c-52ee-48c4-a6f0-0763da4405b9
[parent ⬆️](#24f0988c-9a61-42df-b995-604b2476b424)
