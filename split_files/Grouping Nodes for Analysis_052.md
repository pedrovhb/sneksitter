---
file: /home/pedro/Documents/chatgpt_export/Markdown/Grouping Nodes for Analysis.md
heading_stack: <root> -> 6db24c38-564f-43d4-b8c9-2fec4e4db353 -> System -> 2953287f-20e5-44fb-a584-4bfe4f961bbb -> System -> aaa23f50-fb72-4433-a7f7-075d9fdfe0f3 -> User -> b5e935e4-8ecf-4850-ac07-4d63ba79b17e -> Assistant -> ad08acfc-210e-4de6-8495-802cfd6644c0 -> Assistant -> 58d33044-a31f-4722-880d-41adf2e0d2e9 -> Tool -> 9a8e14e9-c1db-4b63-9860-668ca3c413e6 -> Assistant -> aaa20cb6-bdc0-41ca-b038-b00cfecd1334 -> User -> f356137c-fbe2-438d-87bb-9695d4112c6c -> Assistant -> d7ff89f8-b73e-4302-af13-473e623c04d9 -> Assistant -> 8df1bdf2-c2ab-45fe-8f3c-29e899a2be79 -> Tool -> f9188ff9-69b8-4c8b-9f72-46698e2fed91 -> Assistant -> a486650a-5d1b-44dd-a66a-ecbb8f23cf42 -> Assistant -> 7fdad3d6-7b6d-4d3c-8450-6f8525f549d8 -> Tool -> 7c2665d3-04a1-463c-96b6-5fe58821ab2f -> Assistant -> aaa2d1fe-01f1-415d-a411-8207fa5fc1ac -> User -> f381d9d6-d4ba-4a39-aee9-5fe0ada66351 -> Assistant -> 08f84522-f933-4eb5-a3ee-545e563022a4 -> Assistant -> 67db0ed6-ee08-4988-ad9f-f19485da0924 -> Tool -> c855f4d9-51a4-4004-9177-c2a2991bac50 -> Assistant -> aaa21fdf-f794-428e-b18e-0a5da141e948 -> User -> 1b40b10b-55f0-4dc2-a8c7-de2fc63cd84e -> Assistant -> aaa24d94-a27f-490b-80ab-67ef86010eb1 -> User -> 31ecee52-cf50-4cbc-9cde-2bca459edf37 -> Assistant -> aaa29558-6bf8-4ccc-95d4-1172c48e4e9e -> User -> ecffc7d4-45ff-4069-839f-2399766750b2 -> Assistant
---
# Assistant

```python
from typing import NamedTuple, List, Dict, Any

# Define a named tuple to represent a node with its corresponding semantic tag
class TaggedNode(NamedTuple):
    type: str
    start_point: Tuple[int, int]
    end_point: Tuple[int, int]
    tag: str

# Example data
example_nodes = [
    TaggedNode("call", (2, 1), (2, 26), 'function.decorator'),
    TaggedNode("identifier", (2, 1), (2, 10), 'decorator.name'),
    TaggedNode("argument_list", (2, 10), (2, 26), 'decorator.args'),
    TaggedNode("identifier", (3, 1), (3, 11), 'decorator.name'),
    TaggedNode("identifier", (3, 1), (3, 11), 'function.decorator'),
    TaggedNode("function_definition", (4, 0), (31, 58), 'function'),
    TaggedNode("identifier", (4, 4), (4, 20), 'function.name'),
    TaggedNode("parameters", (4, 20), (4, 66), 'function.parameters'),
    TaggedNode("identifier", (4, 21), (4, 29), 'function.parameter.name'),
    TaggedNode("type", (4, 31), (4, 34), 'function.parameter.type'),
    TaggedNode("identifier", (4, 36), (4, 51), 'function.parameter.name'),
    TaggedNode("type", (4, 53), (4, 57), 'function.parameter.type'),
    TaggedNode("false", (4, 60), (4, 65), 'function.parameter.default'),
    TaggedNode("type", (4, 70), (4, 90), 'function.return'),
    TaggedNode("block", (5, 4), (31, 58), 'function.body_contents'),
    TaggedNode("string", (5, 4), (8, 7), 'function.docstring'),
    TaggedNode("block", (5, 4), (31, 58), 'function.body_contents'),
    TaggedNode("string", (5, 4), (8, 7), 'function.docstring'),
    TaggedNode("identifier", (34, 1), (34, 5), 'decorator.name'),
    TaggedNode("identifier", (34, 1), (34, 5), 'function.decorator'),
    TaggedNode("function_definition", (35, 0), (38, 46), 'function'),
    TaggedNode("identifier", (35, 4), (35, 9), 'function.name'),
    TaggedNode("parameters", (35, 9), (35, 73), 'function.parameters'),
    TaggedNode("identifier", (35, 10), (35, 16), 'function.parameter.name'),
    TaggedNode("type", (35, 18), (35, 21), 'function.parameter.type'),
    TaggedNode("identifier", (35, 23), (35, 31), 'function.parameter.name'),
    TaggedNode("type", (35, 33), (35, 36), 'function.parameter.type'),
    TaggedNode("identifier", (35, 38), (35, 58), 'function.parameter.name'),
    TaggedNode("type", (35, 60), (35, 64), 'function.parameter.type'),
    TaggedNode("false", (35, 67), (35, 72), 'function.parameter.default'),
    TaggedNode("type", (35, 77), (35, 93), 'function.return'),
    TaggedNode("block", (36, 4), (38, 46), 'function.body_contents')
]

# Sort nodes by their start_point
sorted_nodes = sorted(example_nodes, key=lambda x: x.start_point)

def process_nodes(sorted_nodes: List[TaggedNode]) -> List[Dict[str, Any]]:
    functions = []
    function = {}
    parameters = []
    decorators = []
    for node in sorted_nodes:
        if node.tag == 'function':
            if function:  # Save the previous function if exists
                function['parameters'] = parameters
                function['decorators'] = decorators
                functions.append(function)
                parameters = []
                decorators = []
            function = {'type': node.type}
        elif 'function.name' in node.tag:
            function['name'] = node.type  # Replace with actual name
        elif 'function.parameter' in node.tag:
            param = {}
            if 'name' in node.tag:
                param['name'] = node.type  # Replace with actual name
            if 'type' in node.tag:
                param['type'] = node.type  # Replace with actual type
            if 'default' in node.tag:
                param['default'] = node.type  # Replace with actual default value
            parameters.append(param)
        elif 'function.decorator' in node.tag:
            decorators.append({'type': node.type})
    
    # Save the last function
    if function:
        function['parameters'] = parameters
        function['decorators'] = decorators
        functions.append(function)
    
    return functions

functions = process_nodes(sorted_nodes)
final_structure = {'functions': functions}
final_structure
```

[child ⬇️](#86da3ef8-5517-42a1-ad2a-de60a7202a46)

---

(main branch ⎇)
###### 86da3ef8-5517-42a1-ad2a-de60a7202a46
[parent ⬆️](#ecffc7d4-45ff-4069-839f-2399766750b2)
