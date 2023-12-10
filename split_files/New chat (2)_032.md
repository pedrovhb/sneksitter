---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (2).md
heading_stack: <root> -> e7c9baec-ffab-4c2e-bbb4-561fd977d430 -> System -> 536e0e74-8c30-49ea-ae85-f83cc1361c13 -> System -> aaa29187-c9e6-4055-a115-71076813ffbc -> User -> cc136d1c-37a8-4c4a-b365-9b8369a2b895 -> Assistant -> Approaches: -> Generalized to ASTs: -> Code Example: -> a238746d-f3e1-4b77-a9b7-ba0f5e8f7049 -> Assistant -> 29d82439-fb56-42eb-afe8-8ca15db19eb8 -> Tool -> f1219ce2-4490-4271-881d-328b7eed1acf -> Assistant -> aaa2c008-0c05-4714-90ce-395abd9559a8 -> User -> b4bb145a-3220-4564-b3ee-c5ec6c3ac485 -> Assistant -> 8d058de8-bf7e-4d33-8add-ff38a294ccf3 -> Tool -> 82fca1ae-6c6b-4948-a056-d75568771d51 -> Assistant -> aaa22bef-f9a9-4ccd-a7ee-a32f715e1298 -> User -> b4eff856-22ed-48d6-9914-b5d88ad5900c -> Assistant -> Design: -> 104bd562-86a6-4f4a-bc9f-a0547164b28e -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field
from typing import Any, Callable, TypeVar, Union, List

# Define type variables
NodeT = TypeVar("NodeT")
EdgeT = TypeVar("EdgeT")

@dataclass
class QueryNode:
    predicate: Callable[[NodeT], bool]
    logical_op: Union[str, None] = None  # Logical operation to combine with the previous query ('and', 'or')
    next_node: 'QueryNode' = None  # Reference to the next QueryNode in the chain
    
    def evaluate(self, node: NodeT) -> bool:
        """Evaluates the predicate for a given node."""
        return self.predicate(node)
    
    def combine(self, other: 'QueryNode', logical_op: str) -> 'QueryNode':
        """Combines this QueryNode with another using a logical operation ('and', 'or')."""
        self.next_node = other
        self.logical_op = logical_op
        return self
```

[child ⬇️](#16e122ab-f2db-436e-828f-bfa39aa4f7ed)

---

(main branch ⎇)
###### 16e122ab-f2db-436e-828f-bfa39aa4f7ed
[parent ⬆️](#104bd562-86a6-4f4a-bc9f-a0547164b28e)
