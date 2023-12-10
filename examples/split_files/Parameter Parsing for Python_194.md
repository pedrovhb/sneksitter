# Assistant

The adjustments to `extract_default` have resolved the issue with the `default` attribute for parameters with default values like `y=1` and `f="a string default"`.

However, there's a new issue: the `default` attribute for parameters `z` and `w` is capturing their type annotations instead of the actual default values. 

I'll go ahead and fix this next.

[child ⬇️](#9e02be39-2e7d-40c6-9608-567daca6cba6)

---

(main branch ⎇)
###### 9e02be39-2e7d-40c6-9608-567daca6cba6
[parent ⬆️](#167d7e1a-b57b-4bb2-b45b-892bb00df0d9)
