# Assistant

The language model could serve as an intelligent code generator that kickstarts your projects by scaffolding out the basic structure, files, and even some initial code. Here's how it could look in practice:

### Features:

1. **Project Type Selection**: Ask the user to specify the type of project (e.g., web app, CLI tool, data pipeline, etc.).
2. **Technology Stack**: Query for the preferred technology stack (e.g., Flask for web, Click for CLI, etc.).
3. **Configuration**: Gather requirements like database setup, cloud provider, CI/CD, etc.
4. **Code Generation**: Generate the basic skeleton of the code.
5. **Best Practices**: Include linters, formatters, and basic tests.

### Workflow:

1. **Initialization**: User invokes the wizard with a command, perhaps `init_project`.
2. **Interactive Q&A**: The wizard asks a series of questions to understand the user's needs.
3. **Generation**: Code, files, and directories are generated.
4. **Post-Generation**: Optional steps like git initialization, virtual environment setup, and dependency installation.

### Example Interaction:

```bash
$ init_project
> What type of project are you creating? [web/cli/data/...]
> web
> Choose a web framework: [Flask/Django/FastAPI/...]
> Flask
> Would you like to include a database? [Yes/No]
> Yes
> Choose a database: [PostgreSQL/MySQL/SQLite]
> PostgreSQL
...
```

### Output:

- Creates a directory structure with Flask-specific files.
- Generates a `requirements.txt` or `Pipfile` with Flask and PostgreSQL adapter.
- Creates a `.env` file for environment variables.
- Sets up initial Flask routes in `app.py`.
- Creates an initial `README.md` with project details.

### Code Quality:

The generated code would follow best practices and could optionally include elements like:

- Type hints and comments
- Logging setup
- Test suite setup with sample tests

Given your skill set, this could be implemented as a Python CLI tool using libraries like `click` for the CLI interface and `jinja2` for templating. The tool could be made async where IO-bound operations are involved. Would you like to dive deeper into any specific part?

[child ⬇️](#aaa22d81-0c5f-4c16-bfcb-6501028b3abb)

---

(main branch ⎇)
###### aaa22d81-0c5f-4c16-bfcb-6501028b3abb
[parent ⬆️](#82599f1c-3cc9-483f-aec3-3ac7d27a364e)
