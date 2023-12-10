---
file: /home/pedro/Documents/chatgpt_export/Markdown/Pydantic Models Validate Grammar.md
heading_stack: <root> -> 061eaf6e-d372-4cb3-89fb-2c4a94f643f6 -> System -> cc0cd000-c5d4-4660-bc2e-8fe013b3c090 -> System -> aaa29d07-977b-4c5b-84ea-2dbd6660aa55 -> User -> Basic Info -> Internal Nodes -> Task -> a59e5ca8-0836-43aa-95ae-557da12f334d -> Tool -> df057f39-09fe-452a-a373-0e8af0517ed8 -> Assistant -> eac7e948-a00f-48dc-9291-b50e427443d8 -> Tool -> 269ca8b2-1769-4ac8-8a5d-deb74bea2c07 -> Assistant -> f12a4d59-1929-403d-abba-eb91897bd209 -> Assistant -> 7a1efd11-fe1f-45ce-8b70-9980dd6701b5 -> Tool -> d2cd1215-a1ae-4c2a-b2e0-8fdba68f2e90 -> Assistant -> a37fa0ec-cfd0-4c94-9569-4b2f95e88c3b -> Assistant -> 2cc0efdf-d6d5-4231-bbfc-49f199cba9b3 -> Tool -> 1a5fb753-2396-462e-8a40-245073e84638 -> Assistant -> aaa214e6-f126-4374-aa7a-a864d4a4a650 -> User -> c9a1a2b6-9829-4136-84a4-7fb52290ecc2 -> Assistant -> 0aac7ebc-176b-4f59-8385-8754815705e0 -> Tool -> 90c0afda-35b5-4d6c-b767-652a10ec7009 -> Assistant -> aaa251f8-f462-4594-a7f4-5110ef19aa88 -> User -> 6f4a1dde-3ce3-4099-8dba-56f8f2ecce2e -> Assistant -> 06d698da-0d98-48ba-8744-ea08aeb456a5 -> Tool -> 91c2c938-df80-4721-9821-48906b31862c -> Assistant -> aaa2bc5d-a4c0-4982-907a-b33f5407edf6 -> User -> a2c08485-4965-42e5-9297-a02f55ebe428 -> Assistant -> adbaeae2-7686-4bd8-a984-217f8adb12f8 -> Tool -> 8fd7c313-58e6-4151-b647-c80fa34c4a77 -> Assistant -> aaa23544-1053-4bfa-8cd2-0ee10a09de03 -> User -> e3569785-9e36-4f56-b9f4-aac6c4ece636 -> Assistant
---
# Assistant

```python
# Implement multiple passes over the supertypes to recursively identify children and create a more detailed tree view.
# The process will continue until no new supernodes are visited.

# Function to recursively identify and collect all child types for a given supertype
def collect_children(supertype, visited):
    if supertype in visited:
        return []
    
    visited.add(supertype)
    children = supertype_to_children.get(supertype, [])
    
    # Recursively collect children of the current node's children
    for child in children[:]:  # Copy the list to avoid modification during iteration
        grandchildren = collect_children(child, visited)
        children.extend(grandchild for grandchild in grandchildren if grandchild not in children)
        
    return children

# Initial empty set to keep track of visited supernodes
visited = set()

# Run multiple passes until no new nodes are visited
previous_visited_count = 0
while len(visited) > previous_visited_count:
    previous_visited_count = len(visited)
    for supertype in validated_data.supertypes:
        collect_children(supertype, visited)

# Generate the tree view using the populated supertype_to_children mapping
tree_views = {st: generate_tree_view(st) for st in validated_data.supertypes}

# Combine all tree views into a single string for display
tree_view_str = "\n".join(f"Supertype: {st}\n{tree}" for st, tree in tree_views.items())
print(tree_view_str)
```

[child ⬇️](#bff1d3d5-822f-4a91-a2d9-475d5930d718)

---

(other branch ⎇)
###### bff1d3d5-822f-4a91-a2d9-475d5930d718
[parent ⬆️](#e3569785-9e36-4f56-b9f4-aac6c4ece636)
