---
file: /home/pedro/Documents/chatgpt_export/Markdown/JSON Data Extraction_ jq.md
heading_stack: <root> -> 0da08a04-263e-41bd-91e8-c2620b989fa4 -> System -> e1b93c0a-ed30-42f4-bf81-94e5d490b58b -> System -> aaa26758-0603-4c3f-95ee-b342d51f8994 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 08cbcecf-1e14-4ea3-910f-35a04d540224 -> Assistant -> aaa21fc3-afbc-44a2-ac1c-ea4b05477e07 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 49383519-faff-4971-bb2b-01c0949c193d -> Assistant
---
# Assistant

To transform your given JSON data and extract the relevant information, you can use `jq` with the following query:

```bash
jq '[.[] | {quality: .children[] | select(.class == "quality") | .text, duration: .children[] | select(.class == "duration") | .text, alt: .children[] | select(.tag == "a") | .children[] | .children[] | .alt, href: .children[] | select(.tag == "a") | .href, img_thumb: .children[] | select(.tag == "a") | .children[] | .children[] | .["data-thumbnail"]}]'
```

Here's the breakdown:

- `quality: .children[] | select(.class == "quality") | .text` — selects the `.text` of a child object with `.class` set to "quality".
  
- `duration: .children[] | select(.class == "duration") | .text` — selects the `.text` of a child object with `.class` set to "duration".
  
- `alt: .children[] | select(.tag == "a") | .children[] | .children[] | .alt` — navigates through nested children to find the `.alt` attribute of the `<img>` tag.

- `href: .children[] | select(.tag == "a") | .href` — selects the `.href` of a child object with `.tag` set to "a".

- `img_thumb: .children[] |

[child 1 ⬇️](#aaa2855e-a232-48aa-8ee0-7ce52f72c15b) | [child 2 ⬇️](#aaa233eb-b6ce-4038-9243-d250e75b0027)

---

(other branch ⎇)
###### aaa2855e-a232-48aa-8ee0-7ce52f72c15b
[parent ⬆️](#49383519-faff-4971-bb2b-01c0949c193d)
