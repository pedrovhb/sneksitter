---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library -> Adding help files, syntax files, or colorschemes in your plugin -> Default plugins -> Plugin Manager -> 4b434983-1975-4b4c-9096-c796fb2afd2b -> Assistant -> aaa29d93-dd8b-4642-876d-c0803d007f6f -> User -> 1493a977-cc93-4d9b-8394-90ae475b5153 -> Assistant -> aaa22da2-5287-4b7a-b4f0-449a5a7a7211 -> User -> d2577d1b-6f51-491d-8b98-200b7aa67ae8 -> Assistant
---
# Assistant

Certainly. A `repo.json` file typically contains metadata about your plugin, such as the name, description, website, and version information. Here's an example `repo.json` tailored for your JumpDefs plugin:

```json
{
  "Name": "JumpDefs",
  "Description": "A micro editor plugin to jump across function and class definitions.",
  "Website": "https://github.com/your_username/JumpDefs",
  "Tags": ["navigation", "code"],
  "Versions": [
    {
      "Version": "1.0.0",
      "Url": "https://github.com/your_username/JumpDefs/archive/v1.0.0.zip",
      "Require": {
        "micro": ">=2.0.0"
      }
    }
  ]
}
```

In this example:

- `"Name"` is the name of your plugin.
- `"Description"` briefly explains what the plugin does.
- `"Website"` is the URL where users can find more information about the plugin. Replace `your_username` with your GitHub username.
- `"Tags"` are keywords that help categorize the plugin.
- `"Versions"` is an array of version objects. Each object includes:
  - `"Version"`: The version number of this release.
  - `"Url"`: The URL where the zip archive of this version can be downloaded. Again, replace `your_username` with your GitHub username.
  - `"Require"`: Dependencies for the plugin. Here, it requires Micro version 2.0.0 or higher.

Please adjust the fields according to your plugin's actual details.

---

(main branch ⎇)
###### aaa23f15-a56c-4552-9dab-3f0098355286
[parent ⬆️](#1493a977-cc93-4d9b-8394-90ae475b5153)
