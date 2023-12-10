---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant
---
# Assistant

The error suggests that there's an issue with calling a non-function object on line 3 of your `JumpDefs.lua` file. The most likely culprit is the `BindKey` function. In the `micro` text editor, key binding is usually done via the `AddRuntimeFile` function, which adds your bindings to a specific event "runtime".

Here's how to correctly initialize your key bindings:

1. **Create a `bindings.json` file**: In your `JumpDefs` directory, create a new file named `bindings.json`.

2. **Add Key Bindings**: In `bindings.json`, add the following content:

```json
{
    "CtrlUp": "init.lua:JumpDefs.jumpUp",
    "CtrlDown": "init.lua:JumpDefs.jumpDown"
}
```

3. **Modify `init()` function**: In your `JumpDefs.lua` file, modify the `init()` function as follows:

```lua
function init()
    AddRuntimeFile("JumpDefs", "help", "README.md")
    AddRuntimeFile("JumpDefs", "keymap", "bindings.json")
end
```

Now, your `JumpDefs` folder should contain:

- `JumpDefs.lua` (your main Lua script)
- `README.md` (your readme file)
- `bindings.json` (your key bindings)

Make sure to reload the plugin or restart `micro` to apply the changes.

Would you like to proceed with troubleshooting or explore any specific parts of the code further?

[child ⬇️](#aaa22449-e24e-47d9-8610-6cdba5cba27e)

---

(main branch ⎇)
###### aaa22449-e24e-47d9-8610-6cdba5cba27e
[parent ⬆️](#13728b7a-2735-4e1d-9a06-14e6d8e00587)
