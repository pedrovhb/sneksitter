---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (12).md
heading_stack: <root> -> 3f06e865-c897-4a4b-a927-9de3232050cd -> System -> b071c1f2-263c-4341-9590-5213dca53085 -> System -> aaa2b49a-84e1-4810-bb7b-b731b4e96f38 -> User -> 841e4077-bd78-480f-814b-b79a9a92e559 -> Assistant -> Step 1: Probe Video for Duration -> aaa28510-70e7-4b0a-b4b4-43752da44402 -> User -> 5959d47b-4592-4d1b-8ad4-07096d9c5fcf -> Assistant -> aaa20452-6339-498f-a308-f7809045dac3 -> User -> e0c9b1a8-a937-49c0-b18f-4e993b1d06ec -> Assistant -> aaa24f19-97f1-4924-8cf1-c04b4f6c650d -> User -> 1c07c845-e06f-4068-a8e0-477fcdd8c81a -> Assistant -> Approach -> Partial Content Fetching with HTTP Range Requests -> Using HLS (HTTP Live Streaming) -> Commands -> Frame Extraction -> 5-Second Clip -> Python Code to Automate the Task
---
### Python Code to Automate the Task

Here's how you can automate this task using Python and `asyncio`.

First, install the required packages if you haven't already:

```bash
pip install aiofiles aiohttp
```

Now, let's write the code:

```python
import asyncio
import aiohttp
import aiofiles
import os
from pathlib import Path

async def download_segment(url: str, start_time: int, duration: int, output_path: Path):
    command = [
        "ffmpeg",
        "-ss", str(start_time),  # Start time in seconds
        "-i", url,               # Input URL
        "-t", str(duration),     # Duration in seconds
        "-y",                    # Overwrite output files without asking
        str(output_path)         # Output path
    ]
    proc = await asyncio.create_subprocess_exec(*command)
    await proc.communicate()

async def main():
    url = "your_video_url_here"
    output_dir = Path("./clips")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Download a 5-second clip every 60 seconds
    for i in range(0, 600, 60):
        output_path = output_dir / f"clip_{i}.mp4"
        await download_segment(url, i, 5, output_path)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
```

Replace `your_video_url_here` with the video URL you're interested in.

This code will download a 5-second clip every 60 seconds up to the 600th second of the video. It saves the clips to a folder named `clips`.

Note: This example assumes that the server supports range requests or HLS segmentation. If the server doesn't, you'll have to download the entire video first, which you want to avoid.

---
