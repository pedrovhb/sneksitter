---
file: /home/pedro/Documents/chatgpt_export/Markdown/AI-Friendly Programming Language.md
heading_stack: <root> -> b94d911f-3ac5-4eef-b701-2eb4def0cc3e -> System -> bd104c7b-8e42-4d87-8430-e4d7f8b03a46 -> System -> aaa29bc8-0f53-458f-8af0-b184dfe8e8b1 -> User -> d603f0c4-c267-4fbd-82a4-b50cdedd013f -> Assistant -> Considerations: -> Possibilities: -> aaa29f81-50fe-4ed9-8a62-cba2b8d99f33 -> User
---
# User

Say we're reimagining programming with AI models at the center, such that the objective is to generate code which is easy for LLMs to generate, and whose model of  evaluation/execution/syntax lends itself well too the model of functioning of language models. What are some considerations and possibilities in this sense?

I'm thinking something along the lines of - AI models are autoregressive; as such, how can we design something which fits well with this, and with the guiding we can do with the autoregressive paradigm? E.g. we can manipulate logits, so it would be beneficial if it were easy to determine the next valid tokens in the language so we could zero out logits which are invalid in the syntax. For another thought - we can do beam sampling, but beam length gets expensive with branching possible tokens and long sequences. How can we optimize for this by creating something whose validity or execution can be verified quickly and backtracked on if not accurate? What other opportunities arise?

[child ⬇️](#64b89f1a-d9c0-41bc-9a7f-ac09a7735d61)

---

(main branch ⎇)
###### 64b89f1a-d9c0-41bc-9a7f-ac09a7735d61
[parent ⬆️](#aaa29f81-50fe-4ed9-8a62-cba2b8d99f33)
