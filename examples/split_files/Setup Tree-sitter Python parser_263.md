# Tool

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[10], line 9
      1 query_str = """
      2 (
      3   (function_definition) @function.def
      4   (class_definition) @class.def
      5 )
      6 """
      8 # Creating the query
----> 9 query = PY_LANGUAGE.query(query_str)
     11 # Capturing the nodes
     12 captures = query.captures(sample_tree.root_node)

NameError: name 'PY_LANGUAGE' is not defined

```

[child ⬇️](#13513505-fcd4-4087-9b83-99a1065db33f)

---

(other branch ⎇)
###### 13513505-fcd4-4087-9b83-99a1065db33f
[parent ⬆️](#e2057ad5-a5e3-4792-bcb4-d1029ac213b4)
