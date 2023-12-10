---
file: /home/pedro/Documents/chatgpt_export/Markdown/Cythonize Python Code_ No bitarray.md
heading_stack: <root> -> d04fc73a-cb67-45f0-9360-149501861721 -> System -> 7a0dbc21-310b-41da-bbf1-c4f90a0faa9d -> System -> aaa23d16-6d99-47c9-bd7c-01144097ce5f -> User -> a88a8d0c-5b5c-4858-ba0a-7b14b7abefd4 -> Assistant -> Notes: -> aaa2501a-fe50-4768-b0c6-ebb08536c259 -> User -> f863d624-425d-4a6f-8ff5-0b56701d1429 -> Assistant -> aaa2e0c2-ec24-4163-ab8b-32f7e3957972 -> User -> 7d198c0c-79df-4b05-8879-9bb7f8b1b35d -> Assistant -> Step 1: Install Cython -> Step 2: Save the Cython Code -> Step 3: Create a `setup.py` File -> Step 4: Compile the Cython Code -> Step 5: Import and Use in Python -> aaa21b34-8d49-47ae-8380-83115fbdbaaf -> User
---
# User

Error compiling Cython file:
------------------------------------------------------------
...
    (x, y): reduce(or_, [coords_braille_mapping[(x, yy)] for yy in range(y + 1)], 0)
    for x in range(2)
    for y in range(4)
}

cpdef str coords_to_braille(*coords: Tuple[int, int], bint filled=False):
                            ^
------------------------------------------------------------

brailliant/core.pyx:56:28: Expected ')', found '*'
T

[child ⬇️](#e6d3673c-4869-4f65-9eae-1d01be664be3)

---

(main branch ⎇)
###### e6d3673c-4869-4f65-9eae-1d01be664be3
[parent ⬆️](#aaa21b34-8d49-47ae-8380-83115fbdbaaf)
