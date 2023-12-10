---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant -> e3e20cb1-d7af-4b3a-8989-0f635e7b7b37 -> Assistant -> 0f60f5d4-ccff-409d-a801-fe2e8e24b7e0 -> Tool -> 2dde9631-ce8a-470f-a73d-efdd18304420 -> Assistant -> efc03986-9e2b-44f4-b7a8-f1ea222b2fe6 -> Assistant -> 6ed08e43-230e-4b6e-a185-fa455f069e46 -> Tool -> b8da2c4b-9db2-47d7-a2af-389be4befc5f -> Assistant
---
# Assistant

The synchronous function composition worked as expected, but the asynchronous composition failed. The issue is that we didn't properly account for the fact that some functions in the chain could be asynchronous while others are not.

When composing an asynchronous function with a synchronous function, the intermediate coroutine produced by the asynchronous function should be awaited before being passed to the next function. The current design doesn't handle this case well.

Let's refactor the composition part to properly handle these mixed cases.

[child ⬇️](#db2e1dd1-0795-480b-bc14-771d0eb39e4d)

---

(other branch ⎇)
###### db2e1dd1-0795-480b-bc14-771d0eb39e4d
[parent ⬆️](#b8da2c4b-9db2-47d7-a2af-389be4befc5f)
