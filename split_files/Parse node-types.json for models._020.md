---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info -> Internal Nodes -> Task -> 9387b9ba-fae2-448c-b4df-a2a1a946c3b6 -> Tool -> b6a63d27-6380-4d59-9ae7-88eabcad6cff -> Assistant -> Key Components: -> Observations: -> Examples: -> aaa2bc1e-c7a6-4ef9-8020-e692c381a096 -> User -> 3682d6bc-a0f0-4628-af8b-6b87bf5ae291 -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Union

# Define the basic Node type with common fields "type" and "named"
@dataclass
class NodeType:
    type: str
    named: bool

# Define the ChildType to describe the possible children that a node can have
@dataclass
class ChildType:
    required: bool
    multiple: bool
    types: List[NodeType]

# Extend NodeType to incorporate internal nodes with "fields" and "children"
@dataclass
class InternalNodeType(NodeType):
    fields: Optional[Dict[str, ChildType]] = field(default_factory=dict)
    children: Optional[ChildType] = None

# Extend NodeType to handle supertype nodes with "subtypes"
@dataclass
class SupertypeNode(NodeType):
    subtypes: List[NodeType]

# Create a union type to represent any kind of node
AnyNodeType = Union[NodeType, InternalNodeType, SupertypeNode]

# Function to parse JSON object into corresponding dataclass instance
def parse_node(node_json: Dict) -> AnyNodeType:
    if "subtypes" in node_json:
        return SupertypeNode(
            type=node_json["type"],
            named=node_json["named"],
            subtypes=[NodeType(type=subtype["type"], named=subtype["named"]) for subtype in node_json["subtypes"]]
        )
    
    if "fields" in node_json or "children" in node_json:
        fields = {k: ChildType(**v) for k, v in node_json.get("fields", {}).items()}
        children = ChildType(**node_json["children"]) if "children" in node_json else None
        return InternalNodeType(
            type=node_json["type"],
            named=node_json["named"],
            fields=fields,
            children=children
        )
    
    return NodeType(
        type=node_json["type"],
        named=node_json["named"]
    )

# Parse the JSON data into dataclass instances
parsed_nodes = [parse_node(node) for node in node_types_data]

# Show the first few parsed nodes to confirm the dataclasses are working as expected
parsed_nodes[:5]
```

[child ⬇️](#4e945266-3138-47a1-8055-825076720fed)

---

(other branch ⎇)
###### 4e945266-3138-47a1-8055-825076720fed
[parent ⬆️](#3682d6bc-a0f0-4628-af8b-6b87bf5ae291)
