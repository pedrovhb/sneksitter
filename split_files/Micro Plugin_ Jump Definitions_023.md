---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library -> Adding help files, syntax files, or colorschemes in your plugin
---
## Adding help files, syntax files, or colorschemes in your plugin

You can use the `AddRuntimeFile(name string, type config.RTFiletype,
                                path string)`
function to add various kinds of files to your plugin. For example, if you'd
like to add a help topic to your plugin called `test`, you would create a
`test.md` file, and call the function:

```lua
config = import("micro/config")
config.AddRuntimeFile("test", config.RTHelp, "test.md")
```

Use `AddRuntimeFilesFromDirectory(name, type, dir, pattern)` to add a number of
files to the runtime. To read the content of a runtime file use
`ReadRuntimeFile(fileType, name string)` or `ListRuntimeFiles(fileType string)`
for all runtime files. In addition, there is `AddRuntimeFileFromMemory` which
adds a runtime file based on a string that may have been constructed at
runtime.

