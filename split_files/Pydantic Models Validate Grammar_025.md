---
file: /home/pedro/Documents/chatgpt_export/Markdown/Pydantic Models Validate Grammar.md
heading_stack: <root> -> 061eaf6e-d372-4cb3-89fb-2c4a94f643f6 -> System -> cc0cd000-c5d4-4660-bc2e-8fe013b3c090 -> System -> aaa29d07-977b-4c5b-84ea-2dbd6660aa55 -> User -> Basic Info -> Internal Nodes -> Task -> a59e5ca8-0836-43aa-95ae-557da12f334d -> Tool -> df057f39-09fe-452a-a373-0e8af0517ed8 -> Assistant -> eac7e948-a00f-48dc-9291-b50e427443d8 -> Tool -> 269ca8b2-1769-4ac8-8a5d-deb74bea2c07 -> Assistant -> f12a4d59-1929-403d-abba-eb91897bd209 -> Assistant -> 7a1efd11-fe1f-45ce-8b70-9980dd6701b5 -> Tool -> d2cd1215-a1ae-4c2a-b2e0-8fdba68f2e90 -> Assistant -> a37fa0ec-cfd0-4c94-9569-4b2f95e88c3b -> Assistant
---
# Assistant

```python
from pydantic import BaseModel, Field
from typing import List, Union, Optional, Dict, Any

# Define child type object
class ChildType(BaseModel):
    required: Optional[bool]
    multiple: Optional[bool]
    types: Optional[List[Dict[str, Union[str, bool]]]]

# Define fields in internal nodes
class Fields(BaseModel):
    multiple: Optional[bool]
    required: Optional[bool]
    types: Optional[List[Dict[str, Union[str, bool]]]]

# Define the basic information for each node type
class NodeType(BaseModel):
    type: str
    named: Optional[bool]
    fields: Optional[Dict[str, ChildType]]
    children: Optional[ChildType]
    subtypes: Optional[List[Dict[str, Union[str, bool]]]]

# Define the supertype nodes
class Supertype(BaseModel):
    type: str
    named: Optional[bool]
    subtypes: Optional[List[Dict[str, Union[str, bool]]]]

# Define the root model to encapsulate all information
class GrammarModel(BaseModel):
    rules: Dict[str, NodeType]
    supertypes: List[str]

# Validate the data using the Pydantic models
validated_data = GrammarModel(**grammar_data)
validated_data
```

[child ⬇️](#2cc0efdf-d6d5-4231-bbfc-49f199cba9b3)

---

(other branch ⎇)
###### 2cc0efdf-d6d5-4231-bbfc-49f199cba9b3
[parent ⬆️](#a37fa0ec-cfd0-4c94-9569-4b2f95e88c3b)
