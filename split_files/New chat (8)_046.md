---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant -> e3e20cb1-d7af-4b3a-8989-0f635e7b7b37 -> Assistant -> 0f60f5d4-ccff-409d-a801-fe2e8e24b7e0 -> Tool -> 2dde9631-ce8a-470f-a73d-efdd18304420 -> Assistant -> efc03986-9e2b-44f4-b7a8-f1ea222b2fe6 -> Assistant -> 6ed08e43-230e-4b6e-a185-fa455f069e46 -> Tool -> b8da2c4b-9db2-47d7-a2af-389be4befc5f -> Assistant -> db2e1dd1-0795-480b-bc14-771d0eb39e4d -> Assistant -> e7105360-42e1-44dc-b634-fe0c00e4e999 -> Tool -> ca3c2937-19b7-4c14-9f94-a96c4aa48bf4 -> Assistant -> aaa241ef-101a-4eeb-93d2-e8d8919d06d9 -> User -> 0d4987c7-80b3-4264-a7cb-373f269f73d6 -> Assistant -> aaa2d51e-8b35-443b-8c51-50d3a8740574 -> User -> 4b0ff9a6-0c97-4d93-b7b8-d64c70c39fe0 -> Assistant -> aaa29522-caba-4582-81f4-fa790988a5cb -> User -> 2671227c-f5b3-4e6a-8bc8-cf8625b9df85 -> Assistant -> 0378287d-290e-4e7d-b03a-e96ab29bc45d -> Tool -> 8be38330-dba2-463c-acb5-18b403657055 -> Assistant -> c66b0691-c55b-4e68-96b1-91f3dc82f4b7 -> Assistant -> a3e0a4c8-fc88-4485-9059-7f406744f6b4 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[2], line 39
     36 h2_wrap = g_wrap << f_wrap  # Should be equivalent to f(g(x))
     38 # Run the test again
---> 39 await test_composition()

Cell In[1], line 63, in test_composition()
     61 async def test_composition():
     62     assert await h1_wrap.func(1) == 4  # (1 + 1) * 2 = 4
---> 63     assert await h2_wrap.func(1) == 3

AssertionError: 

```

[child ⬇️](#419e449b-8c14-40cc-a0c1-b3e7c21548f0)

---

(main branch ⎇)
###### 419e449b-8c14-40cc-a0c1-b3e7c21548f0
[parent ⬆️](#a3e0a4c8-fc88-4485-9059-7f406744f6b4)
