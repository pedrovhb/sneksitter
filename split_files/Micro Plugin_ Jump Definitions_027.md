---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library -> Adding help files, syntax files, or colorschemes in your plugin -> Default plugins -> Plugin Manager -> 4b434983-1975-4b4c-9096-c796fb2afd2b -> Assistant
---
# Assistant

Thank you for sharing the documentation. It provides a comprehensive overview of how Micro's plugin system works, the Lua callbacks, and the Go standard library functions that can be accessed. Let's address the issue you've experienced:

The error you're encountering—`attempt to call a non-function object`—usually indicates that you're trying to call something that Lua doesn't recognize as a callable object.

In the context of Micro, the issue could be with how you're trying to bind keys or manipulate internal structures. Based on the documentation you've provided, you should use the `init()` function for your plugin initialization, where you'd likely also set up your key bindings.

Here's a revised example with a focus on the Micro API:

```lua
function init()
    -- Initialize your plugin here.
    -- Key bindings could be set up here using Micro's API.
    config.TryBindKey("CtrlUp", "JumpDefs.jumpUp", true)
    config.TryBindKey("CtrlDown", "JumpDefs.jumpDown", true)
end

function jumpUp(bp)
    local cursor = bp.Cursor
    while cursor.Y > 0 do
        cursor:Up()
        local line = bp.Buf:Line(cursor.Y)
        if string.match(line, "^def ") or string.match(line, "^class ") then
            break
        end
    end
    return false
end

function jumpDown(bp)
    local cursor = bp.Cursor
    while cursor.Y < bp.Buf.NumLines - 1 do
        cursor:Down()
        local line = bp.Buf:Line(cursor.Y)
        if string.match(line, "^def ") or string.match(line, "^class ") then
            break
        end
    end
    return false
end
```

In this code snippet:

- `config.TryBindKey` is used to bind keys. The third argument specifies whether to overwrite existing bindings.
- `jumpUp` and `jumpDown` functions are defined as per Micro's API. They take a `BufPane` object `bp` as an argument.
- The functions return `false`, meaning the `BufPane` shouldn't be relocated to the cursor after the action is complete.

Make sure to place this code in a `.lua` file within your plugin directory, and add an appropriate `repo.json` as per Micro's documentation. After that, you should be able to load your plugin via Micro's plugin manager.

Given your expertise in software engineering, this should provide a more accurate starting point tailored to Micro's API and Lua capabilities. Feel free to adjust and extend it as needed.

[child ⬇️](#aaa29d93-dd8b-4642-876d-c0803d007f6f)

---

(main branch ⎇)
###### aaa29d93-dd8b-4642-876d-c0803d007f6f
[parent ⬆️](#4b434983-1975-4b4c-9096-c796fb2afd2b)
