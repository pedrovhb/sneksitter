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

