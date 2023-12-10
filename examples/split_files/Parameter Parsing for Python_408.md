# Assistant

It seems the issue persists. I attempted to skip parameters with `None` names after instantiation, but the validation error occurs during the instantiation process itself.

A better approach might be to directly check if the node is a separator before even attempting to instantiate a `Parameter` object. Let's implement this change.

[child ⬇️](#32c81f0b-3c93-45fe-8a5b-2d9dd95da0d5)

---

(other branch ⎇)
###### 32c81f0b-3c93-45fe-8a5b-2d9dd95da0d5
[parent ⬆️](#8a82996c-f0c0-43f2-b046-548f1621339c)
