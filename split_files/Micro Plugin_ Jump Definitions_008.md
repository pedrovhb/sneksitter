---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant
---
# Assistant

Writing a plugin for the `micro` text editor to jump up and down across function or class definitions involves a few steps:

1. **Understand the Plugin API**: Micro's plugin API uses Lua. Familiarize yourself with the Lua language if you haven't already.

2. **Directory Structure**: Create a directory with the name of your plugin, e.g., `JumpDefs`. Inside this directory, create a `README.md` and a `.lua` file with the same name as the directory, i.e., `JumpDefs.lua`.

3. **Plugin Initialization**: Initialize your plugin by defining the `init()` function in the `.lua` file.

4. **Implement the Logic**: Implement the logic to jump across function or class definitions. You can use Micro's API functions like `CursorUp()`, `CursorDown()`, `GetActiveView()` to manipulate the cursor position and get the editor's current state.

5. **Key Binding**: Bind `Ctrl+Up` and `Ctrl+Down` to your functions. This will be done inside the `init()` function.

6. **Installation**: Move the plugin folder into `~/.config/micro/plug`.

Here is a rough outline of how your `JumpDefs.lua` might look like:

```lua
function init()
    -- Bind Ctrl+Up to the function 'jumpUp'
    BindKey("CtrlUp", "JumpDefs.jumpUp")
    -- Bind Ctrl+Down to the function 'jumpDown'
    BindKey("CtrlDown", "JumpDefs.jumpDown")
end

function isDefLine(line)
    -- Logic to check if the line is a function or class definition
    -- For example, in Python:
    return string.match(line, "^def ") or string.match(line, "^class ")
end

function jumpUp()
    local view = GetActiveView()
    local cursor = view.Cursor
    while cursor.Loc.Y > 0 do
        cursor:Up()
        local line = view.Buf:Line(cursor.Loc.Y)
        if isDefLine(line) then
            break
        end
    end
end

function jumpDown()
    local view = GetActiveView()
    local cursor = view.Cursor
    while cursor.Loc.Y < view.Buf.NumLines - 1 do
        cursor:Down()
        local line = view.Buf:Line(cursor.Loc.Y)
        if isDefLine(line) then
            break
        end
    end
end
```

In this outline:

- `init()` binds `Ctrl+Up` and `Ctrl+Down` to the `jumpUp()` and `jumpDown()` functions.
- `isDefLine()` checks if a given line is a class or function definition. This is a basic example; you might want a more robust implementation.
- `jumpUp()` and `jumpDown()` navigate up and down through the text buffer, stopping at function or class definitions.

To install the plugin, you can move your `JumpDefs` directory into the `~/.config/micro/plug` directory, and then enable it within Micro using `plugin install`.

Since you're on NixOS and likely familiar with Lua, this approach should be a good starting point. Feel free to adapt it to your specific needs.

[child ⬇️](#aaa28f27-4c2e-43e0-bd23-02e759e2a046)

---

(main branch ⎇)
###### aaa28f27-4c2e-43e0-bd23-02e759e2a046
[parent ⬆️](#55a82fb5-6597-4870-bc54-3f056fcc765d)
