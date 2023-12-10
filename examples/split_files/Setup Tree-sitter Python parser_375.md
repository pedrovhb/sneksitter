# Tool

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[37], line 22
      1 decorator_sample_code = '''
      2 @simple_decorator
      3 def simple_func():
   (...)
     18     pass
     19 '''
     21 # Parse the sample code
---> 22 decorator_sample_tree = py_parser.parse(bytes(decorator_sample_code, "utf8"))
     24 # Visualize the tree structure
     25 print_tree(decorator_sample_tree.root_node)

NameError: name 'py_parser' is not defined

```

[child ⬇️](#beeea022-f1ef-409c-b303-842b3b7fe6a7)

---

(main branch ⎇)
###### beeea022-f1ef-409c-b303-842b3b7fe6a7
[parent ⬆️](#8f7d280f-73f1-4724-8bfb-535379c84eae)
