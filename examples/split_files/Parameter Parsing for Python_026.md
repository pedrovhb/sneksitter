# Assistant

With these utility functions in place, we can now work on implementing the `from_node` and `from_node_parameters` methods in the `Parameter` class. These methods will use the utility functions to extract the relevant details from tree-sitter nodes.

Here's how we will proceed:

1. **Implement `from_node`**: This will involve using the utility functions to populate a `Parameter` object.
2. **Implement `from_node_parameters`**: Here, we will loop through child nodes and call `from_node` on each, making adjustments based on the context of surrounding parameters.

Let's start by implementing `from_node`.

[child ⬇️](#708dd07b-a37a-4010-a6b3-443954d384ec)

---

(main branch ⎇)
###### 708dd07b-a37a-4010-a6b3-443954d384ec
[parent ⬆️](#e82533cc-5287-4d6c-ae8f-7ee2f25991c7)
