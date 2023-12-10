# Assistant

Even after using `named_children`, the issue with the `name` attribute for the `*vararg` parameter remains. Given that the method is supposed to be more accurate, this suggests that the problem might lie elsewhere, possibly in how the `from_node` method processes the nodes before calling `extract_name`.

Let's debug the `from_node` method to see what's happening there.

[child ⬇️](#ba03b7bd-581d-4aed-876c-a112859d8888)

---

(main branch ⎇)
###### ba03b7bd-581d-4aed-876c-a112859d8888
[parent ⬆️](#46680d74-ef30-4c83-8b5c-a1f4c8e4ffdc)
