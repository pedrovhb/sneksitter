---
file: /home/pedro/Documents/chatgpt_export/Markdown/JSON Data Extraction_ jq.md
heading_stack: <root> -> 0da08a04-263e-41bd-91e8-c2620b989fa4 -> System -> e1b93c0a-ed30-42f4-bf81-94e5d490b58b -> System -> aaa26758-0603-4c3f-95ee-b342d51f8994 -> User -> Input data -> Relevant data: -> - quality -> - duration -> - alt (title) -> - href (link) -> - img_thumb (data-thumbnail) -> - vid_thumb (data-thumbnail) -> jq query to extract relevant data in a nice new single object with the key names as per above: -> 08cbcecf-1e14-4ea3-910f-35a04d540224 -> Assistant -> aaa21fc3-afbc-44a2-ac1c-ea4b05477e07 -> User -> Input data
---
# Input data
[
{
  "children": [
    {
      "class": "quality",
      "tag": "div",
      "text": "HD"
    },
    {
      "class": "duration",
      "tag": "div",
      "text": "06:35"
    },
    {
      "children": [
        {
          "children": [
            {
              "alt": "Perky tits",
              "class": "poster vthumb",
              "data-thumbnail": "//cdn77.czechcash.com/files/czechcabins.com/e018/thumbnail-240p.mp4?secure=n_2F7DpGwFjtF9miFmmdyQ==,1704063600",
              "src": "https://thumbs.czechcash.com/526x295/czechcabins.com/e018/orig/sample.jpg?abuNFjGpoeiWgnPoL+JCey+waINzDGsK3S9oamSxhGKV2MXx3JN0PVQr3fzYUomObC/A6XX4Nzv41Imxn5+jHLYEXrlnSiosgQ1vZtcNz2E5WS7mt5bNb0PYOlmjiU7Fey6Mi7lUtx7NTn7RlRVA5oECnhi+5CXdMerRpD/hH+Q2Bjuc",
              "tag": "img"
            }
          ],
          "class": "thumbnail_wrapper",
          "tag": "div"
        }
      ],
      "href": "/members/gallery/perky-tits/",
      "tag": "a"
    }
  ],
  "class": "main-thumb",
  "tag": "div"
},
...
]

