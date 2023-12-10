---
file: /home/pedro/Documents/chatgpt_export/Markdown/Logic Programming Basics.md
heading_stack: <root> -> aae83d65-0c6b-4610-b472-2aec0cdb80b3 -> System -> cd5f65ce-2de1-48c1-aa94-c4163a6f79bd -> System -> aaa22cbb-606f-41d0-b4ae-e591f21bb854 -> User -> e29cce05-dbd4-4728-8c1b-c03f43a7b92e -> Assistant -> Core Components -> How It Works -> Execution Flow: -> aaa2ae6d-a9b8-41f7-87e8-a93920624bd0 -> User -> a699099e-00cf-49be-8eb0-38733c577fa0 -> Assistant -> ac90bca6-5a7a-4d60-9a92-0a011029e761 -> Tool -> 380dfda5-d15a-451f-8e90-19b93624240d -> Assistant -> aaa2c7ad-b00f-44e2-9de9-6d855dc585f8 -> User -> 7ef98a9f-1f7c-4b2d-92df-6e588b7a0d9f -> Assistant
---
# Assistant

Certainly, the idea of creating a more user-friendly query interface similar to Django's QuerySet API is intriguing. We can mimic that by creating a Python class that abstracts the underlying logic of facts, rules, and queries, and allows chaining of methods for more complex queries.

Here's how we could architect this:

1. **Core Logic Class**: This class would contain methods to add facts, rules, and perform queries. The basic logic remains the same as in the earlier example.
  
2. **Query Interface Class**: A higher-level class that provides methods for querying. Each method returns a new instance of the class with the query conditions updated, allowing for chainable queries.

Let's go ahead and implement this.

[child ⬇️](#437c6506-4d99-402e-8217-957b6ba049be)

---

(main branch ⎇)
###### 437c6506-4d99-402e-8217-957b6ba049be
[parent ⬆️](#7ef98a9f-1f7c-4b2d-92df-6e588b7a0d9f)