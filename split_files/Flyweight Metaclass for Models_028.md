---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User -> cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4 -> Assistant -> aee36206-2846-4af8-97fc-c08ea32d04f7 -> Assistant -> fe5d834e-f4ba-4d75-a77b-b419a41172d6 -> Tool -> 3cc5cb2f-9bf2-4ec7-b730-4b7a6e37379d -> Assistant -> aaa2c0bf-efc0-41ea-9394-4821c3fecdd6 -> User -> 7770a31d-c47b-48a5-9a87-cd318296e663 -> Assistant -> 186f96c5-6c2e-4c78-90de-dfcc8ee777fc -> Tool -> c7e4a869-cad6-4bc6-8ce6-a57f1c21d6a5 -> Assistant -> aaa25436-2417-4590-99f2-b2c737ebd76e -> User -> 19cc38f8-b99d-499e-968a-3b533d806593 -> System -> 5827125a-b24e-4d18-86f6-470e815d7c30 -> Assistant
---
# Assistant

```python
# Test data to initialize objects
basic_node_data = {'type': 'A', 'named': True}
child_type_data = {'required': False, 'multiple': True, 'types': [basic_node_data]}
field_data = {'key': 'field1', 'type': child_type_data}
internal_node_data = {'type': 'Internal', 'named': True, 'fields': {'field1': child_type_data}}
supertype_node_data = {'type': 'Super', 'named': True, 'subtypes': [basic_node_data]}

# Creating objects
basic_node1 = BasicNode.from_dict(basic_node_data)
basic_node2 = BasicNode.from_dict(basic_node_data)

child_type1 = ChildType.from_dict(child_type_data)
child_type2 = ChildType.from_dict(child_type_data)

field1 = Field(field_data['key'], ChildType.from_dict(field_data['type']))
field2 = Field(field_data['key'], ChildType.from_dict(field_data['type']))

internal_node1 = InternalNode.from_dict(internal_node_data)
internal_node2 = InternalNode.from_dict(internal_node_data)

supertype_node1 = SupertypeNode.from_dict(supertype_node_data)
supertype_node2 = SupertypeNode.from_dict(supertype_node_data)

# Check if objects with the same attributes are indeed the same object
tests = [
    basic_node1 is basic_node2,
    child_type1 is child_type2,
    field1 is field2,
    internal_node1 is internal_node2,
    supertype_node1 is supertype_node2,
]

tests
```

[child ⬇️](#2514e975-d6c8-40fa-82d6-b29ba3ca3f5b)

---

(main branch ⎇)
###### 2514e975-d6c8-40fa-82d6-b29ba3ca3f5b
[parent ⬆️](#5827125a-b24e-4d18-86f6-470e815d7c30)
