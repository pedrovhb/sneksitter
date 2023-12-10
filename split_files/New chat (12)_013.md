---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (12).md
heading_stack: <root> -> 3f06e865-c897-4a4b-a927-9de3232050cd -> System -> b071c1f2-263c-4341-9590-5213dca53085 -> System -> aaa2b49a-84e1-4810-bb7b-b731b4e96f38 -> User -> 841e4077-bd78-480f-814b-b79a9a92e559 -> Assistant -> Step 1: Probe Video for Duration -> aaa28510-70e7-4b0a-b4b4-43752da44402 -> User -> 5959d47b-4592-4d1b-8ad4-07096d9c5fcf -> Assistant
---
# Assistant

If you're looking to get keyframes every \( N \) seconds from a video URL without downloading the full video in a single command, you can use FFmpeg with a combination of its options. Specifically, the `-ss` option to specify the starting point, the `-vf "select=eq(pict_type\,PICT_TYPE_I)"` filter to select keyframes, and the `-an` option to skip audio can be useful.

Here's a generic FFmpeg command that would do this:

```bash
ffmpeg -ss [start_time] -i [URL] -vf "select=eq(pict_type\,PICT_TYPE_I)" -vsync vfr -an -r 1/[N] keyframe_%03d.png
```

- `[start_time]`: Time to start the video. Usually set this to 0 to start at the beginning.
- `[URL]`: The video URL.
- `[N]`: Number of seconds between each keyframe you want to extract.

To get keyframes every 5 seconds from a video starting at the beginning, you can modify the command as follows:

```bash
ffmpeg -ss 0 -i [URL] -vf "select=eq(pict_type\,PICT_TYPE_I)" -vsync vfr -an -r 1/5 keyframe_%03d.png
```

**Note**: Replace `[URL]` with the actual video URL.

This command works by decoding the video stream but only keeping keyframes, which are then output at a rate of one every \( N \) seconds. 

Keep in mind that this method still requires FFmpeg to process the video, so the video data will be streamed, but not stored in its entirety. Would you like to proceed with this approach in Python using `asyncio` for subprocess handling?

[child ⬇️](#aaa20452-6339-498f-a308-f7809045dac3)

---

(other branch ⎇)
###### aaa20452-6339-498f-a308-f7809045dac3
[parent ⬆️](#5959d47b-4592-4d1b-8ad4-07096d9c5fcf)
