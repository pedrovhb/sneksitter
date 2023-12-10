# Assistant

The debugging output shows that `extract_default` is called for a node of type `default_parameter`, but it fails to proceed further to capture the actual default value.

The issue seems to be that `extract_default` is not finding any child nodes that match the criteria for being a default value. Specifically, it seems that the child nodes of the type `default_parameter` or `typed_default_parameter` are not being properly identified or accessed.

I'll adjust the function to better capture these child nodes.

[child ⬇️](#70bec5e2-ec52-46f0-893b-59e56483fdff)

---

(main branch ⎇)
###### 70bec5e2-ec52-46f0-893b-59e56483fdff
[parent ⬆️](#42454858-fbb9-4574-b2f6-99577ce3da97)
