# Assistant

```python
# Sample Python code with various function decorators
decorator_sample_code = '''
@simple_decorator
def simple_func():
    pass

@decorator_with_args("arg1", 2)
def func_with_args():
    pass

@decorator1
@decorator2
def multiple_decorators():
    pass

@decorator_with_args("arg1", 2)
@simple_decorator
def multiple_decorators_mixed():
    pass
'''

# Parse the sample code
decorator_sample_tree = py_parser.parse(bytes(decorator_sample_code, "utf8"))

# Visualize the tree structure
print_tree(decorator_sample_tree.root_node)
```

[child ⬇️](#8f7d280f-73f1-4724-8bfb-535379c84eae)

---

(main branch ⎇)
###### 8f7d280f-73f1-4724-8bfb-535379c84eae
[parent ⬆️](#44e95c17-b10b-4c51-94e4-bd0dfda03f61)
