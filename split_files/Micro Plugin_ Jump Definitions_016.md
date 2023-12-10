---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant
---
# Assistant

I apologize for the confusion. The error seems to indicate that something in line 2 of `JumpDefs.lua` is being called as if it were a function but isn't one. The most common issue related to this error in Micro's Lua plugins is the incorrect usage of the API.

The `AddRuntimeFile` function is generally used for defining syntax highlighting and key bindings, but it's not for binding Lua functions to key events directly within the plugin's `init` function. In Micro, you typically define the keybindings in the `bindings.json` file, as I previously mentioned.

If you still get an error, it might be helpful to see the actual code causing the error. Could you please share the contents of your `JumpDefs.lua` and `bindings.json` files? This would help me pinpoint the issue more accurately.

[child ⬇️](#aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5)

---

(main branch ⎇)
###### aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5
[parent ⬆️](#8726a647-85de-484c-a4a8-09246e56d7d3)
