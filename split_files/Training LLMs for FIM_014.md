---
file: /home/pedro/Documents/chatgpt_export/Markdown/Training LLMs for FIM.md
heading_stack: <root> -> d3653077-6640-4b01-b930-cc922166c99e -> System -> 42013fd0-4021-45b5-a02e-4bbeeeb173ab -> System -> aaa298f3-a860-4d8c-9fe0-73b1a02d2c0f -> User -> ccf9ba9f-5d24-494c-97d3-9b4b0f0fa00e -> Assistant -> aaa21265-6d8b-4384-8c19-d32ac8c59430 -> User -> 18a81849-1009-4f45-84b4-5bca45f411e8 -> Assistant -> Data Preparation -> Training Objective
---
### Training Objective
While the underlying architecture remains autoregressive, you can modify the loss function to focus on the masked tokens. Essentially, you want the model to learn the conditional probabilities of the masked tokens given the surrounding context.

1. **Custom Loss Function**: During the backpropagation step, apply the loss function only to the positions corresponding to the masked tokens.

