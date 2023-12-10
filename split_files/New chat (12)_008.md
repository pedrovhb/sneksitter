---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (12).md
heading_stack: <root> -> 3f06e865-c897-4a4b-a927-9de3232050cd -> System -> b071c1f2-263c-4341-9590-5213dca53085 -> System -> aaa2b49a-84e1-4810-bb7b-b731b4e96f38 -> User -> 841e4077-bd78-480f-814b-b79a9a92e559 -> Assistant
---
# Assistant

To get keyframes every \( N \) seconds from a video given a URL, without downloading the full video, you can use FFmpeg's `-ss` and `-frames:v` options in conjunction with `-vf "select=eq(pict_type\,PICT_TYPE_I)"` to extract keyframes. The `-ss` option seeks to a given time in the input, and `-frames:v` specifies the number of video frames to output. The `-vf "select=eq(pict_type\,PICT_TYPE_I)"` filter ensures that only keyframes (I-frames) are selected.

Here's a general outline of the steps involved:

1. Probe the video to get its duration and other metadata.
2. Calculate the timestamps where keyframes should be extracted.
3. Run FFmpeg commands to extract keyframes at those timestamps.

### Step 1: Probe Video for Duration

Firstly,

[child ⬇️](#aaa28510-70e7-4b0a-b4b4-43752da44402)

---

(other branch ⎇)
###### aaa28510-70e7-4b0a-b4b4-43752da44402
[parent ⬆️](#841e4077-bd78-480f-814b-b79a9a92e559)
