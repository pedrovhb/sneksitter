# Assistant

The debugging output shows that `extract_name` is capable of correctly extracting the name `vararg` when directly applied to the `list_splat_pattern` node. This suggests that the issue lies in how `from_node` invokes `extract_name` or processes its returned value.

Let's debug `from_node` to get a better understanding of the problem.

[child ⬇️](#fe4906cc-b3a1-46e2-8417-5bd7f5cf467b)

---

(main branch ⎇)
###### fe4906cc-b3a1-46e2-8417-5bd7f5cf467b
[parent ⬆️](#c77124df-73e1-4913-a16a-9e01582222cc)
