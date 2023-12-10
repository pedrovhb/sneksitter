---
file: /home/pedro/Documents/chatgpt_export/Markdown/FIM Logic and Debugging.md
heading_stack: <root> -> ccfb9a26-4159-40fe-b34e-021fbc2c3255 -> System -> ec3e3103-d827-4adc-88e3-b58200f32ea1 -> System -> aaa24904-7ec6-4e44-875c-31e21b7e874c -> User -> 3e42be5a-97b3-4ca4-9124-2ca3d4c32e56 -> Assistant -> aaa28121-a13e-461d-b618-50b1d0782f06 -> User -> 4e857123-36b1-4338-93ea-5120e13173e6 -> Assistant -> 758a5e3b-4420-4a7f-a358-2a439ec0d249 -> Tool -> db910fdc-c297-4dca-89b9-6f372fef740f -> Assistant -> 1. Recursive Factorial Function
---
### 1. Recursive Factorial Function
#### Prompt
```plaintext
[INST]Implement a function to calculate the factorial of a given number using recursion.[/INST]
```
#### FIM Placeholder
```python
<MID>
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
#### Test
```plaintext
[INST]Test the factorial function with different inputs.[/INST]
```
#### FIM Placeholder
```python
<MID>
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
```

