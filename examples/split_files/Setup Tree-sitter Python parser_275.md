# Assistant

```python
# Importing the setup_env module to initialize the environment
import setup_env

# Re-initializing the parser and language objects
PY_LANGUAGE = setup_env.tsl.get_language("python")
parser = setup_env.tsl.get_parser("python")

# Parse the sample code to generate a syntax tree
sample_tree = parser.parse(bytes(sample_code, "utf8"))

# Creating the query
query = PY_LANGUAGE.query(query_str)

# Capturing the nodes
captures = query.captures(sample_tree.root_node)

# Displaying the captures
captures
```

[child ⬇️](#ec160e42-1f13-45b9-beee-988d7076c36e)

---

(other branch ⎇)
###### ec160e42-1f13-45b9-beee-988d7076c36e
[parent ⬆️](#3144f0d0-7ec0-40ae-8bf1-2d629f73f14d)
