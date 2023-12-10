# Assistant

The output indicates that the parsing is not correct. Several attributes such as `name`, `type`, and `default` are not being populated as expected. Additionally, there are empty `Parameter` objects, suggesting that not all child nodes should be treated as parameters.

The issue likely lies in the `from_node_parameters` method where it loops through each child of the `parameters` node without filtering out irrelevant nodes. Also, the utility functions for extracting name, type, and default values may need further refinement to correctly dig into the tree structure.

I'll proceed to debug these issues.

[child ⬇️](#ebafe23c-ad38-4f4e-b8ef-f3001ba60002)

---

(main branch ⎇)
###### ebafe23c-ad38-4f4e-b8ef-f3001ba60002
[parent ⬆️](#25e80099-dabc-4d84-90fd-d5f29f4a6133)
