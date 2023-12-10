---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Review Template Design.md
heading_stack: <root> -> 614c118a-e7bd-4dab-b05b-1e9de063e318 -> System -> 3131d9ce-3bbd-484f-ad76-d940b1b89d05 -> System -> aaa24d68-b640-47f4-8003-0fff2fcafd6c -> User -> dcb6f63d-9e74-4323-881a-676a66b09f52 -> Assistant -> Scope Definition -> Review Objective -> Ethical Guidelines -> Complexity -> Critical Sections -> Technical Depth -> Commentary and Rationale -> Code Smells and Anti-Patterns -> Suggested Improvements -> Test Coverage -> Concurrency and Performance -> Documentation -> aaa2cc11-bb55-4eb7-bac2-4a51c5c7fc26 -> User -> 6639f3ab-d612-4912-927a-c881ce116081 -> Assistant -> Structure and Formatting -> Content -> Interactivity -> Extensibility -> Usability -> Automation -> aaa20e00-6513-49de-97df-f6bf9c8c06c3 -> User -> 6ff1f292-044b-45be-997d-fd21ad691520 -> Assistant -> aaa299f2-2551-4084-8942-2f8df78204a5 -> User -> e0518dbf-f701-4180-98ce-d9545c7e087a -> Assistant -> aaa21371-7723-428e-b458-648552fa5e23 -> User -> f7a493ff-26df-4622-b69c-5cbe7de1042c -> Assistant -> aaa2456c-c3a5-42d2-821c-78656e0132eb -> User -> bf846e8e-cdd9-47db-b5f9-59059d933354 -> Assistant
---
# Assistant

Making the template more generic involves introducing optional sections and phrasing that allow for flexibility depending on the nature of the code being reviewed. You might want to include conditional logic or questions that guide the reviewer in deciding what sections to complete. Here's a revised version of the template:

```markdown
# Code Review Template

## Table of Contents
1. [General Information](#general-information)
2. [Readability](#readability)
3. [Performance](#performance)
4. [Optional: Error Handling](#optional-error-handling)
5. [Optional: Test Coverage](#optional-test-coverage)
6. [Optional: Security](#optional-security)
7. [Consistency and Coding Standards](#consistency-and-coding-standards)
8. [Optional: Best Practices](#optional-best-practices)
9. [Additional Remarks](#additional-remarks)

---

## General Information
- **Reviewer**: 
- **Date of Review**: 
- **Code Repository**: 
- **Reviewed Commit/PR**: 

---

## Readability

### Variable Naming
- Are variables appropriately named?

### Comments
- Are comments clear and informative?

### Code Organization
- Is the code logically structured?

---

## Performance

### Time Complexity
- Are there any obvious optimizations?

### Space Complexity
- Is memory used efficiently?

---

## Optional: Error Handling

### Exception Handling
- Are errors caught and handled gracefully?

### Logging
- Are errors properly logged?

---

## Optional: Test Coverage

### Unit Tests
- Are unit tests comprehensive?

### Integration Tests
- Are integration tests present?

---

## Optional: Security

### Input Validation
- Are all user inputs validated?

### Data Encryption
- Is sensitive data encrypted?

---

## Consistency and Coding Standards

### Code Style
- Does the code follow project guidelines?

### Documentation
- Is the codebase sufficiently documented?

---

## Optional: Best Practices

- Are best practices followed in the code?

---

## Additional Remarks

- Additional comments or suggestions for the code.

---
```

Sections like "Test Coverage" and "Security" are marked as optional, and the reviewer can decide whether to complete them based on the context of the review. This offers a more flexible approach while still maintaining a systematic structure.

---

(main branch ⎇)
###### aaa2619d-0d4b-4eef-addf-d1d055249fa8
[parent ⬆️](#3131d9ce-3bbd-484f-ad76-d940b1b89d05)
