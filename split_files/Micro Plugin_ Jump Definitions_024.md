---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library -> Adding help files, syntax files, or colorschemes in your plugin -> Default plugins
---
## Default plugins

There are 6 default plugins that come pre-installed with micro. These are

* `autoclose`: automatically closes brackets, quotes, etc...
* `comment`: provides automatic commenting for a number of languages
* `ftoptions`: alters some default options (notably indentation) depending on the filetype
* `linter`: provides extensible linting for many languages
* `literate`: provides advanced syntax highlighting for the Literate
   programming tool.
* `status`: provides some extensions to the status line (integration with
   Git and more).
* `diff`: integrates the `diffgutter` option with Git. If you are in a Git
   directory, the diff gutter will show changes with respect to the most
   recent Git commit rather than the diff since opening the file.

See `> help linter`, `> help comment`, and `> help status` for additional
documentation specific to those plugins.

These are good examples for many use-cases if you are looking to write
your own plugins.

