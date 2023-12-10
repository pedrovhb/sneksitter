---
file: /home/pedro/Documents/chatgpt_export/Markdown/JSON Data Extraction_ jq.md
heading_stack: <root> -> 0da08a04-263e-41bd-91e8-c2620b989fa4 -> System -> e1b93c0a-ed30-42f4-bf81-94e5d490b58b -> System -> aaa26758-0603-4c3f-95ee-b342d51f8994 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 08cbcecf-1e14-4ea3-910f-35a04d540224 -> Assistant
---
# Assistant

Certainly, the JSON data can be transformed using `jq` to get only the required attributes.

Here's the `jq` query to extract the relevant fields:

```bash
jq '{
  quality: .children[] | select(.class == "quality") | .text,
  duration: .children[] | select(.class == "duration") | .text,
  alt: .children[] | select(.class == "thumbnail_wrapper") | .children[0].children[0].alt,
  href: .children[] | select(.class == "thumbnail_wrapper") | .children[0].href,
  img_thumb: .children[] | select(.class == "thumbnail_wrapper") | .children[0].children[0]["data-thumbnail"],
  vid_thumb: .children[] | select(.class == "thumbnail_wrapper") | .children[0].children[0]["data-thumbnail"]
}' input.json
```

This `jq` query will select each child node of the input JSON where the class matches the desired one and extract the corresponding value. The output will be a new JSON object with only the relevant data.

Replace `input.json` with the file that contains your input JSON data.

---

(main branch ⎇)
###### aaa21fc3-afbc-44a2-ac1c-ea4b05477e07
[parent ⬆️](#e1b93c0a-ed30-42f4-bf81-94e5d490b58b)
