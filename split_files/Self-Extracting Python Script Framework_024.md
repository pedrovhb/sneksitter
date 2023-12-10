---
file: /home/pedro/Documents/chatgpt_export/Markdown/Self-Extracting Python Script Framework.md
heading_stack: <root> -> b84c160d-01f8-4464-bdcb-ce33aed920f2 -> System -> 223bd57b-5a68-450f-8413-2c9aaa3de884 -> System -> aaa2f0a0-5c47-46c8-9517-226c34230146 -> User -> 0fec26b9-8a0c-4dfc-b842-fb7cf4697924 -> Assistant -> Problem Exploration and Design Specification -> Problem Statement -> Core Components -> Data Packing -> Data Unpacking -> Operation Interfaces -> Script Generation -> Specifications -> aaa28cbe-9139-4539-915e-cee347975b63 -> User -> 2d6e1ca0-1786-4102-b30e-5545b9b2f1e0 -> Assistant -> aaa2fcae-5154-4dac-91c6-f8c98e0dba1f -> User -> e7d6cadc-2ed5-4673-aa24-5eabdf011818 -> Assistant
---
# Assistant

```python
# Importing necessary modules for the framework
from abc import ABC, abstractmethod
import tarfile
import base64
from pathlib import Path
import tempfile
import textwrap

# Abstract Base Class for Operations
class Operation(ABC):
    @abstractmethod
    def execute(self):
        """Execute the operation."""
        pass

    @abstractmethod
    def validate(self):
        """Validate the operation before execution."""
        pass

    @abstractmethod
    def generate_code(self) -> str:
        """Generate the Python code for this operation."""
        pass

# Example Operation for Installing Libraries
class InstallLibraries(Operation):
    def __init__(self, libraries):
        self.libraries = libraries

    def execute(self):
        # Placeholder for installing libraries
        pass

    def validate(self):
        # Placeholder for validation
        pass

    def generate_code(self) -> str:
        libraries_str = ', '.join([f'"{lib}"' for lib in self.libraries])
        return f"subprocess.run(['pip', 'install', {libraries_str}])"

# Function to pack data into base64 tar.gz string
def pack_data(paths):
    with tempfile.NamedTemporaryFile() as temp_file:
        with tarfile.open(fileobj=temp_file, mode="w:gz") as tar:
            for path in paths:
                tar.add(path)
        temp_file.seek(0)
        return base64.b64encode(temp_file.read()).decode('utf-8')

# Function to generate the script
def generate_script(operations, packed_data):
    operations_code = "\n    ".join([op.generate_code() for op in operations])
    
    template = textwrap.dedent(f"""
        import base64
        import tarfile
        import tempfile
        import subprocess

        def main():
            # Unpack Data
            packed_data = "{packed_data}"
            with tempfile.NamedTemporaryFile() as temp_file:
                temp_file.write(base64.b64decode(packed_data))
                temp_file.seek(0)
                with tarfile.open(fileobj=temp_file, mode="r:gz") as tar:
                    tar.extractall()

            # Execute Operations
            {operations_code}

        if __name__ == '__main__':
            main()
    """)
    return template

# Example Usage
paths = ["some_file.txt", "some_folder"]
operations = [InstallLibraries(["numpy", "pandas"])]
packed_data = pack_data(paths)
script = generate_script(operations, packed_data)
print(script)
```

[child ⬇️](#4ab984b5-d8c1-4463-83b0-dd85ff18f35f)

---

(main branch ⎇)
###### 4ab984b5-d8c1-4463-83b0-dd85ff18f35f
[parent ⬆️](#e7d6cadc-2ed5-4673-aa24-5eabdf011818)
