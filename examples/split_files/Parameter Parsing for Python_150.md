# Assistant

The `print_tree` output reveals the internal structure of the `typed_parameter` node for `*vararg`. It has a `list_splat_pattern` child node, which in turn has an `identifier` child node containing the name `vararg`.

Given this structure, the `extract_name` function should theoretically be able to capture the name, especially when considering `list_splat_pattern` and its `identifier` child node.

The issue might be in how the text content of these nodes is being accessed. I'll debug the `extract_name` function again with this new insight.

[child ⬇️](#ff98c37b-021b-4b9d-8d41-3ce7ef489027)

---

(main branch ⎇)
###### ff98c37b-021b-4b9d-8d41-3ce7ef489027
[parent ⬆️](#2dc33a97-ded4-4aba-97d6-b2ff53b72132)
