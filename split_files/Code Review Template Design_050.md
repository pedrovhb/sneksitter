---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Review Template Design.md
heading_stack: <root> -> 614c118a-e7bd-4dab-b05b-1e9de063e318 -> System -> 3131d9ce-3bbd-484f-ad76-d940b1b89d05 -> System -> aaa24d68-b640-47f4-8003-0fff2fcafd6c -> User -> dcb6f63d-9e74-4323-881a-676a66b09f52 -> Assistant -> Scope Definition -> Review Objective -> Ethical Guidelines -> Complexity -> Critical Sections -> Technical Depth -> Commentary and Rationale -> Code Smells and Anti-Patterns -> Suggested Improvements -> Test Coverage -> Concurrency and Performance -> Documentation -> aaa2cc11-bb55-4eb7-bac2-4a51c5c7fc26 -> User -> 6639f3ab-d612-4912-927a-c881ce116081 -> Assistant -> Structure and Formatting -> Content -> Interactivity -> Extensibility -> Usability -> Automation -> aaa20e00-6513-49de-97df-f6bf9c8c06c3 -> User -> 6ff1f292-044b-45be-997d-fd21ad691520 -> Assistant -> aaa299f2-2551-4084-8942-2f8df78204a5 -> User -> e0518dbf-f701-4180-98ce-d9545c7e087a -> Assistant -> aaa21371-7723-428e-b458-648552fa5e23 -> User -> f7a493ff-26df-4622-b69c-5cbe7de1042c -> Assistant -> aaa2456c-c3a5-42d2-821c-78656e0132eb -> User -> bf846e8e-cdd9-47db-b5f9-59059d933354 -> Assistant -> aaa2619d-0d4b-4eef-addf-d1d055249fa8 -> User -> 7307c40b-0515-4e4a-85ad-4f00a09a9ac8 -> Assistant
---
# Assistant

Designing a Markdown-based template for large language models to review code files is a non-trivial task. Here are some important considerations:

### Flexibility
- **Language Agnostic**: The template should be generic enough to accommodate multiple programming languages.
- **Review Scope**: Allow the model to comment on both micro (syntax, logic) and macro (architecture, design patterns) aspects.

### Structure
- **Headers and Sub-headers**: Clearly demarcate sections like "Code Quality", "Performance", "Security", etc.
- **Placeholders**: Use placeholders for code snippets, comments, and suggested changes.

### Guidance for the Model
- **Question Prompts**: Use question prompts under each section to guide the model in what to look for. E.g., "Is the function adhering to Single Responsibility Principle?"
- **Severity Indicators**: Use tags like `[Critical]`, `[Moderate]`, `[Low]` to indicate the importance of each point.

### Brevity and Depth
- **Conciseness**: Design the template to elicit concise yet informative responses.
- **No Fluff**: Avoid having the model produce verbose or redundant information.

### Functionality and Bug Detection
- **Checklist**: Include a checklist for common pitfalls and anti-patterns in code.
- **Test Case Suggestions**: Optionally, a section where the model can suggest test cases.

### Example Template Structure

Here's a simplified example structure:

```markdown
# Code Review by [Model Name]

## Summary
- **File**: [File Name]
- **Language**: [Programming Language]
- **Reviewer**: [Model Name]

## Code Quality
### Readability
- Are variable names descriptive?
- Is the code well-commented?

### Maintainability
- Does the code adhere to DRY principles?
- Are there any magic numbers or strings?

## Performance
- Are there any obvious bottlenecks?
- Are data structures used appropriately?

## Security
- Are there any potential security vulnerabilities?
- Is sensitive data handled securely?

## Best Practices
- Is error-handling implemented?
- Are there logging mechanisms in place?

## Suggested Changes
- [Code snippet / Line number]: [Suggested change]

## Conclusion
- Summary of key points
- Recommended next steps
```

This is just a starting point; the template should be iteratively refined based on the quality and relevance of the reviews it produces.

[child ⬇️](#aaa2cc05-65f0-485a-a0aa-e03c2683acff)

---

(main branch ⎇)
###### aaa2cc05-65f0-485a-a0aa-e03c2683acff
[parent ⬆️](#7307c40b-0515-4e4a-85ad-4f00a09a9ac8)
