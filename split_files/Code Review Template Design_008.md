---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Review Template Design.md
heading_stack: <root> -> 614c118a-e7bd-4dab-b05b-1e9de063e318 -> System -> 3131d9ce-3bbd-484f-ad76-d940b1b89d05 -> System -> aaa24d68-b640-47f4-8003-0fff2fcafd6c -> User -> dcb6f63d-9e74-4323-881a-676a66b09f52 -> Assistant
---
# Assistant

Designing a template for large language models to review code files is a task that requires careful consideration of various factors. These factors include the nature of the code to be reviewed, the expertise of the language model, and the systematic approach required to ensure that the review is comprehensive, coherent, and actionable. Below are key elements to keep in mind:

### Scope Definition
The first thing to consider is the scope of the review. This should be clearly defined in the template to avoid ambiguity. It should specify what types of code the review will cover—whether it's restricted to specific languages, frameworks, or systems.

### Review Objective
State the objective of the review in the template. Objectives could range from ensuring code quality to confirming security practices. This sets the tone and helps the model to focus its efforts accordingly.

### Ethical Guidelines
Considering the potential for biased or unfair reviews, especially in cases where code comments or variable names could have cultural, gender, or other biases, the template should include a section on ethical guidelines to ensure fair and equitable review.

### Complexity
Large codebases can be overwhelming. Therefore, the template should provide guidance on how to deal with complex or large code files. Whether the model should focus on specific modules or take a more high-level approach should be defined.

### Critical Sections
Identify critical sections of code that require more in-depth analysis. This could be parts of the code that deal with security, data integrity, or crucial business logic.

### Technical Depth
Given that you are a Senior Software Engineer with expertise in Python, Linux, and general computing, the template should allow for a deep technical dive. The model should be guided to look into design patterns, optimization, and even algorithmic efficiency.

### Commentary and Rationale
The template should have sections that prompt the model to explain the rationale behind its comments. Simple annotations like "this is bad" are not helpful. The model should provide context—why something is considered a bad practice and what the potential impacts could be.

### Code Smells and Anti-Patterns
These are common indicators of problems in the code. The template should include a checklist of common code smells and anti-patterns for the language or framework being reviewed.

### Suggested Improvements
It’s not enough to point out issues; a good review also offers solutions. The template should have a dedicated section for this, suggesting alternative approaches, refactoring, or even tools that could help improve the code.

### Test Coverage
Considering the importance of testing in modern software development, the template should prompt the model to evaluate the adequacy of test coverage and the quality of tests written.

### Concurrency and Performance
Given your preference for asyncio, the template should include a section that specifically focuses on evaluating the code's concurrency model and performance characteristics. 

### Documentation
Code isn’t just for machines; it’s for humans too. The template should require the model to assess the quality and completeness of code

---

(other branch ⎇)
###### aaa2cc11-bb55-4eb7-bac2-4a51c5c7fc26
[parent ⬆️](#3131d9ce-3bbd-484f-ad76-d940b1b89d05)
