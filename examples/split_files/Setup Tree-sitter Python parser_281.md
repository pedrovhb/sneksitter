# Assistant

```python
# Importing tsl from the setup_env module
from setup_env import tsl

# Re-initializing the parser and language objects
PY_LANGUAGE = tsl.get_language("python")
parser = tsl.get_parser("python")

# Parse the sample code to generate a syntax tree
sample_tree = parser.parse(bytes(sample_code, "utf8"))

# Create the query
query = PY_LANGUAGE.query(query_str)

# Capture the nodes
captures = query.captures(sample_tree.root_node)

# Display the captures
captures
```

[child ⬇️](#a96833d6-ebb1-48b2-a998-8d6841cfe142)

---

(other branch ⎇)
###### a96833d6-ebb1-48b2-a998-8d6841cfe142
[parent ⬆️](#c89b7049-1e92-4dc5-9e58-4bc4a94fd1d9)
