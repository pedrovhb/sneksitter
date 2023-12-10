# Assistant

The `typed_default_parameter` node for the parameter `z: int=5` has three child nodes:

1. `identifier`: Represents the name of the parameter (`z` in this case)
2. `type`: Represents the type annotation (`int` in this case)
3. `integer`: Represents the default value (`5` in this case)

Given this structure, it's clear that the `extract_default` function should be capable of capturing the correct default value (`5`).

The issue seems to arise from the way `extract_default` is handling the children of `typed_default_parameter` nodes. I'll go ahead and adjust the function to fix this.

[child ⬇️](#07c939d7-b376-4d1a-8f20-828b513768cc)

---

(main branch ⎇)
###### 07c939d7-b376-4d1a-8f20-828b513768cc
[parent ⬆️](#b43f61fe-baec-46d1-a187-0c5c3b6d3820)
