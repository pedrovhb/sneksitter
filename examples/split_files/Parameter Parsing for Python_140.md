# Assistant

As we can see, the `from_node` method is being called for a node of type `typed_parameter`, which is what we expect for the `*vararg` parameter. However, the name is still not being captured.

Since the issue persists, let's debug the `extract_name` function specifically for the `*vararg` node to understand what's going wrong there.

[child 1 ⬇️](#4781fbd3-d5a1-49a2-996d-2a2237130d8a) | [child 2 ⬇️](#aaa2993a-f7d3-40b4-9bd0-b7c2885e48a1)

---

(other branch ⎇)
###### 4781fbd3-d5a1-49a2-996d-2a2237130d8a
[parent ⬆️](#b373b8fe-e85a-42b2-86c4-c7c212d597e7)
