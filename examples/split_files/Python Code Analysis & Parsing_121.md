# Let's print the individual components to understand where the issue is.
print('Name:', extract_name(node.children_by_field_name('name')[0]))
print('Parameters Node:', node.children_by_field_name('parameters')[0])
print('Return Type Node:', node.children_by_field_name('return_type'))
print('Docstring Node:', node.children_by_field_name('docstring'))
print('Body Node:', node.children_by_field_name('body')[0])
== Output ==
```
{'ename': 'NameError', 'evalue': "name 'node' is not defined"}
```



[child ⬇️](#d3683a45-1bd7-4808-bdfa-c10cb154a203)

---

(main branch ⎇)
###### d3683a45-1bd7-4808-bdfa-c10cb154a203
[parent ⬆️](#5e0a4f78-25cd-4868-ae0b-559f12970349)
