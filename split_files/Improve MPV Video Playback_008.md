---
file: /home/pedro/Documents/chatgpt_export/Markdown/Improve MPV Video Playback.md
heading_stack: <root> -> d72f2381-cacf-4cbe-9d00-2988b793abc3 -> System -> 95c09f59-8b0e-4edc-b0dd-971bed8c2aac -> System -> aaa2efe2-35da-40e0-9038-4d87d09532da -> User -> 785653dd-b9e0-47a8-951c-58227314c9a1 -> Assistant
---
# Assistant

To make MPV play 1080p videos without stuttering on a system with Intel/NVIDIA drivers, you can try the following approaches:

### 1. Update Drivers
Firstly, make sure your Intel and NVIDIA drivers are up-to-date. On NixOS, you can do this by updating your system or modifying your `configuration.nix` to include the latest driver versions and then rebuilding.

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

### 3. Disable V-Sync
Disabling V-Sync in the NVIDIA control panel or Intel Graphics Command Center might help improve performance. 

### 4. Run MPV with High Priority
You can set MPV to run with higher priority to ensure it gets more CPU time.

#### For Linux:

```bash
nice -n -20 mpv <file_name>
```

### 5. Troubleshoot with Logs
Run MPV from the terminal with verbose logs to look for any issues:

```bash
mpv --log-file=mpv.log <file_name>
```

### 6. Profile System
Monitor system resources while playing the video to see if CPU, GPU, or memory is bottlenecking performance.

#### For Linux:

```bash
htop
nvidia-smi
```

By following these steps, you should be able to achieve smoother playback. If issues persist, further debugging will be needed based on logs and system profiling.

---
