---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library -> Adding help files, syntax files, or colorschemes in your plugin -> Default plugins -> Plugin Manager -> 4b434983-1975-4b4c-9096-c796fb2afd2b -> Assistant -> aaa29d93-dd8b-4642-876d-c0803d007f6f -> User -> 1493a977-cc93-4d9b-8394-90ae475b5153 -> Assistant
---
# Assistant

I apologize for the oversight. The error suggests that the `config` object is `nil`. This could be because the import statement for the `config` package is missing. In Micro's Lua plugins, you usually need to import packages explicitly.

Try adding this line at the top of your Lua script to import Micro's `config` package:

```lua
local config = import("micro/config")
```

So the corrected `JumpDefs.lua` would look something like this:

```lua
local config = import("micro/config")

function init()
    config.TryBindKey("CtrlUp", "JumpDefs.jumpUp", true)
    config.TryBindKey("CtrlDown", "JumpDefs.jumpDown", true)
end

function jumpUp(bp)
    -- ... (same as before)
end

function jumpDown(bp)
    -- ... (same as before)
end
```

This should fix the error you're encountering. Remember to reload the plugin or restart Micro to pick up the changes.

[child 1 ⬇️](#aaa22da2-5287-4b7a-b4f0-449a5a7a7211) | [child 2 ⬇️](#aaa23f15-a56c-4552-9dab-3f0098355286)

---

(other branch ⎇)
###### aaa22da2-5287-4b7a-b4f0-449a5a7a7211
[parent ⬆️](#1493a977-cc93-4d9b-8394-90ae475b5153)