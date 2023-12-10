---
file: /home/pedro/Documents/chatgpt_export/Markdown/Send SIGKILL to FG Process.md
heading_stack: <root> -> 112df2cd-b2fe-46bf-9e30-383f7f8e4049 -> System -> 386e7010-f16e-4339-907d-8d9a3a5d53db -> System -> aaa212f3-f065-4575-8cf1-d234fce6838f -> User -> 9000801b-058b-4ea0-99a5-20af456aef74 -> Assistant -> aaa27e15-7128-4628-8ad3-68aa0d7b08df -> User -> 5e3167a6-6934-4df9-a983-a933af506c21 -> Assistant
---
# Assistant

In the Fish shell, the process to send a `SIGKILL` to a foreground process is similar to that in other shells like Bash. Here's how you can do it:

1. **Suspend the Process**: Press `Ctrl + Z` to suspend the foreground process and put it in the background.
2. **Kill the Process**: Use `kill -KILL %1` to send a `SIGKILL` to the job with job ID 1 (which is usually the most recently suspended job).

In Fish, job IDs are used to refer to background jobs, and you can list them with the `jobs` command. The `%1`, `%2`, etc. are job specifiers that you can use in commands like `kill`.

So, the sequence in Fish would be `Ctrl + Z` followed by `kill -KILL %1`.

[child ⬇️](#aaa2d27d-0bdf-4d37-a2a8-871ee9020379)

---

(main branch ⎇)
###### aaa2d27d-0bdf-4d37-a2a8-871ee9020379
[parent ⬆️](#5e3167a6-6934-4df9-a983-a933af506c21)
