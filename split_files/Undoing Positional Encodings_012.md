---
file: /home/pedro/Documents/chatgpt_export/Markdown/Undoing Positional Encodings.md
heading_stack: <root> -> 4e44ee95-cb7a-4242-97be-52b6794098fd -> System -> 2984f899-ca70-4b1e-b2be-96ced8112a5e -> System -> aaa2f123-87f4-49f7-b9f0-234481819e63 -> User -> f32a251d-43c1-468d-8d74-d4e3d39545d5 -> Assistant -> aaa24e29-3f25-43e5-8bec-450e86dff908 -> User -> 777c7829-2f03-4e21-a4d2-d49947300f77 -> Assistant
---
# Assistant

Given your goal, the effect of positional encoding might indeed be a confounding factor when visualizing latent spaces. However, completely removing the positional encoding is non-trivial for the reasons previously discussed. Here are some alternative approaches that you could try:

1. **Initial Layers**: You could extract the hidden states from earlier layers where the effect of positional encoding might be less pronounced. This could offer a less "tainted" view of the latent space.

2. **Zero Positional Encoding**: Another approach is to set the positional encoding to zero and then feed the sequences through the model. This would result in a hidden state representation that is devoid of any positional information. Note that this would be a kind of "what-if" scenario and not a true undoing of the encoding.

3. **Statistical Adjustment**: You could try to statistically adjust the latent states to account for the influence of positional encodings. For example, you could fit a model that predicts latent states based solely on the positional encodings and then remove this predicted component from the actual latent states.

4. **Relative Positional Encoding**: Some models use relative positional encoding which is more focused on the relationship between tokens rather than their absolute position. If the model architecture allows for it, using relative positional encoding could lessen the positional impact on the latent space.

5. **Cluster Analysis**: Another approach could be to perform clustering on the latent states and then analyze the characteristics of each cluster. This could potentially help in separating out the effect of positional encodings.

6. **Manual Inspection**: As a last resort, you could manually inspect a subset of the latent states and their corresponding generated text to better understand how positional encoding is affecting the latent space.

Given your expertise, you could even combine these approaches to see which offers the best separation of content from positional effects in the latent space. Would you like to delve into one of these approaches in more detail?

[child ⬇️](#aaa2a0c1-8281-4119-936d-0786564f543e)

---

(main branch ⎇)
###### aaa2a0c1-8281-4119-936d-0786564f543e
[parent ⬆️](#777c7829-2f03-4e21-a4d2-d49947300f77)
