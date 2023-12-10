---
file: /home/pedro/Documents/chatgpt_export/Markdown/Pydantic Models Validate Grammar.md
heading_stack: <root> -> 061eaf6e-d372-4cb3-89fb-2c4a94f643f6 -> System -> cc0cd000-c5d4-4660-bc2e-8fe013b3c090 -> System -> aaa29d07-977b-4c5b-84ea-2dbd6660aa55 -> User -> Basic Info -> Internal Nodes -> Task -> a59e5ca8-0836-43aa-95ae-557da12f334d -> Tool -> df057f39-09fe-452a-a373-0e8af0517ed8 -> Assistant -> eac7e948-a00f-48dc-9291-b50e427443d8 -> Tool -> 269ca8b2-1769-4ac8-8a5d-deb74bea2c07 -> Assistant -> f12a4d59-1929-403d-abba-eb91897bd209 -> Assistant -> 7a1efd11-fe1f-45ce-8b70-9980dd6701b5 -> Tool -> d2cd1215-a1ae-4c2a-b2e0-8fdba68f2e90 -> Assistant -> a37fa0ec-cfd0-4c94-9569-4b2f95e88c3b -> Assistant -> 2cc0efdf-d6d5-4231-bbfc-49f199cba9b3 -> Tool -> 1a5fb753-2396-462e-8a40-245073e84638 -> Assistant -> aaa214e6-f126-4374-aa7a-a864d4a4a650 -> User -> c9a1a2b6-9829-4136-84a4-7fb52290ecc2 -> Assistant
---
# Assistant

```python
# Update the Pydantic models to be recursively nested where appropriate

# Define child type object
class ChildType(BaseModel):
    required: Optional[bool]
    multiple: Optional[bool]
    types: Optional[List['NodeType']]  # Recursive reference

# Define fields in internal nodes
class Fields(BaseModel):
    multiple: Optional[bool]
    required: Optional[bool]
    types: Optional[List['NodeType']]  # Recursive reference

# Define the basic information for each node type
class NodeType(BaseModel):
    type: str
    named: Optional[bool]
    fields: Optional[Dict[str, ChildType]]
    children: Optional[ChildType]
    subtypes: Optional[List['NodeType']]  # Recursive reference

# Define the supertype nodes
class Supertype(BaseModel):
    type: str
    named: Optional[bool]
    subtypes: Optional[List['NodeType']]  # Recursive reference

# Update forward references
NodeType.update_forward_refs()

# Validate the data again using the updated Pydantic models
try:
    validated_data = GrammarModel(rules=rules_data, supertypes=supertypes_data)
    validation_success = True
except Exception as e:
    validation_success = False
    validation_error = str(e)

validation_success, validation_error if not validation_success else "No errors"
```

[child ⬇️](#0aac7ebc-176b-4f59-8385-8754815705e0)

---

(other branch ⎇)
###### 0aac7ebc-176b-4f59-8385-8754815705e0
[parent ⬆️](#c9a1a2b6-9829-4136-84a4-7fb52290ecc2)
