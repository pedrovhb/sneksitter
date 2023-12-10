---
file: /home/pedro/Documents/chatgpt_export/Markdown/Self-Extracting Python Script Framework.md
heading_stack: <root> -> b84c160d-01f8-4464-bdcb-ce33aed920f2 -> System -> 223bd57b-5a68-450f-8413-2c9aaa3de884 -> System -> aaa2f0a0-5c47-46c8-9517-226c34230146 -> User -> 0fec26b9-8a0c-4dfc-b842-fb7cf4697924 -> Assistant -> Problem Exploration and Design Specification -> Problem Statement -> Core Components -> Data Packing -> Data Unpacking -> Operation Interfaces -> Script Generation -> Specifications -> aaa28cbe-9139-4539-915e-cee347975b63 -> User -> 2d6e1ca0-1786-4102-b30e-5545b9b2f1e0 -> Assistant -> aaa2fcae-5154-4dac-91c6-f8c98e0dba1f -> User -> e7d6cadc-2ed5-4673-aa24-5eabdf011818 -> Assistant -> 4ab984b5-d8c1-4463-83b0-dd85ff18f35f -> Tool -> 2e7a6320-a857-4f06-9c46-2438d80bb331 -> Assistant -> 30890fc7-d405-44a9-b4b4-5755b79309c7 -> Assistant -> 8cfa77c9-ffc0-42a1-b070-72225b99093d -> Tool -> 682274cb-508e-40ea-b309-1c8ae23ed8ad -> Assistant -> aaa2c4c9-6f1b-496c-98e9-fb1ccce31bff -> User -> f58e1ce0-a2bf-4b5a-8a83-c57d7ae7b39d -> Assistant
---
# Assistant

```python
from typing import List, Union

# Refactor Abstract Base Class for Operations with type annotations
class Operation(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def validate(self) -> None:
        pass

    @abstractmethod
    def generate_code(self) -> str:
        pass

# Refactor InstallLibraries class with type annotations
class InstallLibraries(Operation):
    def __init__(self, libraries: List[str]) -> None:
        self.libraries = libraries

    def execute(self) -> None:
        pass

    def validate(self) -> None:
        pass

    def generate_code(self) -> str:
        libraries_str = ', '.join([f'"{lib}"' for lib in self.libraries])
        return f"subprocess.run(['pip', 'install', {libraries_str}])"

# Refactor data packing and script generation functions with type annotations
def pack_data(paths: List[str]) -> str:
    with tempfile.NamedTemporaryFile() as temp_file:
        with tarfile.open(fileobj=temp_file, mode="w:gz") as tar:
            for path in paths:
                tar.add(path)
        temp_file.seek(0)
        return base64.b64encode(temp_file.read()).decode('utf-8')

def generate_script(operations: List[Operation], packed_data: str) -> str:
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

# Re-create temporary files and folders for demonstration
temp_dir.mkdir(exist_ok=True)
with temp_file.open("w") as f:
    f.write("This is a sample file.")

# Example usage with type annotations
paths = [str(temp_file)]
operations = [InstallLibraries(["numpy", "pandas"])]
packed_data = pack_data(paths)
script = generate_script(operations, packed_data)

# Clean up the temporary files and folders
temp_file.unlink()
temp_dir.rmdir()

# Show a snippet of the generated script
print(script[:500] + "...")
```

[child ⬇️](#fb30f088-a47f-4bd3-880d-f080eedfdb46)

---

(main branch ⎇)
###### fb30f088-a47f-4bd3-880d-f080eedfdb46
[parent ⬆️](#f58e1ce0-a2bf-4b5a-8a83-c57d7ae7b39d)
