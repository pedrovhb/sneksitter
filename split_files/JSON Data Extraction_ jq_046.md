---
file: /home/pedro/Documents/chatgpt_export/Markdown/JSON Data Extraction_ jq.md
heading_stack: <root> -> 0da08a04-263e-41bd-91e8-c2620b989fa4 -> System -> e1b93c0a-ed30-42f4-bf81-94e5d490b58b -> System -> aaa26758-0603-4c3f-95ee-b342d51f8994 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 08cbcecf-1e14-4ea3-910f-35a04d540224 -> Assistant -> aaa21fc3-afbc-44a2-ac1c-ea4b05477e07 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 49383519-faff-4971-bb2b-01c0949c193d -> Assistant -> aaa2855e-a232-48aa-8ee0-7ce52f72c15b -> User -> d2abf624-a7ba-4ed7-9fae-71eebccb5373 -> Assistant -> aaa233eb-b6ce-4038-9243-d250e75b0027 -> User -> e3ef8bdf-7ef6-4273-add9-382ab74984ec -> Assistant -> aaa2a2e0-85f8-40fa-abf0-2cc194c3b5ba -> User -> eda4f377-6caa-4c6f-aeb4-7ceb79c27e9d -> Assistant -> aaa2915e-b872-4486-9d2f-5b7045726de4 -> User -> 41009490-cce6-4664-8f6a-a0f62a387541 -> Assistant
---
# Assistant

Sure, we'll modify the script to read JSON data from `stdin`. I'll also update the script to use the `pathlib.Path` library to handle file paths, as per your preferences.

Here's the updated Python script:

```python
import asyncio
import httpx
import json
import sys
from slugify import slugify
from pathlib import Path

async def download_file(url, filename: Path):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            filename.write_bytes(r.content)

async def main():
    json_data = json.load(sys.stdin)
    
    tasks = []
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
            tasks.append(download_file(img_thumb, img_filename))

        if vid_thumbnail:
            vid_filename = Path(f"{slug}-vid_thumbnail.jpg")
            tasks.append(download_file(vid_thumbnail, vid_filename))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

To run the script, you can pipe the JSON data into it:

```bash
cat your_data.json | python your_script.py
```

This will read the JSON data from `stdin`, parse it, and then asynchronously download the required files.

[child ⬇️](#aaa2c724-d7b8-4ddd-848d-13eff3e7a386)

---

(main branch ⎇)
###### aaa2c724-d7b8-4ddd-848d-13eff3e7a386
[parent ⬆️](#41009490-cce6-4664-8f6a-a0f62a387541)
