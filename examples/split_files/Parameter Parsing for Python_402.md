# Assistant

The `ValidationError` is caused because the name of the parameter is `None` for separators like `/` and `*`. Since the `name` field in the `Parameter` class is mandatory, this leads to a validation error.

To handle this, I'll skip adding such separators to the `parameters` list in the `from_node_parameters` method. Let me fix this.

[child ⬇️](#6345b2c5-052f-468d-b885-45d929cd3ce5)

---

(other branch ⎇)
###### 6345b2c5-052f-468d-b885-45d929cd3ce5
[parent ⬆️](#70a2b6d6-7443-4156-9620-6d1a8160a815)
