# User

That's interesting. So the setup I'm building now is that after some discussion, the language model generates a YAML specification of the project, initially high level, and over a few refinement rounds with analyzing the spec and perhaps the language model asking questions to clarify scope, architecture, etc., the YAML evolves so it's something including, along other metadata, something hierarchical like

- package(s)
  - modules
    - module docstring
      - functions and classes in the module
        - functions and classes are represented by subobjects in yaml containing name, signature with types, members, and additional fields mapping to Google style docstrings

These rounds of refinement are meant for quickly aligning the project with the user's intention before committing to writing a bunch of code.

Then the plugin creates the files with the proper directories and fills the files with the function and class definitions as specified, but with just `pass` for function and method bodies. It can from then on use plugin commands (just API calls) to edit the body of created functions.

[child ⬇️](#fe9b346a-bb29-47a2-9d2c-46143833df8b)

---

(main branch ⎇)
###### fe9b346a-bb29-47a2-9d2c-46143833df8b
[parent ⬆️](#aaa22d81-0c5f-4c16-bfcb-6501028b3abb)