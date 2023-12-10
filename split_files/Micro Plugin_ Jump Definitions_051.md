---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library -> Adding help files, syntax files, or colorschemes in your plugin -> Default plugins -> Plugin Manager -> 4b434983-1975-4b4c-9096-c796fb2afd2b -> Assistant -> aaa29d93-dd8b-4642-876d-c0803d007f6f -> User -> 1493a977-cc93-4d9b-8394-90ae475b5153 -> Assistant -> aaa22da2-5287-4b7a-b4f0-449a5a7a7211 -> User -> d2577d1b-6f51-491d-8b98-200b7aa67ae8 -> Assistant -> aaa23f15-a56c-4552-9dab-3f0098355286 -> User -> 78149733-8486-47b0-ac5b-a3168c040ea4 -> Assistant -> aaa25208-4813-436d-97a8-2b1e8577a6a3 -> User -> cab0d8b0-ffb6-421b-a14c-7008f19b69bc -> Assistant -> aaa2683a-56c9-4931-a410-60fd60be9003 -> User -> b49b7c06-6077-42fa-841c-1f1ee9077863 -> Assistant -> aaa22d32-edc4-4b28-ac03-cd576c14ea82 -> User -> f313744e-d56b-4898-8697-6de96941ecdb -> Assistant
---
# Assistant

The issue with `jumpDown` could be related to the buffer line indexing or the loop conditions. Let's add some debug logs to help identify where the issue might be occurring.

Modify your `jumpDown` function as follows:

```lua
function jumpDown(bp)
    local cursor = bp.Cursor
    local micro = import("micro")
    
    if cursor == nil then
        micro.Log("Cursor is nil")
        return
    end
    
    local numLines = bp.Buf.NumLines
    if numLines == nil then
        micro.Log("NumLines is nil")
        return
    end
    
    micro.Log("Starting from line: " .. cursor.Y)
    
    while cursor.Y < numLines - 1 do
        cursor:Down()
        local line = bp.Buf:Line(cursor.Y)
        
        if line == nil then
            micro.Log("Line is nil at Y: " .. cursor.Y)
            return
        end
        
        if string.match(line, "^def ") or string.match(line, "^class ") then
            micro.Log("Match found at line: " .. cursor.Y)
            break
        end
    end
end
```

In this modified version, I've added debug log statements using `micro.Log()`. After you reload the plugin and try using `jumpDown`, check the debug log by running `> log` in Micro's command prompt. This should give you more insights into where the problem might be occurring.

---

(other branch ⎇)
###### a962e220-fe10-45d7-9e6c-69c1a6e1bcda
[parent ⬆️](#aaa22d32-edc4-4b28-ac03-cd576c14ea82)
