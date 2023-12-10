---
file: /home/pedro/Documents/chatgpt_export/Markdown/Braille Graphics CFFI Library.md
heading_stack: <root> -> b0cd4ccf-b58a-4555-9f13-6b1a31814d25 -> System -> 5a574436-e9d1-4b97-a272-d099a8dccb99 -> System -> aaa20d14-8506-4527-a842-e8b226e754d5 -> User -> 52f2c2a1-f4d8-4c75-a363-e17d0de117dc -> Assistant -> aaa2146d-e69a-4754-a17c-ac579be36bda -> User
---
# User

1. From tiny grids to reasonable size grids for terminal. Let's say the worst case scenario is a user who likes small fonts using a full screen terminal in a cinema screen should still have it work.

2. Let's do pure C.

3. There will be two main modes - newline joined lines (universal, can be copied and pasted or written to a file easily), and for live applications, terminal control character enabled display, for efficient drawing and refreshing.

4. Anything where the performance can shine. Perhaps tuples of (x, y) integer values, but I'm quite flexible on that and would be open to different ideas.

5. Broadly compatible.

[child ⬇️](#9fb3444e-a1db-43ec-8cb7-ff0bebf818c7)

---

(main branch ⎇)
###### 9fb3444e-a1db-43ec-8cb7-ff0bebf818c7
[parent ⬆️](#aaa2146d-e69a-4754-a17c-ac579be36bda)
