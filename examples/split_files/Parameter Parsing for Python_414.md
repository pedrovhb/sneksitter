# Assistant

It looks like the issue still persists. On closer inspection, it seems I didn't remove the redundant check for separators, which was supposed to be skipped.

Let's refine the `from_node_parameters` method to carefully handle such cases and rerun the tests.

[child ⬇️](#86f42684-1e10-4ddc-a2bc-71f75d52d49a)

---

(other branch ⎇)
###### 86f42684-1e10-4ddc-a2bc-71f75d52d49a
[parent ⬆️](#7867c704-3df5-4d5e-adea-dcf18f022864)
