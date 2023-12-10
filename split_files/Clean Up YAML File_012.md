---
file: /home/pedro/Documents/chatgpt_export/Markdown/Clean Up YAML File.md
heading_stack: <root> -> 3036fc2d-0131-4ece-9260-9db5fda4bac7 -> System -> c906f56e-5281-42ae-8f8c-e85f1623ae7e -> System -> aaa29a78-0bff-4967-a89c-a8299281843e -> User -> ef56f22f-19f1-42bd-a214-5b79de6e7c35 -> Assistant -> Steps to Clean Up the File -> Python Code to Perform These Steps -> 46afc464-1a90-4766-a3f3-4c9802264e4f -> Assistant
---
# Assistant

```python
from pathlib import Path

def clean_yaml_file(file_path: Path) -> None:
    # Read the file into a string
    file_content = file_path.read_text()
    
    # Filter out unacceptable control characters (non-printable ASCII characters)
    cleaned_content = ''.join(ch for ch in file_content if ch.isprintable() or ch.isspace())
    
    # Write the cleaned content back to the file
    file_path.write_text(cleaned_content)

# Create a sample YAML file with an unacceptable character
sample_yaml_path = Path("sample.yaml")
sample_yaml_path.write_text("key: value\nunacceptable: \x80")

# Clean up the sample YAML file
clean_yaml_file(sample_yaml_path)

# Verify the cleaned content
cleaned_content = sample_yaml_path.read_text()
cleaned_content
```

[child ⬇️](#60c6cdcf-c5c3-4266-b15f-82e433f32926)

---

(other branch ⎇)
###### 60c6cdcf-c5c3-4266-b15f-82e433f32926
[parent ⬆️](#46afc464-1a90-4766-a3f3-4c9802264e4f)
