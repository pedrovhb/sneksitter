# Let's print the children of the function_node to understand its structure.
print([child for child in function_node.children])
== Output ==
[<Node type="def", start_point=(1, 0), end_point=(1, 3)>, <Node type=identifier, start_point=(1, 4), end_point=(1, 20)>,
 <Node type=parameters, start_point=(1, 20), end_point=(1, 58)>, <Node type="->", start_point=(1, 59), end_point=(1, 61)
>, <Node type=type, start_point=(1, 62), end_point=(1, 66)>, <Node type=":", start_point=(1, 66), end_point=(1, 67)>, <N
ode type=block, start_point=(2, 4), end_point=(3, 25)>]


[child ⬇️](#bd7bca67-92d2-4c74-94d1-61ddafc4e0a5)

---

(main branch ⎇)
###### bd7bca67-92d2-4c74-94d1-61ddafc4e0a5
[parent ⬆️](#21b2506b-c068-42f2-9a7c-4a52b79b3621)
