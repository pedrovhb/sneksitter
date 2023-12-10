---
file: /home/pedro/Documents/chatgpt_export/Markdown/Self-Extracting Python Script Framework.md
heading_stack: <root> -> b84c160d-01f8-4464-bdcb-ce33aed920f2 -> System -> 223bd57b-5a68-450f-8413-2c9aaa3de884 -> System -> aaa2f0a0-5c47-46c8-9517-226c34230146 -> User -> 0fec26b9-8a0c-4dfc-b842-fb7cf4697924 -> Assistant -> Problem Exploration and Design Specification -> Problem Statement -> Core Components -> Data Packing -> Data Unpacking -> Operation Interfaces -> Script Generation -> Specifications -> aaa28cbe-9139-4539-915e-cee347975b63 -> User -> 2d6e1ca0-1786-4102-b30e-5545b9b2f1e0 -> Assistant -> aaa2fcae-5154-4dac-91c6-f8c98e0dba1f -> User -> e7d6cadc-2ed5-4673-aa24-5eabdf011818 -> Assistant -> 4ab984b5-d8c1-4463-83b0-dd85ff18f35f -> Tool -> 2e7a6320-a857-4f06-9c46-2438d80bb331 -> Assistant -> 30890fc7-d405-44a9-b4b4-5755b79309c7 -> Assistant -> 8cfa77c9-ffc0-42a1-b070-72225b99093d -> Tool -> 682274cb-508e-40ea-b309-1c8ae23ed8ad -> Assistant -> aaa2c4c9-6f1b-496c-98e9-fb1ccce31bff -> User -> f58e1ce0-a2bf-4b5a-8a83-c57d7ae7b39d -> Assistant -> fb30f088-a47f-4bd3-880d-f080eedfdb46 -> Tool -> 677e81ba-f9f5-4ba1-83af-d8d440a13496 -> Assistant -> aaa2c27f-0250-48cb-add7-fd54540b0234 -> User -> f02a8a00-3031-488f-bf57-8835c4ca4d6f -> Assistant
---
# Assistant

```python
from typing import Any, Dict
import logging

# Adding a logging setup for demonstration
logging.basicConfig(level=logging.INFO)

# Extend Operation ABC to include logging
class Operation(ABC):
    @abstractmethod
    def execute(self, log: logging.Logger) -> None:
        pass

    @abstractmethod
    def validate(self, log: logging.Logger) -> None:
        pass

    @abstractmethod
    def generate_code(self) -> str:
        pass

# Implement MoveFiles operation
class MoveFiles(Operation):
    def __init__(self, file_mapping: Dict[str, str]) -> None:
        """
        :param file_mapping: A dictionary where keys are source paths and values are destination paths.
        """
        self.file_mapping = file_mapping

    def execute(self, log: logging.Logger) -> None:
        pass

    def validate(self, log: logging.Logger) -> None:
        pass

    def generate_code(self) -> str:
        code_lines = []
        for src, dest in self.file_mapping.items():
            code_line = f"shutil.move('{src}', '{dest}')"
            code_lines.append(code_line)
        return '\n    '.join(code_lines)

# Update generate_script to include logging
def generate_script(operations: List[Operation], packed_data: str) -> str:
    operations_code = "\n    ".join([op.generate_code() for op in operations])
    
    template = textwrap.dedent(f"""
        import base64
        import tarfile
        import tempfile
        import subprocess
        import shutil
        import logging

        logging.basicConfig(level=logging.INFO)
        log = logging.getLogger(__name__)

        def main():
            log.info("Starting self-extracting script.")

            # Unpack Data
            log.info("Unpacking data...")
            packed_data = "{packed_data}"
            with tempfile.NamedTemporaryFile() as temp_file:
                temp_file.write(base64.b64decode(packed_data))
                temp_file.seek(0)
                with tarfile.open(fileobj=temp_file, mode="r:gz") as tar:
                    tar.extractall()
            log.info("Data unpacked.")

            # Execute Operations
            log.info("Executing operations...")
            {operations_code}
            log.info("Operations completed.")

        if __name__ == '__main__':
            main()
    """)
    return template

# Example usage with new MoveFiles operation and logging
file_mapping = {"some_source_file.txt": "some_dest_file.txt"}
operations = [InstallLibraries(["numpy", "pandas"]), MoveFiles(file_mapping)]
packed_data = pack_data(paths)
script = generate_script(operations, packed_data)

# Show a snippet of the generated script
print(script[:500] + "...")
```

[child ⬇️](#e866aa99-f1a7-4870-827b-8c06a0e3915a)

---

(main branch ⎇)
###### e866aa99-f1a7-4870-827b-8c06a0e3915a
[parent ⬆️](#f02a8a00-3031-488f-bf57-8835c4ca4d6f)
