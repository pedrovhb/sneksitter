---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User -> cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4 -> Assistant -> aee36206-2846-4af8-97fc-c08ea32d04f7 -> Assistant -> fe5d834e-f4ba-4d75-a77b-b419a41172d6 -> Tool -> 3cc5cb2f-9bf2-4ec7-b730-4b7a6e37379d -> Assistant -> aaa2c0bf-efc0-41ea-9394-4821c3fecdd6 -> User -> 7770a31d-c47b-48a5-9a87-cd318296e663 -> Assistant -> 186f96c5-6c2e-4c78-90de-dfcc8ee777fc -> Tool -> c7e4a869-cad6-4bc6-8ce6-a57f1c21d6a5 -> Assistant -> aaa25436-2417-4590-99f2-b2c737ebd76e -> User -> 19cc38f8-b99d-499e-968a-3b533d806593 -> System -> 5827125a-b24e-4d18-86f6-470e815d7c30 -> Assistant -> 2514e975-d6c8-40fa-82d6-b29ba3ca3f5b -> Tool -> c413c192-dbfa-4cd5-b113-6201359a48c4 -> Assistant -> aaa26c46-7fbc-40e0-84af-8ed1af29aead -> User -> 506d9386-4909-4f98-b93b-918b5195353d -> Assistant -> 8d250109-2a1c-441d-ba2a-308f0a29d4ee -> Tool -> 3f71f78a-f0ab-414d-8582-4eb8ac0509a1 -> Assistant -> aaa2ffb7-f72c-40d5-966d-14e571c53329 -> User -> e807b595-379e-4edb-8fe6-eaa3da99bfe9 -> Assistant -> 1. `eval` and `exec` -> aaa25a0d-f0e8-4bd4-a669-466936b2c926 -> User -> a8b4ec28-b54d-42a8-9869-1f9003b5d03d -> Assistant -> 1. String Interpolation and Formatting -> 2. Template Engines -> 3. Abstract Syntax Trees (AST) -> 4. Code Objects -> 5. External Code Generators -> Considerations: -> aaa2160c-f02b-435f-b83d-e90262137062 -> User -> d53f0445-e6dd-4877-87d0-888ed58ebb6a -> Assistant -> Specialized Tools for Code Generation: -> aaa2e3d0-1e2b-4b68-8514-d4f950d30cc7 -> User -> 010a9d0b-ce90-4bf3-95b8-88e5ff084052 -> Assistant -> aaa21d32-d668-44ae-b08f-f222f44b4cd0 -> User -> a0cd3eb4-5990-44ff-9805-da6f97ff9893 -> Assistant
---
# Assistant

```python
from jinja2 import Environment, PackageLoader, select_autoescape

# Initialize Jinja2 environment
env = Environment(
    loader=PackageLoader('your_package', 'templates'),  # Replace 'your_package' and 'templates' with actual values
    autoescape=select_autoescape(['html', 'xml'])
)

# Sample templates for each type of node
basic_node_template = env.from_string("""
class {{ node.type }}:
    def __init__(self, named: bool):
        self.named = named
""")

child_type_template = env.from_string("""
{{ child_type.as_annotation() }}
""")

field_template = env.from_string("""
self.{{ field.key }}: {{ field.type.as_annotation() }}
""")

internal_node_template = env.from_string("""
class {{ node.type }}:
{% for field in node.fields %}
    {{ field.key }}: {{ field.type.as_annotation() }}
{% endfor %}
""")

supertype_node_template = env.from_string("""
class {{ node.type }}:
{% for subtype in node.subtypes %}
    {{ subtype.type }}
{% endfor %}
""")

# Function to render BasicNode
def render_basic_node(node: BasicNode) -> str:
    return basic_node_template.render(node=node)

# Function to render ChildType
def render_child_type(child_type: ChildType) -> str:
    return child_type_template.render(child_type=child_type)

# Function to render Field
def render_field(field: Field) -> str:
    return field_template.render(field=field)

# Function to render InternalNode
def render_internal_node(node: InternalNode) -> str:
    return internal_node_template.render(node=node)

# Function to render SupertypeNode
def render_supertype_node(node: SupertypeNode) -> str:
    return supertype_node_template.render(node=node)

# Test rendering a BasicNode
render_basic_node(BasicNode(type="TestBasic", named=True))
```

[child ⬇️](#f3b40fa7-3ee3-4a97-96eb-3ccf9fedc08b)

---

(main branch ⎇)
###### f3b40fa7-3ee3-4a97-96eb-3ccf9fedc08b
[parent ⬆️](#a0cd3eb4-5990-44ff-9805-da6f97ff9893)