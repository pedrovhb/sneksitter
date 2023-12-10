---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Project Wizard.md
heading_stack: <root> -> 8c269285-142e-435d-b9a6-09f088ee55a0 -> System -> 3f14cc08-f4b7-4f8c-8004-80585ceb35cb -> System -> aaa238c5-ebfb-4a7c-a2a9-36a5e8e7f8b4 -> User -> 82599f1c-3cc9-483f-aec3-3ac7d27a364e -> Assistant -> Features: -> Workflow: -> Example Interaction: -> Output: -> Code Quality: -> aaa22d81-0c5f-4c16-bfcb-6501028b3abb -> User -> fe9b346a-bb29-47a2-9d2c-46143833df8b -> Assistant -> Example YAML Spec:
---
### Example YAML Spec:

```yaml
project_name: "MyWebApp"
framework: "Flask"
database: "PostgreSQL"
packages:
  - name: "controllers"
    modules:
      - name: "user_controller"
        docstring: "Handles user-related operations."
        functions:
          - name: "get_user"
            signature: "user_id: int"
            return_type: "User"
            docstring: "Retrieves a user."
          - name: "create_user"
            signature: "user_data: Dict[str, Any]"
            return_type: "User"
            docstring: "Creates a new user."
  - name: "models"
    modules:
      - name: "user_model"
        docstring: "User data model."
        classes:
          - name: "User"
            docstring: "User class."
            members: 
              - "id: int"
              - "name: str"
```

