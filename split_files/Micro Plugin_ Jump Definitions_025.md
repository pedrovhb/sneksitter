---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library -> Adding help files, syntax files, or colorschemes in your plugin -> Default plugins -> Plugin Manager
---
## Plugin Manager

Micro also has a built in plugin manager which you can invoke with the
`> plugin ...` command, or in the shell with `micro -plugin ...`.

For the valid commands you can use, see the `commands` help topic.

The manager fetches plugins from the channels (which is simply a list of plugin
metadata) which it knows about. By default, micro only knows about the official
channel which is located at github.com/micro-editor/plugin-channel but you can
add your own third-party channels using the `pluginchannels` option and you can
directly link third-party plugins to allow installation through the plugin
manager with the `pluginrepos` option.

If you'd like to publish a plugin you've made as an official plugin, you should
upload your plugin online (to Github preferably) and add a `repo.json` file.
This file will contain the metadata for your plugin. Here is an example:

```json
[{
  "Name": "pluginname",
  "Description": "Here is a nice concise description of my plugin",
  "Website": "https://github.com/user/plugin",
  "Tags": ["python", "linting"],
  "Versions": [
    {
      "Version": "1.0.0",
      "Url": "https://github.com/user/plugin/archive/v1.0.0.zip",
      "Require": {
        "micro": ">=1.0.3"
      }
    }
  ]
}]
```

Then open a pull request at github.com/micro-editor/plugin-channel adding a
link to the raw `repo.json` that is in your plugin repository.

To make updating the plugin work, the first line of your plugins lua code
should contain the version of the plugin. (Like this: `VERSION = "1.0.0"`)
Please make sure to use [semver](http://semver.org/) for versioning.

[child ⬇️](#4b434983-1975-4b4c-9096-c796fb2afd2b)

---

(main branch ⎇)
###### 4b434983-1975-4b4c-9096-c796fb2afd2b
[parent ⬆️](#aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5)
