---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Project Wizard.md
heading_stack: <root> -> 8c269285-142e-435d-b9a6-09f088ee55a0 -> System -> 3f14cc08-f4b7-4f8c-8004-80585ceb35cb -> System -> aaa238c5-ebfb-4a7c-a2a9-36a5e8e7f8b4 -> User -> 82599f1c-3cc9-483f-aec3-3ac7d27a364e -> Assistant -> Features: -> Workflow: -> Example Interaction: -> Output: -> Code Quality: -> aaa22d81-0c5f-4c16-bfcb-6501028b3abb -> User -> fe9b346a-bb29-47a2-9d2c-46143833df8b -> Assistant -> Example YAML Spec: -> Technical Details: -> aaa211da-11d1-42b0-b243-8b5317275494 -> User -> 20e348c8-2674-4247-a2df-a800d30e6919 -> Assistant -> Steps in Refinement Rounds:
---
### Steps in Refinement Rounds:

1. **Initial Analysis**: After the first draft of the YAML is generated, the model performs an analysis to identify gaps or ambiguities. For instance, if a database is specified but no models are defined, that could trigger a question.

2. **Question Generation**: The model generates a list of questions or options for the user. These could range from clarifying the purpose of a certain module to asking if additional functionalities should be added.

    - Example: "I see you've included a `PostgreSQL` database but haven't defined any models. Would you like to add some now?"

3. **User Input**: The user answers the questions, either refining existing entries in the YAML or adding new ones.

4. **YAML Update**: The model updates the YAML spec based on the answers.

5. **Validation**: Optionally, the updated YAML can be validated against a schema to ensure it's well-formed.

6. **Review**: The updated YAML is presented to the user for review. If they approve, it moves to code generation; otherwise, another refinement round is initiated.

