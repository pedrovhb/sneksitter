### Steps in Refinement Rounds:

1. **Initial Analysis**: After the first draft of the YAML is generated, the model performs an analysis to identify gaps or ambiguities. For instance, if a database is specified but no models are defined, that could trigger a question.

2. **Question Generation**: The model generates a list of questions or options for the user. These could range from clarifying the purpose of a certain module to asking if additional functionalities should be added.

    - Example: "I see you've included a `PostgreSQL` database but haven't defined any models. Would you like to add some now?"

3. **User Input**: The user answers the questions, either refining existing entries in the YAML or adding new ones.

4. **YAML Update**: The model updates the YAML spec based on the answers.

5. **Validation**: Optionally, the updated YAML can be validated against a schema to ensure it's well-formed.

6. **Review**: The updated YAML is presented to the user for review. If they approve, it moves to code generation; otherwise, another refinement round is initiated.

