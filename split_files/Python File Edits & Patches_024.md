---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python File Edits & Patches.md
heading_stack: <root> -> d65e480f-8595-4e4f-a96c-ce3434873813 -> System -> 2d1d2f48-e6fe-4a7a-b2e8-7c38ee3ce43d -> System -> aaa28854-ea24-4096-a1b3-65acbd78ce34 -> User -> 229b3159-3937-4139-8002-dab8432ea6b7 -> Assistant -> 0d19e97d-592a-440e-89b1-0cc080576d0d -> Tool -> 4007542a-2b2c-42a9-b987-cd8ef54d4240 -> Assistant -> aaa2e46a-0bd8-496c-a6ea-778fe58489c5 -> User -> cce558b4-222f-4027-9320-09717c4dbbef -> Assistant -> a3459690-5e17-400a-b914-28c453d3f714 -> Tool -> 9f2b08be-207c-48fe-a9ec-871a422e49c8 -> Assistant -> aaa24cea-5a66-46e8-ab60-2fb20e5c4bc4 -> User -> 45e48c63-b8c0-4652-aceb-10d5d3ef6f57 -> Assistant
---
# Assistant

```python
# Create a more complex initial Python file
complex_file_name = 'complex_sample_file.py'
initial_content = """# Complex Sample Python File

def function_one():
    print("This is function one.")
    
def function_two():
    print("This is function two.")
    
def function_three():
    print("This is function three.")

# Repeated code block
for i in range(3):
    function_one()
    function_two()
    function_three()

if __name__ == '__main__':
    print("Main program starts here.")
    function_one()
    function_two()
    function_three()
"""

# Write the initial content to the file
complex_path = Path(complex_file_name)
complex_path.write_text(initial_content)

# List to store the patches
complex_patches = []

# Function to generate unified diff string with 1 context line
def generate_diff_one_line_context(old_text, new_text):
    return '\n'.join(list(difflib.unified_diff(old_text.splitlines(), new_text.splitlines(), lineterm='', fromfile='original', tofile='modified', n=1)))

# Edit 1: Change function names and loop range
edit_1_content = """# Complex Sample Python File

def func_one():
    print("This is func one.")
    
def func_two():
    print("This is func two.")
    
def func_three():
    print("This is func three.")

# Repeated code block
for i in range(4):
    func_one()
    func_two()
    func_three()

if __name__ == '__main__':
    print("Main program starts here.")
    func_one()
    func_two()
    func_three()
"""

# Generate diff for Edit 1
complex_patches.append(generate_diff_one_line_context(initial_content, edit_1_content))

# Edit 2: Remove repeated code block, add new functions
edit_2_content = """# Complex Sample Python File

def func_one():
    print("This is func one.")
    
def func_two():
    print("This is func two.")
    
def func_four():
    print("This is func four.")

def func_five():
    print("This is func five.")

if __name__ == '__main__':
    print("Main program starts here.")
    func_one()
    func_two()
    func_four()
    func_five()
"""

# Generate diff for Edit 2
complex_patches.append(generate_diff_one_line_context(edit_1_content, edit_2_content))

# Edit 3: Change main block, remove old functions, add new one
edit_3_content = """# Complex Sample Python File

def func_six():
    print("This is func six.")
    
def func_seven():
    print("This is func seven.")

def func_eight():
    print("This is func eight.")

if __name__ == '__main__':
    print("New main program.")
    func_six()
    func_seven()
    func_eight()
"""

# Generate diff for Edit 3
complex_patches.append(generate_diff_one_line_context(edit_2_content, edit_3_content))

# Save the final version of the complex file
complex_path.write_text(edit_3_content)

# Save each patch to a separate file
for i, patch in enumerate(complex_patches):
    patch_file_path = Path(f'complex_sample_file_patch_{i + 1}.txt')
    patch_file_path.write_text(patch)

# Move the files to the accessible directory for download
download_complex_path = Path('/mnt/data/complex_sample_file.py')
complex_path.rename(download_complex_path)

download_patch_paths = []
for i in range(len(complex_patches)):
    patch_file_path = Path(f'/mnt/data/complex_sample_file_patch_{i + 1}.txt')
    download_patch_paths.append(patch_file_path)

download_complex_path, download_patch_paths
```

[child ⬇️](#5b0cf78b-b5d0-4ef1-99d4-66e8553a85e1)

---

(main branch ⎇)
###### 5b0cf78b-b5d0-4ef1-99d4-66e8553a85e1
[parent ⬆️](#45e48c63-b8c0-4652-aceb-10d5d3ef6f57)
