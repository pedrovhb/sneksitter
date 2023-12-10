---
file: /home/pedro/Documents/chatgpt_export/Markdown/Cythonize Python Code_ No bitarray.md
heading_stack: <root> -> d04fc73a-cb67-45f0-9360-149501861721 -> System -> 7a0dbc21-310b-41da-bbf1-c4f90a0faa9d -> System -> aaa23d16-6d99-47c9-bd7c-01144097ce5f -> User -> a88a8d0c-5b5c-4858-ba0a-7b14b7abefd4 -> Assistant -> Notes: -> aaa2501a-fe50-4768-b0c6-ebb08536c259 -> User -> f863d624-425d-4a6f-8ff5-0b56701d1429 -> Assistant -> aaa2e0c2-ec24-4163-ab8b-32f7e3957972 -> User -> 7d198c0c-79df-4b05-8879-9bb7f8b1b35d -> Assistant -> Step 1: Install Cython -> Step 2: Save the Cython Code -> Step 3: Create a `setup.py` File -> Step 4: Compile the Cython Code -> Step 5: Import and Use in Python
---
### Step 5: Import and Use in Python

After compilation, you should see a file named `braille_cy.cpython-XXm-<platform>.so` in your directory (the name may vary depending on your Python version and platform).

Now you can import this compiled module in your Python code:

```python
import braille_cy

print(braille_cy.coords_to_braille((0, 0), (1, 0)))  # Output should be '⣀'
```

You can also use this compiled module just like any other Python module, but it should execute more quickly than the pure Python version.

[child ⬇️](#aaa21b34-8d49-47ae-8380-83115fbdbaaf)

---

(main branch ⎇)
###### aaa21b34-8d49-47ae-8380-83115fbdbaaf
[parent ⬆️](#7d198c0c-79df-4b05-8879-9bb7f8b1b35d)
