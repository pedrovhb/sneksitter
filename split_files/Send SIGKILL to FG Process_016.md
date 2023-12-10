---
file: /home/pedro/Documents/chatgpt_export/Markdown/Send SIGKILL to FG Process.md
heading_stack: <root> -> 112df2cd-b2fe-46bf-9e30-383f7f8e4049 -> System -> 386e7010-f16e-4339-907d-8d9a3a5d53db -> System -> aaa212f3-f065-4575-8cf1-d234fce6838f -> User -> 9000801b-058b-4ea0-99a5-20af456aef74 -> Assistant -> aaa27e15-7128-4628-8ad3-68aa0d7b08df -> User -> 5e3167a6-6934-4df9-a983-a933af506c21 -> Assistant -> aaa2d27d-0bdf-4d37-a2a8-871ee9020379 -> User -> bcc0b815-a442-4075-82e5-a95fb8079533 -> Assistant
---
# Assistant

In the Fish shell, jobs are tasks that are either running in the background or have been suspended. This job control feature is particularly useful for multitasking within a single terminal session. Here's a breakdown of how jobs work in Fish and what you can do with them:

### Job Control Commands

1. **Suspend a Job**: `Ctrl + Z`  
   Suspend the current foreground job and move it to the background as a suspended job.

2. **List Jobs**: `jobs`  
   List all background and suspended jobs with their job IDs.

3. **Foreground a Job**: `fg %<job_id>`  
   Bring a background or suspended job to the foreground.

4. **Background a Job**: `bg %<job_id>`  
   Resume a suspended job in the background.

5. **Kill a Job**: `kill -<signal> %<job_id>`  
   Send a signal to a job. For example, `kill -KILL %1` sends `SIGKILL` to the job with ID 1.

6. **Disown a Job**: `disown %<job_id>`  
   Remove a job from the shell's job table, usually to prevent it from being terminated when the shell exits.

### Job Specifiers

- `%1`, `%2`, etc.: Refer to jobs by their job ID.
- `%%` or `%+`: Refer to the current job.
- `%-`: Refer to the previous job.

### Examples

1. **Run a job in the background**:  
   ```fish
   command &
   ```

2. **List background jobs**:  
   ```fish
   jobs
   ```

3. **Bring a job to the foreground**:  
   ```fish
   fg %1
   ```

4. **Send a job to the background**:  
   ```fish
   bg %1
   ```

5. **Kill a job**:  
   ```fish
   kill -KILL %1
   ```

6. **Disown a job**:  
   ```fish
   disown %1
   ```

In summary, job control in Fish allows you to manage multiple processes more effectively within a single terminal. This includes running, suspending, resuming, and terminating jobs either in the foreground or the background.

---
