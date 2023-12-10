# Assistant

The debugging output confirms that `from_node` is invoking `extract_name` for a node of type `typed_parameter`. However, `extract_name` is failing to return the correct name when called in this context.

The most likely explanation is that the `extract_name` function is not navigating deep enough into the node tree to reach the `list_splat_pattern` node where the name `vararg` is located.

To resolve this, I'll modify `extract_name` to navigate into child nodes of type `list_splat_pattern` or `dictionary_splat_pattern` when it encounters a `typed_parameter` node.

[child ⬇️](#4afd4aff-8d28-4e3b-8cca-2b9bf5e75475)

---

(main branch ⎇)
###### 4afd4aff-8d28-4e3b-8cca-2b9bf5e75475
[parent ⬆️](#374df437-8398-4aba-af9f-9667f30a4e0c)
