---
file: /home/pedro/Documents/chatgpt_export/Markdown/AI-Friendly Programming Language.md
heading_stack: <root> -> b94d911f-3ac5-4eef-b701-2eb4def0cc3e -> System -> bd104c7b-8e42-4d87-8430-e4d7f8b03a46 -> System -> aaa29bc8-0f53-458f-8af0-b184dfe8e8b1 -> User -> d603f0c4-c267-4fbd-82a4-b50cdedd013f -> Assistant -> Considerations: -> Possibilities: -> aaa29f81-50fe-4ed9-8a62-cba2b8d99f33 -> User -> 64b89f1a-d9c0-41bc-9a7f-ac09a7735d61 -> Assistant -> Syntax Design
---
### Syntax Design

1. **Token Minimization**: Reducing the number of tokens needed to express a computation can help in controlling the logits and thus make it easier to guide the language model. This would also reduce the beam width during beam search.
  
2. **Context-Free Syntax**: A language that allows you to determine the validity of the next token solely based on the last few tokens will be easier for autoregressive models to work with. This would allow for more effective zeroing out of invalid logits.

3. **Explicit Markers for Scopes**: Using explicit tokens to mark the beginning and end of scopes (like loops or conditionals) could make it easier for the model to understand the context in which it's generating code.

