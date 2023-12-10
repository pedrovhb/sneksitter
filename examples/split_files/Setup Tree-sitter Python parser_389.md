# Assistant

```python
from dataclasses import dataclass, field
from typing import List, Union, Optional

@dataclass
class DecoratorInfo:
    name: str
    args: Optional[List[Union[str, int]]]  # Assume that the args can only be strings or integers for simplicity

@dataclass
class FunctionInfo:
    name: str
    parameters: List[str]
    decorators: List[DecoratorInfo]

    @classmethod
    def from_node(cls, node):
        """
        Create a FunctionInfo instance from a tree-sitter node representing a decorated function.
        """
        decorators = []
        func_name = ""
        parameters = []
        
        for child in node.children:
            if child.type == 'decorator':
                decorator_name = child.children[1].text.decode()
                decorator_args = []
                for arg_node in child.children[2].children:
                    if arg_node.type in ['string', 'integer']:
                        decorator_args.append(arg_node.text.decode().replace('"', ''))
                decorators.append(DecoratorInfo(name=decorator_name, args=decorator_args if decorator_args else None))
            
            elif child.type == 'function_definition':
                func_name = child.children[1].text.decode()
                params_node = child.children[2]
                for param in params_node.children:
                    if param.type == 'identifier':
                        parameters.append(param.text.decode())

        return cls(name=func_name, parameters=parameters, decorators=decorators)

# Test the FunctionInfo class with a sample node
sample_decorated_definition_node = decorator_sample_tree.root_node.children[0]
FunctionInfo.from_node(sample_decorated_definition_node)
```

[child ⬇️](#228a1410-86f3-4a88-887d-fc45c82694a6)

---

(other branch ⎇)
###### 228a1410-86f3-4a88-887d-fc45c82694a6
[parent ⬆️](#57707e39-23ae-4b70-a45a-7d7ff8f7d338)
