# Assistant

The child nodes include various types such as `typed_parameter`, `identifier`, `default_parameter`, etc., as well as separators like `(`, `)`, and `,`. These separators and other non-parameter nodes are being incorrectly treated as parameters.

The immediate steps to correct this are:
1. Filter out irrelevant nodes when looping through the children in `from_node_parameters`.
2. Modify the utility functions to better target the right sub-nodes.

Let's start by implementing these changes.

[child ⬇️](#09c8e042-b8b8-4ef8-8cdb-84825e97ec17)

---

(main branch ⎇)
###### 09c8e042-b8b8-4ef8-8cdb-84825e97ec17
[parent ⬆️](#037a7534-304d-416b-8105-62769874266d)
