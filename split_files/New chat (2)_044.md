---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (2).md
heading_stack: <root> -> e7c9baec-ffab-4c2e-bbb4-561fd977d430 -> System -> 536e0e74-8c30-49ea-ae85-f83cc1361c13 -> System -> aaa29187-c9e6-4055-a115-71076813ffbc -> User -> cc136d1c-37a8-4c4a-b365-9b8369a2b895 -> Assistant -> Approaches: -> Generalized to ASTs: -> Code Example: -> a238746d-f3e1-4b77-a9b7-ba0f5e8f7049 -> Assistant -> 29d82439-fb56-42eb-afe8-8ca15db19eb8 -> Tool -> f1219ce2-4490-4271-881d-328b7eed1acf -> Assistant -> aaa2c008-0c05-4714-90ce-395abd9559a8 -> User -> b4bb145a-3220-4564-b3ee-c5ec6c3ac485 -> Assistant -> 8d058de8-bf7e-4d33-8add-ff38a294ccf3 -> Tool -> 82fca1ae-6c6b-4948-a056-d75568771d51 -> Assistant -> aaa22bef-f9a9-4ccd-a7ee-a32f715e1298 -> User -> b4eff856-22ed-48d6-9914-b5d88ad5900c -> Assistant -> Design: -> 104bd562-86a6-4f4a-bc9f-a0547164b28e -> Assistant -> 16e122ab-f2db-436e-828f-bfa39aa4f7ed -> Tool -> b02c5db1-9ad5-4939-8bd8-aa59a9c6b557 -> Assistant -> 9b2d3607-c709-4fc4-8538-ebf92d3bde56 -> Assistant -> c5b8c212-728c-4fe8-8f3a-a7b4f0192f92 -> Tool -> fe53cc43-94fc-46e7-baed-171a6da9377d -> Assistant -> 731821cf-5d1e-4c27-b899-a28ff2d41032 -> Assistant
---
# Assistant

```python
# Redefine NodeWrapper to handle cases where the right-hand side is not a NodeWrapper

class NodeWrapper:
    def __init__(self, predicate: Optional[Callable[[NodeT], bool]] = None):
        self.predicate = predicate if predicate else lambda node: True

    def __eq__(self, other):
        return NodeWrapper(lambda node: node.get("node_type") == other)

    def __or__(self, other):
        other_predicate = other.predicate if isinstance(other, NodeWrapper) else lambda node: node.get("node_type") == other
        return NodeWrapper(lambda node: self.predicate(node) or other_predicate(node))
    
    def __and__(self, other):
        other_predicate = other.predicate if isinstance(other, NodeWrapper) else lambda node: node.get("node_type") == other
        return NodeWrapper(lambda node: self.predicate(node) and other_predicate(node))

# Redefine symbol for node operations
N = NodeWrapper()

# Reinitialize QueryWrapper and rebuild query
my_queriable = QueryWrapper[NodeT, EdgeT](G)
my_queriable.add_predicate((N == "module").predicate)
my_queriable.add_predicate((N == "function_definition" | N == "class_definition" | N == "decorated_definition").predicate, logical_op="or")

# Re-run resolve
print(my_queriable.resolve())
```

[child ⬇️](#c8cf863a-b329-4cba-8005-96a60c18cb54)

---

(main branch ⎇)
###### c8cf863a-b329-4cba-8005-96a60c18cb54
[parent ⬆️](#731821cf-5d1e-4c27-b899-a28ff2d41032)
