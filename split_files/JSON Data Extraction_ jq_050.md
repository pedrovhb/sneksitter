---
file: /home/pedro/Documents/chatgpt_export/Markdown/JSON Data Extraction_ jq.md
heading_stack: <root> -> 0da08a04-263e-41bd-91e8-c2620b989fa4 -> System -> e1b93c0a-ed30-42f4-bf81-94e5d490b58b -> System -> aaa26758-0603-4c3f-95ee-b342d51f8994 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 08cbcecf-1e14-4ea3-910f-35a04d540224 -> Assistant -> aaa21fc3-afbc-44a2-ac1c-ea4b05477e07 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 49383519-faff-4971-bb2b-01c0949c193d -> Assistant -> aaa2855e-a232-48aa-8ee0-7ce52f72c15b -> User -> d2abf624-a7ba-4ed7-9fae-71eebccb5373 -> Assistant -> aaa233eb-b6ce-4038-9243-d250e75b0027 -> User -> e3ef8bdf-7ef6-4273-add9-382ab74984ec -> Assistant -> aaa2a2e0-85f8-40fa-abf0-2cc194c3b5ba -> User -> eda4f377-6caa-4c6f-aeb4-7ceb79c27e9d -> Assistant -> aaa2915e-b872-4486-9d2f-5b7045726de4 -> User -> 41009490-cce6-4664-8f6a-a0f62a387541 -> Assistant -> aaa2c724-d7b8-4ddd-848d-13eff3e7a386 -> User -> eb9bf749-02d7-472e-ae23-6df540dafbef -> Assistant
---
# Assistant

Great, let's enhance the script based on your requirements. We'll make the following changes:

1. Use a global `httpx.AsyncClient` object to reuse connections.
2. Limit concurrent downloads to 5 using a semaphore.
3. Use a user-agent string that mimics a normal web browser.
4. Display download progress and logs using the `rich` library.

First, install the required `rich` library:

```bash
!pip install rich
```

Now, the updated script:

```python
import asyncio
import httpx
import json
import sys
from slugify import slugify
from pathlib import Path
from rich.console import Console
from rich.progress import Progress

console = Console()
progress = Progress(console=console)

client = httpx.AsyncClient(headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.3"
})
semaphore = asyncio.Semaphore(5)

async def download_file(url, filename: Path, task_id):
    async with semaphore, client.get(url) as r:
        if r.status_code == 200:
            filename.write_bytes(r.content)
            with progress:
                progress.update(task_id, advance=1)
                console.log(f"Downloaded {filename}")

async def main():
    json_data = json.load(sys.stdin)
    
    tasks = []
    with progress:
        task_id = progress.add_task("Downloading...", total=len(json_data))

        for item in json_data:
            quality = item.get("quality")
            duration = item.get("duration")
            alt = item.get("alt")
            href = item.get("href")
            img_thumb = item.get("img_thumb")
            vid_thumbnail = item.get("vid_thumbnail")

            slug = slugify(href)

            if img_thumb:
                img_filename = Path(f"{slug}-img_thumb.jpg")
                tasks.append(download_file(img_thumb, img_filename, task_id))

            if vid_thumbnail:
                vid_filename = Path(f"{slug}-vid_thumbnail.jpg")
                tasks.append(download_file(vid_thumbnail, vid_filename, task_id))

        await asyncio.gather(*tasks)
        
        console.log("All downloads complete.")

if __name__ == "__main__":
    asyncio.run(main())
```

To execute, run:

```bash
cat your_data.json | python your_script.py
```

Here's what changed:

- Added the `rich` library's `Console` and `Progress` to display logs and progress bars.
- Defined a global `httpx.AsyncClient` object with the user-agent string.
- Introduced a semaphore to limit the number of concurrent downloads.
- Updated the `download_file()` function to use the semaphore, display progress, and log download completion.

The script will now display a progress bar and log messages as it downloads the files.

---
