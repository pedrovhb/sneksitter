---
file: /home/pedro/Documents/chatgpt_export/Markdown/JSON Data Extraction_ jq.md
heading_stack: <root> -> 0da08a04-263e-41bd-91e8-c2620b989fa4 -> System -> e1b93c0a-ed30-42f4-bf81-94e5d490b58b -> System -> aaa26758-0603-4c3f-95ee-b342d51f8994 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 08cbcecf-1e14-4ea3-910f-35a04d540224 -> Assistant -> aaa21fc3-afbc-44a2-ac1c-ea4b05477e07 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 49383519-faff-4971-bb2b-01c0949c193d -> Assistant -> aaa2855e-a232-48aa-8ee0-7ce52f72c15b -> User -> d2abf624-a7ba-4ed7-9fae-71eebccb5373 -> Assistant -> aaa233eb-b6ce-4038-9243-d250e75b0027 -> User -> e3ef8bdf-7ef6-4273-add9-382ab74984ec -> Assistant
---
# Assistant

Certainly, let's modify the `jq` query to also extract the `src` attribute for `img_thumbnail` and rename `data-thumbnail` to `vid_thumbnail`.

```bash
jq '[.[] | {quality: .children[] | select(.class == "quality") | .text, duration: .children[] | select(.class == "duration") | .text, alt: .children[] | select(.tag == "a") | .children[] | .children[] | .alt, href: .children[] | select(.tag == "a") | .href, img_thumb: .children[] | select(.tag == "a") | .children[] | .children[] | .src, vid_thumbnail: .children[] | select(.tag == "a") | .children[] | .children[] | .["data-thumbnail"]}]'
```

- `img_thumb: .children[] | select(.tag == "a") | .children[] | .children[] | .src` — navigates through nested children to find the `src` attribute of the `<img>` tag.

- `vid_thumbnail: .children[] | select(.tag == "a") | .children[] | .children[] | .["data-thumbnail"]` — renamed `data-thumbnail` to `vid_thumbnail` and extracted the value.

This `jq` query should now fulfill your requirements.

[child ⬇️](#aaa2a2e0-85f8-40fa-abf0-2cc194c3b5ba)

---

(main branch ⎇)
###### aaa2a2e0-85f8-40fa-abf0-2cc194c3b5ba
[parent ⬆️](#e3ef8bdf-7ef6-4273-add9-382ab74984ec)
