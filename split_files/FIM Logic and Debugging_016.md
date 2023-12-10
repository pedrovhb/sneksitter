---
file: /home/pedro/Documents/chatgpt_export/Markdown/FIM Logic and Debugging.md
heading_stack: <root> -> ccfb9a26-4159-40fe-b34e-021fbc2c3255 -> System -> ec3e3103-d827-4adc-88e3-b58200f32ea1 -> System -> aaa24904-7ec6-4e44-875c-31e21b7e874c -> User -> 3e42be5a-97b3-4ca4-9124-2ca3d4c32e56 -> Assistant -> aaa28121-a13e-461d-b618-50b1d0782f06 -> User -> 4e857123-36b1-4338-93ea-5120e13173e6 -> Assistant -> 758a5e3b-4420-4a7f-a358-2a439ec0d249 -> Tool -> db910fdc-c297-4dca-89b9-6f372fef740f -> Assistant
---
# Assistant

Here are some interesting Fill-in-the-Middle (FIM) prompts to test code generation capabilities:

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

### 2. 2D Point Class with Distance Calculation
#### Prompt
```plaintext
[INST]Write a Python class that represents a 2D point.[/INST]
```
#### FIM Placeholder
```python
<MID>
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
```
#### Test
```plaintext
[INST]Extend the class to calculate the distance between two points.[/INST]
```
#### FIM Placeholder
```python
<MID>
    def distance(self, other: 'Point') -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
```

### 3. Asynchronous URL Fetcher
#### Prompt
```plaintext
[INST]Write an asynchronous function that fetches data from a given URL.[/INST]
```
#### FIM Placeholder
```python
<MID>
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text
```
#### Test
```plaintext
[INST]Test the asynchronous function by fetching data from multiple URLs.[/INST]
```
#### FIM Placeholder
```python
<MID>
    url1 = 'http://example.com'
    url2 = 'http://example.org'
    data1, data2 = await asyncio.gather(fetch_data(url1), fetch_data(url2))
```

### 4. Reverse a Linked List
#### Prompt
```plaintext
[INST]Implement a function that reverses a linked list.[/INST]
```
#### FIM Placeholder
```python
<MID>
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev
```
#### Test
```plaintext
[INST]Verify the reverse function by testing it with a sample linked list.[/INST]
```
#### FIM Placeholder
```python
<MID>
    head = Node(1, Node(2, Node(3)))
    reversed_head = reverse_linked_list(head)
    assert reversed_head.value == 3
```

### 5. Serialize and Deserialize Binary Tree
#### Prompt
```plaintext
[INST]Write a function to serialize and deserialize a binary tree.[/INST]
```
#### FIM Placeholder
```python
<MID>
    if root is None:
        return 'null,'
    return f'{root.val},' + serialize(root.left) + serialize(root.right)
```
#### Test
```plaintext
[INST]Test the serialization and deserialization functions.[/INST]
```
#### FIM Placeholder
```python
<MID>
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    serialized = serialize(root)
    deserialized = deserialize(serialized)
    assert deserialized.val == 1
```

Feel free to use these for your Fill-in-the-Middle tests.

---
