# Re-run the test for the Function model using the existing parser object
tree = parser.parse(bytes(test_code, 'utf8'))
root_node = tree.root_node
function_node = [n for n in root_node.children if n.type == 'function_definition'][0]

parsed_function = Function.from_node(function_node)
parsed_function.dict()
== Output ==
```
{ 'ename': 'AttributeError',
  'evalue': "'NoneType' object has no attribute 'decode'"}
```



[child ⬇️](#2364bbca-13fe-4b3f-8b43-cbc518b112b8)

---

(main branch ⎇)
###### 2364bbca-13fe-4b3f-8b43-cbc518b112b8
[parent ⬆️](#0984e606-f068-488f-8e66-be8faa5e434f)
