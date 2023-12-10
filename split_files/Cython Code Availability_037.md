---
file: /home/pedro/Documents/chatgpt_export/Markdown/Cython Code Availability.md
heading_stack: <root> -> bd37907b-67fb-4b78-b0fb-713ee5c6223b -> System -> 63bfd26c-ef54-45e1-9f04-fd6737297b25 -> System -> aaa2bcf0-05ef-44ed-97ee-fdece4f86d1e -> User -> 35ba7f8e-54c5-40bf-a04a-47391a0a871f -> Assistant -> 2d32b217-45dc-4604-af02-216e0e496a3b -> Tool -> 276f8111-9137-42a5-a7c8-b6a3bb187f72 -> Assistant -> aaa22d0e-0d3d-4e9c-8649-5b23012611cf -> User -> fbeb3ea1-d269-44f8-8fb1-4266b515ef66 -> Assistant -> Comprehensive Guide to Cython for Python Experts -> Introduction -> Setup and Installation -> Cython Syntax Basics -> Cythonizing Python Code -> Interfacing with C/C++ -> Performance Optimization -> Memory Management -> Parallelism -> Error Handling and Debugging -> Advanced Features -> Best Practices -> Case Studies -> Conclusion -> aaa291a0-5a29-4887-892f-3cd0f7d56f8f -> User -> 90ecde42-a64b-4a33-a218-878702e327fd -> Assistant -> Chapter: Cython Syntax Basics -> Introduction -> Defining Functions and Variables
---
### Defining Functions and Variables

#### Functions

In Cython, you can define functions in two primary ways: using `def` or `cdef`.

- `def`: Functions declared using `def` are Python functions and can be called from Python as well as Cython code.
  
  ```python
  def py_function(x):
      return x * 2
  ```

- `cdef`: Functions declared using `cdef` are C functions and can only be called within Cython code.
  
  ```python
  cdef int c_function(int x):
      return x * 2
  ```

> **Info**: Using `cdef` to declare a function enables Cython to bypass Python's function-call overhead, making the function faster.

#### Variables

In Cython, you can define variables without type annotations, just like in Python, or with static type declarations.

- Without type: 
  
  ```python
  var = 10
  ```

- With type:

  ```python
  cdef int var = 10
  ```

> **Tip**: Explicitly typing variables can significantly speed up operations involving those variables.

