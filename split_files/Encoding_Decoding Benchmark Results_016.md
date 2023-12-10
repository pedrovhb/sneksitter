---
file: /home/pedro/Documents/chatgpt_export/Markdown/Encoding_Decoding Benchmark Results.md
heading_stack: <root> -> 45bfa0f9-0280-4536-84fe-9f5a2b886748 -> System -> 6e6dc52e-87cd-443f-8455-8f3b2627c1a5 -> System -> aaa2d7d6-5705-4351-a4b5-6ac5b9bb328d -> User -> 2fb2df16-e3b9-43e8-b679-167cac98874e -> Assistant -> 99cabd56-53c1-4d29-95a7-64a236319ddf -> Tool -> 6e23f93f-78cb-4931-95c5-1a03ade96cc2 -> Assistant -> 6417ee72-c53a-491c-b535-4ee25c0edae1 -> Tool -> 196bf9c5-4a6e-4346-8dee-a0640c7dc5c2 -> Assistant
---
# Assistant

The benchmark results for the encoding and decoding functions are as follows:

- `encode_base16`: 0.00146 s
- `encode_base64`: 0.00155 s
- `decode_base64`: 0.00261 s
- `decode_base16`: 0.00612 s
- `encode_base85`: 0.02688 s
- `encode_base32`: 0.02707 s
- `decode_base85`: 0.04489 s
- `decode_base32`: 0.05348 s

The horizontal bar chart visualizes the time taken for each function to execute 1000 times. It's evident that encoding in base16 and base64 is the fastest, while decoding in base32 takes the most time.

Would you like to proceed with further analysis or visualization based on these results?

[child ⬇️](#aaa2ab41-acb8-41a3-b1d0-b8ec666f58a5)

---

(main branch ⎇)
###### aaa2ab41-acb8-41a3-b1d0-b8ec666f58a5
[parent ⬆️](#196bf9c5-4a6e-4346-8dee-a0640c7dc5c2)
