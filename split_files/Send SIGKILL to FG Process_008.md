---
file: /home/pedro/Documents/chatgpt_export/Markdown/Send SIGKILL to FG Process.md
heading_stack: <root> -> 112df2cd-b2fe-46bf-9e30-383f7f8e4049 -> System -> 386e7010-f16e-4339-907d-8d9a3a5d53db -> System -> aaa212f3-f065-4575-8cf1-d234fce6838f -> User -> 9000801b-058b-4ea0-99a5-20af456aef74 -> Assistant
---
# Assistant

To send a `SIGKILL` to the foreground process in a Linux environment, you can use the `kill` command with the `-KILL` option, specifying the process ID (PID) of the foreground process.

1. **Find the PID**: Use `ps` or `top` to find the PID of the foreground process.
2. **Kill the Process**: Use `kill -9 <PID>` or `kill -KILL <PID>` to send `SIGKILL`.

However, if you're in the same terminal where the process is running in the foreground, you can usually use the following shortcut:

- Press `Ctrl + Z` to suspend the process and put it in the background.
- Execute `kill -9 %%` to send a `SIGKILL` to the last process put into the background (which would be your foreground process).

Would you like to see a code snippet to programmatically achieve this in Python?

[child ⬇️](#aaa27e15-7128-4628-8ad3-68aa0d7b08df)

---

(main branch ⎇)
###### aaa27e15-7128-4628-8ad3-68aa0d7b08df
[parent ⬆️](#9000801b-058b-4ea0-99a5-20af456aef74)
