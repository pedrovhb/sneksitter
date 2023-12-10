---
file: /home/pedro/Documents/chatgpt_export/Markdown/FIM Logic and Debugging.md
heading_stack: <root> -> ccfb9a26-4159-40fe-b34e-021fbc2c3255 -> System -> ec3e3103-d827-4adc-88e3-b58200f32ea1 -> System -> aaa24904-7ec6-4e44-875c-31e21b7e874c -> User -> 3e42be5a-97b3-4ca4-9124-2ca3d4c32e56 -> Assistant -> aaa28121-a13e-461d-b618-50b1d0782f06 -> User -> 4e857123-36b1-4338-93ea-5120e13173e6 -> Assistant
---
# Assistant

```python
# Creating a list of interesting Fill-in-the-Middle (FIM) prompts to test code generation capabilities.
fim_prompts = [
    {
        "prompt": "[INST]Implement a function to calculate the factorial of a given number using recursion.[/INST]\n```<MID>\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```\n[INST]Test the factorial function with different inputs.[/INST]\n```<MID>\n    assert factorial(5) == 120\n    assert factorial(0) == 1\n    assert factorial(1) == 1\n```",
        "description": "Recursive factorial function"
    },
    {
        "prompt": "[INST]Write a Python class that represents a 2D point.[/INST]\n```<MID>\n    def __init__(self, x: float, y: float):\n        self.x = x\n        self.y = y\n```\n[INST]Extend the class to calculate the distance between two points.[/INST]\n```<MID>\n    def distance(self, other: 'Point') -> float:\n        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5\n```",
        "description": "2D Point class with distance calculation"
    },
    {
        "prompt": "[INST]Write an asynchronous function that fetches data from a given URL.[/INST]\n```<MID>\n    async with httpx.AsyncClient() as client:\n        response = await client.get(url)\n    return response.text\n```\n[INST]Test the asynchronous function by fetching data from multiple URLs.[/INST]\n```<MID>\n    url1 = 'http://example.com'\n    url2 = 'http://example.org'\n    data1, data2 = await asyncio.gather(fetch_data(url1), fetch_data(url2))\n```",
        "description": "Asynchronous URL fetcher"
    },
    {
        "prompt": "[INST]Implement a function that reverses a linked list.[/INST]\n```<MID>\n    prev = None\n    while head:\n        next_node = head.next\n        head.next = prev\n        prev = head\n        head = next_node\n    return prev\n```\n[INST]Verify the reverse function by testing it with a sample linked list.[/INST]\n```<MID>\n    head = Node(1, Node(2, Node(3)))\n    reversed_head = reverse_linked_list(head)\n    assert reversed_head.value == 3\n```",
        "description": "Reverse a linked list"
    },
    {
        "prompt": "[INST]Write a function to serialize and deserialize a binary tree.[/INST]\n```<MID>\n    if root is None:\n        return 'null,'\n    return f'{root.val},' + serialize(root.left) + serialize(root.right)\n```\n[INST]Test the serialization and deserialization functions.[/INST]\n```<MID>\n    root = TreeNode(1, TreeNode(2), TreeNode(3))\n    serialized = serialize(root)\n    deserialized = deserialize(serialized)\n    assert deserialized.val == 1\n```",
        "description": "Serialize and Deserialize Binary Tree"
    }
]

fim_prompts
```

[child ⬇️](#758a5e3b-4420-4a7f-a358-2a439ec0d249)

---

(main branch ⎇)
###### 758a5e3b-4420-4a7f-a358-2a439ec0d249
[parent ⬆️](#4e857123-36b1-4338-93ea-5120e13173e6)
