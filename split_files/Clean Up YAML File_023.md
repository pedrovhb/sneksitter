---
file: /home/pedro/Documents/chatgpt_export/Markdown/Clean Up YAML File.md
heading_stack: <root> -> 3036fc2d-0131-4ece-9260-9db5fda4bac7 -> System -> c906f56e-5281-42ae-8f8c-e85f1623ae7e -> System -> aaa29a78-0bff-4967-a89c-a8299281843e -> User -> ef56f22f-19f1-42bd-a214-5b79de6e7c35 -> Assistant -> Steps to Clean Up the File -> Python Code to Perform These Steps -> 46afc464-1a90-4766-a3f3-4c9802264e4f -> Assistant -> 60c6cdcf-c5c3-4266-b15f-82e433f32926 -> Tool -> 3d4d27b4-e900-4388-8031-380ec6250890 -> Assistant -> aaa25102-ed61-4c87-b709-62516f83bb2c -> User -> 51b77da6-7d1a-4439-8c6f-863453a3331d -> Assistant -> Code to Auto-Escape Control Characters -> 65250812-09ae-450a-8cae-f909b1d2e1f8 -> Assistant
---
# Assistant

```python
def auto_escape_yaml_file(file_path: Path) -> (str, bool):
    # Read the file into a string
    file_content = file_path.read_text()
    
    # Initialize flag for whether escaping was done
    escaped = False
    
    # Replace non-printable characters with their Unicode escape sequence
    escaped_content = ''
    for ch in file_content:
        if ch.isprintable() or ch.isspace():
            escaped_content += ch
        else:
            escaped_content += f"\\u{ord(ch):04x}"
            escaped = True
            
    # Write the escaped content back to the file if any escaping was done
    if escaped:
        file_path.write_text(escaped_content)
        
    return escaped_content, escaped

# Create a sample YAML file with an unacceptable character
sample_yaml_path.write_text("key: value\nunacceptable: \x80")

# Auto-escape the sample YAML file
escaped_content, was_escaped = auto_escape_yaml_file(sample_yaml_path)

escaped_content, was_escaped
```

[child ⬇️](#8907255b-077e-4485-94fb-31d0a0421fb2)

---

(other branch ⎇)
###### 8907255b-077e-4485-94fb-31d0a0421fb2
[parent ⬆️](#65250812-09ae-450a-8cae-f909b1d2e1f8)
