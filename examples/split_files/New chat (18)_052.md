# Assistant

Here's the core logic for parsing the function parameters based on the FSM.

```python
def parse_parameters(node):
    state = ParamState.INIT
    parameters = []
    temp_param = {}

    for child in node.children:
        token_type = child.type

        if state == ParamState.INIT:
            if token_type == "identifier":
                temp_param["name"] = child
                state = ParamState.NAME
            elif token_type == "list_splat_pattern":
                temp_param["is_vararg"] = True
                state = ParamState.VARARG
            elif token_type == "dictionary_splat_pattern":
                temp_param["is_kwarg"] = True
                state = ParamState.KWARG
            elif token_type == "positional_separator":
                state = ParamState.POS_ONLY
            elif token_type == "keyword_separator":
                state = ParamState.KW_ONLY

        elif state == ParamState.NAME:
            if token_type == "type":
                temp_param["type"] = child
                state = ParamState.TYPE
            else:
                parameters.append(temp_param)
                temp_param = {}
                state = ParamState.INIT

        elif state == ParamState.TYPE:
            if token_type == "default_parameter":
                temp_param["default"] = child
                state = ParamState.DEFAULT
            else:
                parameters.append(temp_param)
                temp_param = {}
                state = ParamState.INIT

        elif state == ParamState.DEFAULT:
            parameters.append(temp_param)
            temp_param = {}
            state = ParamState.INIT

        elif state == ParamState.POS_ONLY:
            temp_param["is_positional_only"] = True
            state = ParamState.INIT

        elif state == ParamState.KW_ONLY:
            temp_param["is_keyword_only"] = True
            state = ParamState.INIT

    if temp_param:
        parameters.append(temp_param)

    return parameters

# Let's do a quick test by simulating a node
class FakeNode:
    def __init__(self, type, children=[]):
        self.type = type
        self.children = children

root = FakeNode("parameters", [
    FakeNode("identifier", []),
    FakeNode("type", []),
    FakeNode("default_parameter", []),
    FakeNode("identifier", []),
    FakeNode("keyword_separator", []),
    FakeNode("identifier", []),
])

parsed_params = parse_parameters(root)
print(parsed_params)
```

This code should now allow us to parse parameters and handle various types like varargs, kwargs, positional-only, and keyword-only parameters. The `temp_param` dictionary temporarily holds information for each parameter until all of its components are parsed, at which point it is appended to the `parameters` list.

[child ⬇️](#292fe1ca-3d8e-4c50-a48e-77c5ac0cf5ee)

---

(main branch ⎇)
###### 292fe1ca-3d8e-4c50-a48e-77c5ac0cf5ee
[parent ⬆️](#45bd1bba-f9c3-4155-8793-2913f7d7ce64)
