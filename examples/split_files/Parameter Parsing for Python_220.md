# Assistant

The `typed_default_parameter` node for the parameter `w: Callable[P, T]=print` has the following child nodes:

1. `identifier`: Represents the name of the parameter (`w` in this case)
2. `type`: Represents the type annotation (`Callable[P, T]` in this case)
3. `identifier`: Represents the default value (`print` in this case)

Given this structure, the issue seems to be that the `extract_default` function is not correctly identifying the child node that represents the default value when the type annotation has child nodes itself (as in `Callable[P, T]`).

I'll go ahead and fix this in the `extract_default` function.

[child ⬇️](#78bc1e31-eb8a-4831-9c6b-4b07a6a85882)

---

(main branch ⎇)
###### 78bc1e31-eb8a-4831-9c6b-4b07a6a85882
[parent ⬆️](#a8d5b1c0-871a-45ff-a923-47c52f9e1d24)
