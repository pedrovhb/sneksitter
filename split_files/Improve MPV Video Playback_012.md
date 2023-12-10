---
file: /home/pedro/Documents/chatgpt_export/Markdown/Improve MPV Video Playback.md
heading_stack: <root> -> d72f2381-cacf-4cbe-9d00-2988b793abc3 -> System -> 95c09f59-8b0e-4edc-b0dd-971bed8c2aac -> System -> aaa2efe2-35da-40e0-9038-4d87d09532da -> User -> 785653dd-b9e0-47a8-951c-58227314c9a1 -> Assistant -> 1. Update Drivers -> 2. MPV Configuration -> 3. Disable V-Sync -> 4. Run MPV with High Priority
---
### 4. Run MPV with High Priority
You can set MPV to run with higher priority to ensure it gets more CPU time.

#### For Linux:

```bash
nice -n -20 mpv <file_name>
```

