---
file: /home/pedro/Documents/chatgpt_export/Markdown/Undoing Positional Encodings.md
heading_stack: <root> -> 4e44ee95-cb7a-4242-97be-52b6794098fd -> System -> 2984f899-ca70-4b1e-b2be-96ced8112a5e -> System -> aaa2f123-87f4-49f7-b9f0-234481819e63 -> User -> f32a251d-43c1-468d-8d74-d4e3d39545d5 -> Assistant -> aaa24e29-3f25-43e5-8bec-450e86dff908 -> User -> 777c7829-2f03-4e21-a4d2-d49947300f77 -> Assistant -> aaa2a0c1-8281-4119-936d-0786564f543e -> User -> 522d93aa-16c8-4f86-94e3-a19bb56622ee -> Assistant
---
# Assistant

Certainly. The idea behind setting the positional encoding to zero is to effectively "neutralize" its impact on the subsequent hidden states. In this scenario, the only information that would be propagated through the network would come from the token embeddings themselves.

Here's a step-by-step explanation:

1. **Token Embeddings**: First, you obtain the token embeddings for your sequence just like you normally would.

2. **Zero Positional Encoding**: Instead of adding the usual positional encodings to the token embeddings, you add zeros of the same shape. This means that the positional information is effectively set to a neutral state.

3. **Forward Pass**: You then perform a forward pass through the model using this "position-less" input. The resulting hidden states should, in theory, be free from the influence of positional encoding.

4. **Analysis**: You can now use these "position-less" hidden states for your UMAP visualization or any other analysis you're interested in.

5. **Caveats**: Keep in mind that by doing this, you're essentially using the model in a way it was not trained for. The absence of positional information could lead to hidden states that are difficult to interpret or lack meaningful structure, as the model relies on position for understanding sequence relationships.

This approach is more of a "what-if" analysis to understand how the latent states might look without the influence of positional encoding. It's not an "undoing" of the effect, but rather an exploration of how the model behaves without that specific information. Would you like to proceed with a code example to illustrate this?

---
