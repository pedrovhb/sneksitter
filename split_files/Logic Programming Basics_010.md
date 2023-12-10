---
file: /home/pedro/Documents/chatgpt_export/Markdown/Logic Programming Basics.md
heading_stack: <root> -> aae83d65-0c6b-4610-b472-2aec0cdb80b3 -> System -> cd5f65ce-2de1-48c1-aa94-c4163a6f79bd -> System -> aaa22cbb-606f-41d0-b4ae-e591f21bb854 -> User -> e29cce05-dbd4-4728-8c1b-c03f43a7b92e -> Assistant -> Core Components -> How It Works
---
### How It Works

1. **Backtracking**: The heart of a logic programming language like Prolog is a backtracking algorithm. When a query is made, the system tries to match it against the known facts and rules. If a partial match is found but ultimately fails, the system backtracks to the last known good state and tries a different path.

2. **Unification**: This is the process of making two different logical expressions identical by finding a set of variable substitutions that make the expressions look the same.

3. **Resolution**: The rules are essentially implications. The system uses resolution to deduce new facts from existing facts and rules.

4. **Search Strategy**: Depth-first search is commonly used, but this can vary. Some systems implement more advanced strategies to improve efficiency.

5. **Recursion**: Many logic programs use recursion to define relations that have an arbitrary number of steps (like finding an ancestor in a family tree).

6. **Tail Call Optimization (TCO)**: Logic programming languages often implement TCO to handle recursion efficiently.

