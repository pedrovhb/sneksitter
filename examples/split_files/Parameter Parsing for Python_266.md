# Assistant

The parsing now correctly captures the default value for the parameter `f`, which is `"a string default"`.

However, for the parameter `w`, the default value is still incorrect; it captures `Callable[P, T]`, which is actually the type annotation. This likely happened because the default value for `w` is an identifier (`print`), and the `extract_default` function needs to be adjusted to account for this.

I'll go ahead and fix this in the `extract_default` function.

[child ⬇️](#28d08a91-f7e0-4e7c-be45-eac28591ca40)

---

(main branch ⎇)
###### 28d08a91-f7e0-4e7c-be45-eac28591ca40
[parent ⬆️](#6a5fe403-0e5e-4f87-8de4-a3d4e68448f9)
