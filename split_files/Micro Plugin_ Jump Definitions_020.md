---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks
---
## Lua callbacks

Plugins use Lua but also have access to many functions both from micro
and from the Go standard library. Many callbacks are also defined which
are called when certain events happen. Here is the list of callbacks
which micro defines:

* `init()`: this function should be used for your plugin initialization.
   This function is called after buffers have been initialized.

* `preinit()`: initialization function called before buffers have been
   initialized.

* `postinit()`: initialization function called after `init()`.

* `onSetActive(bufpane)`: runs when changing the currently active panel.

* `onBufferOpen(buf)`: runs when a buffer is opened. The input contains
   the buffer object.

* `onBufPaneOpen(bufpane)`: runs when a bufpane is opened. The input
   contains the bufpane object.

* `onAction(bufpane)`: runs when `Action` is triggered by the user, where
   `Action` is a bindable action (see `> help keybindings`). A bufpane
   is passed as input and the function should return a boolean defining
   whether the view should be relocated after this action is performed.

* `preAction(bufpane)`: runs immediately before `Action` is triggered
   by the user. Returns a boolean which defines whether the action should
   be canceled.

* `onRune(rune)`: runs when the composed rune has been inserted

* `preRune(rune)`: runs before the composed rune will be inserted

For example a function which is run every time the user saves the buffer
would be:

```lua
function onSave(bp)
    ...
    return false
end
```

The `bp` variable is a reference to the bufpane the action is being executed
within.  This is almost always the current bufpane.

All available actions are listed in the keybindings section of the help.

These functions should also return a boolean specifying whether the bufpane
should be relocated to the cursor or not after the action is complete.

