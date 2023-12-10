---
file: /home/pedro/Documents/chatgpt_export/Markdown/Training LLMs for FIM.md
heading_stack: <root> -> d3653077-6640-4b01-b930-cc922166c99e -> System -> 42013fd0-4021-45b5-a02e-4bbeeeb173ab -> System -> aaa298f3-a860-4d8c-9fe0-73b1a02d2c0f -> User -> ccf9ba9f-5d24-494c-97d3-9b4b0f0fa00e -> Assistant -> aaa21265-6d8b-4384-8c19-d32ac8c59430 -> User -> 18a81849-1009-4f45-84b4-5bca45f411e8 -> Assistant -> Data Preparation -> Training Objective -> Training Process -> Inference -> Caveats
---
### Caveats
- Autoregressive models generate tokens sequentially, so inference may require workarounds such as generating multiple sequences and then selecting the one that best fits the mask.
- The model may require a "warm-up" phase during inference to properly condition on the prefix before reaching the masked part.

While this approach repurposes an autoregressive model for a task it's not naturally suited for, it can be effective if done correctly.

---
