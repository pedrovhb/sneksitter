---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (13).md
heading_stack: <root> -> e10c2f77-8080-42ec-af42-a3887b76def9 -> System -> 83d65b0b-2baa-449b-b718-d2b8cc114684 -> System -> aaa2bcea-4758-4eec-8700-5edd0f828f38 -> User -> Goals:
---
### Goals:

1. **Compile C Code into a Shared Library**: The C code simulates a synthetic sensor data generator. Compile this into a shared library (.so file).

2. **Python CFFI Interface**: Write Python code using CFFI to interface with this C shared library. Implement this within a Python class that adheres to the iterator protocol (`__iter__` and `__next__` methods).

3. **Customization and Realism**: The Python class should allow customization of sensor characteristics like frequency for each axis. The C code should generate realistic sensor data based on these frequencies, using sine and cosine functions with added noise.

4. **Iterate Over Sensor Data**: Demonstrate that you can iterate over the sensor data in Python using a `for` loop.

