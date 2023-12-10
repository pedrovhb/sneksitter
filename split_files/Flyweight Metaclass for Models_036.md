---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User -> cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4 -> Assistant -> aee36206-2846-4af8-97fc-c08ea32d04f7 -> Assistant -> fe5d834e-f4ba-4d75-a77b-b419a41172d6 -> Tool -> 3cc5cb2f-9bf2-4ec7-b730-4b7a6e37379d -> Assistant -> aaa2c0bf-efc0-41ea-9394-4821c3fecdd6 -> User -> 7770a31d-c47b-48a5-9a87-cd318296e663 -> Assistant -> 186f96c5-6c2e-4c78-90de-dfcc8ee777fc -> Tool -> c7e4a869-cad6-4bc6-8ce6-a57f1c21d6a5 -> Assistant -> aaa25436-2417-4590-99f2-b2c737ebd76e -> User -> 19cc38f8-b99d-499e-968a-3b533d806593 -> System -> 5827125a-b24e-4d18-86f6-470e815d7c30 -> Assistant -> 2514e975-d6c8-40fa-82d6-b29ba3ca3f5b -> Tool -> c413c192-dbfa-4cd5-b113-6201359a48c4 -> Assistant -> aaa26c46-7fbc-40e0-84af-8ed1af29aead -> User -> 506d9386-4909-4f98-b93b-918b5195353d -> Assistant
---
# Assistant

```python
# Test data with slight modifications to ensure unique objects
basic_node_data_modified = {'type': 'A', 'named': False}
child_type_data_modified = {'required': True, 'multiple': True, 'types': [basic_node_data]}
internal_node_data_modified = {'type': 'Internal', 'named': False, 'fields': {'field1': child_type_data}}
supertype_node_data_modified = {'type': 'Super', 'named': False, 'subtypes': [basic_node_data_modified]}

# Creating modified objects
basic_node3 = BasicNode.from_dict(basic_node_data_modified)
child_type3 = ChildType.from_dict(child_type_data_modified)
internal_node3 = InternalNode.from_dict(internal_node_data_modified)
supertype_node3 = SupertypeNode.from_dict(supertype_node_data_modified)

# Check if objects with different attributes are indeed different objects
tests_different = [
    basic_node1 is basic_node3,
    child_type1 is child_type3,
    internal_node1 is internal_node3,
    supertype_node1 is supertype_node3,
]

tests_different
```

[child ⬇️](#8d250109-2a1c-441d-ba2a-308f0a29d4ee)

---

(main branch ⎇)
###### 8d250109-2a1c-441d-ba2a-308f0a29d4ee
[parent ⬆️](#506d9386-4909-4f98-b93b-918b5195353d)
