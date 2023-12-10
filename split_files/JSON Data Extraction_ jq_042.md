---
file: /home/pedro/Documents/chatgpt_export/Markdown/JSON Data Extraction_ jq.md
heading_stack: <root> -> 0da08a04-263e-41bd-91e8-c2620b989fa4 -> System -> e1b93c0a-ed30-42f4-bf81-94e5d490b58b -> System -> aaa26758-0603-4c3f-95ee-b342d51f8994 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 08cbcecf-1e14-4ea3-910f-35a04d540224 -> Assistant -> aaa21fc3-afbc-44a2-ac1c-ea4b05477e07 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 49383519-faff-4971-bb2b-01c0949c193d -> Assistant -> aaa2855e-a232-48aa-8ee0-7ce52f72c15b -> User -> d2abf624-a7ba-4ed7-9fae-71eebccb5373 -> Assistant -> aaa233eb-b6ce-4038-9243-d250e75b0027 -> User -> e3ef8bdf-7ef6-4273-add9-382ab74984ec -> Assistant -> aaa2a2e0-85f8-40fa-abf0-2cc194c3b5ba -> User -> eda4f377-6caa-4c6f-aeb4-7ceb79c27e9d -> Assistant
---
# Assistant

To accomplish this task, we can write a Python script using the `httpx` library for HTTP requests and the `slugify` library for creating file-friendly names from the URLs. Since you've specified a preference for using `asyncio`, we can perform the downloads asynchronously.

First, let's install the required packages. I'll assume you already have `httpx`.

```bash
!pip install python-slugify
```

Now, let's write the Python script:

```python
import asyncio
import httpx
import json
from slugify import slugify
from pathlib import Path

async def download_file(url, filename):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(r.content)

async def main():
    json_data = [
        # your JSON data here
    ]
    
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

Here's what's happening in the script:

- The `download_file()` coroutine takes a URL and a filename, performs an HTTP GET request for the URL, and writes the content to the specified file.

- In the `main()` coroutine, we define our JSON data and iterate through each item.
  - We create slugified filenames based on the `href` field.
  - If there's an image or video thumbnail URL, we schedule a coroutine to download the corresponding file.

- Finally, we run the `main()` coroutine, which waits for all download tasks to complete.

You can populate the `json_data` list with your actual data. The script will then download the image and video thumbnails and save them using slugified filenames.

[child ⬇️](#aaa2915e-b872-4486-9d2f-5b7045726de4)

---

(main branch ⎇)
###### aaa2915e-b872-4486-9d2f-5b7045726de4
[parent ⬆️](#eda4f377-6caa-4c6f-aeb4-7ceb79c27e9d)
