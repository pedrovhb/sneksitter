---
file: /home/pedro/Documents/chatgpt_export/Markdown/Improve MPV Video Playback.md
heading_stack: <root> -> d72f2381-cacf-4cbe-9d00-2988b793abc3 -> System -> 95c09f59-8b0e-4edc-b0dd-971bed8c2aac -> System -> aaa2efe2-35da-40e0-9038-4d87d09532da -> User -> 785653dd-b9e0-47a8-951c-58227314c9a1 -> Assistant -> 1. Update Drivers -> 2. MPV Configuration
---
### 2. MPV Configuration
Create or edit the `mpv.conf` file in `~/.config/mpv/` to include performance-boosting settings. Here are some options to consider:

```text
# Use a hardware decoder if possible
hwdec=auto-safe

# Make use of multiple cores
vd-lavc-threads=4

# Video output options to tweak performance
vo=gpu

# Frame drop settings
framedrop=vo

# Cache settings
cache=yes
cache-secs=30
```

