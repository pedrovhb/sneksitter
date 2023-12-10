---
file: /home/pedro/Documents/chatgpt_export/Markdown/Undoing Positional Encodings.md
heading_stack: <root> -> 4e44ee95-cb7a-4242-97be-52b6794098fd -> System -> 2984f899-ca70-4b1e-b2be-96ced8112a5e -> System -> aaa2f123-87f4-49f7-b9f0-234481819e63 -> User -> f32a251d-43c1-468d-8d74-d4e3d39545d5 -> Assistant
---
# Assistant

The concept of "undoing" positional encodings in large language models like GPT or BERT is not straightforward for several reasons:

1. **Non-Linearity**: The positional encodings are mixed with the token embeddings and then passed through multiple layers of non-linear transformations (like attention mechanisms and feed-forward neural networks). The operations are not easily invertible.

2. **Interactions**: The positional information is used in the attention mechanism to understand the relationship between different tokens in the sequence. This interaction is complex and not simply "added" to the hidden states.

3. **Architecture Specifics**: Different language models may use different kinds of positional encodings (sine/cosine-based, learned, etc.) and architectures (transformer-based, RNN-based, etc.), making a generic "undo" operation difficult.

In theory, one could attempt to construct a model to learn the inverse operation, but it would be highly approximate and computationally expensive. Moreover, the utility of such an "untainted" state is questionable, as the positional information is crucial for the model's understanding of the sequence.

Given your expertise, you'll recognize that the operation is akin to trying to reverse-engineer a highly complex and non-linear function, which is generally an intractable problem.

[child ⬇️](#aaa24e29-3f25-43e5-8bec-450e86dff908)

---

(main branch ⎇)
###### aaa24e29-3f25-43e5-8bec-450e86dff908
[parent ⬆️](#f32a251d-43c1-468d-8d74-d4e3d39545d5)
