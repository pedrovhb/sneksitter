---
file: /home/pedro/Documents/chatgpt_export/Markdown/Pydantic Models Validate Grammar.md
heading_stack: <root> -> 061eaf6e-d372-4cb3-89fb-2c4a94f643f6 -> System -> cc0cd000-c5d4-4660-bc2e-8fe013b3c090 -> System -> aaa29d07-977b-4c5b-84ea-2dbd6660aa55 -> User -> Basic Info -> Internal Nodes -> Task -> a59e5ca8-0836-43aa-95ae-557da12f334d -> Tool -> df057f39-09fe-452a-a373-0e8af0517ed8 -> Assistant -> eac7e948-a00f-48dc-9291-b50e427443d8 -> Tool -> 269ca8b2-1769-4ac8-8a5d-deb74bea2c07 -> Assistant -> f12a4d59-1929-403d-abba-eb91897bd209 -> Assistant -> 7a1efd11-fe1f-45ce-8b70-9980dd6701b5 -> Tool -> d2cd1215-a1ae-4c2a-b2e0-8fdba68f2e90 -> Assistant -> a37fa0ec-cfd0-4c94-9569-4b2f95e88c3b -> Assistant -> 2cc0efdf-d6d5-4231-bbfc-49f199cba9b3 -> Tool -> 1a5fb753-2396-462e-8a40-245073e84638 -> Assistant -> aaa214e6-f126-4374-aa7a-a864d4a4a650 -> User -> c9a1a2b6-9829-4136-84a4-7fb52290ecc2 -> Assistant -> 0aac7ebc-176b-4f59-8385-8754815705e0 -> Tool -> 90c0afda-35b5-4d6c-b767-652a10ec7009 -> Assistant -> aaa251f8-f462-4594-a7f4-5110ef19aa88 -> User -> 6f4a1dde-3ce3-4099-8dba-56f8f2ecce2e -> Assistant
---
# Assistant

```python
# Merge Fields and ChildType into a single class
class ChildType(BaseModel):
    required: Optional[bool]
    multiple: Optional[bool]
    types: Optional[List['NodeType']]  # Recursive reference

# Update NodeType to use the merged class
class NodeType(BaseModel):
    type: str
    named: Optional[bool]
    fields: Optional[Dict[str, ChildType]]
    children: Optional[ChildType]
    subtypes: Optional[List['NodeType']]  # Recursive reference

# Update forward references
NodeType.update_forward_refs()

# Create a tree view to represent supertypes and their children types
def generate_tree_view(node_type: NodeType, level: int = 0, visited=None):
    if visited is None:
        visited = set()
    
    if node_type.type in visited:
        return f"{'  ' * level}|- {node_type.type} (recursive)\n"
    
    visited.add(node_type.type)
    
    tree_str = f"{'  ' * level}|- {node_type.type}\n"
    if node_type.subtypes:
        for subtype in node_type.subtypes:
            tree_str += generate_tree_view(subtype, level + 1, visited)
    
    return tree_str

# Create tree views for supertypes
tree_views = {}
for supertype in validated_data.supertypes:
    # Find the NodeType object for each supertype
    node_type = NodeType(type=supertype, subtypes=[validated_data.rules.get(t) for t in validated_data.rules if t == supertype])
    tree_views[supertype] = generate_tree_view(node_type)

tree_views
```

[child ⬇️](#06d698da-0d98-48ba-8744-ea08aeb456a5)

---

(other branch ⎇)
###### 06d698da-0d98-48ba-8744-ea08aeb456a5
[parent ⬆️](#6f4a1dde-3ce3-4099-8dba-56f8f2ecce2e)
