---
file: /home/pedro/Documents/chatgpt_export/Markdown/Detecting Deadlocks in asyncio.md
heading_stack: <root> -> 37087476-f357-4c07-bb9a-cbd6f7ce8936 -> System -> 18a374ea-54f7-408a-829d-f60766f75e3a -> System -> aaa207d7-d8c9-4cfe-a09c-7a8c955a3979 -> User -> ce028723-44f2-4667-b510-9f27ad1b64ea -> Assistant -> Detecting Deadlocks in `asyncio` -> aaa22514-b1a5-43b2-be50-0b517693a92e -> User -> 387cf5fb-37d4-4a9b-8cdf-f50ec9986d1f -> Assistant -> Components of a Resource Allocation Graph -> Using Resource Allocation Graphs to Detect Deadlocks -> Implementing RAG in Python with `asyncio` -> aaa25dfd-3475-43cd-a062-f771187415f1 -> User -> f45eab83-6841-4049-87c6-81bd58a3f62b -> Assistant
---
# Assistant

```python
# Importing necessary libraries
import asyncio
import networkx as nx
from networkx.algorithms.cycles import simple_cycles

# Initialize a NetworkX directed graph to represent the Resource Allocation Graph
rag = nx.DiGraph()

# Custom Task/Future Factory
class CustomTask(asyncio.Task):
    def __init__(self, coro, *, loop=None, name=None):
        super().__init__(coro, loop=loop, name=name)
        self.id = id(self)
        # Add the task node to the RAG
        rag.add_node(self.id, type='task')

    async def acquire(self, resource):
        # Add request edge from task to resource
        rag.add_edge(self.id, resource, type='request')
        # Check for cycles in RAG before acquiring the resource
        if any(simple_cycles(rag)):
            raise RuntimeError("Deadlock detected")
        # Simulate resource acquisition (using a simple lock here for demonstration)
        await asyncio.sleep(0.1)
        # Change request edge to assignment edge
        rag.add_edge(resource, self.id, type='assignment')
        rag.remove_edge(self.id, resource)
        
    async def release(self, resource):
        # Remove assignment edge from resource to task
        rag.remove_edge(resource, self.id)
        # Optionally, check for cycles again
        if any(simple_cycles(rag)):
            raise RuntimeError("Deadlock detected")

# Resource representation
class Resource:
    def __init__(self, name):
        self.name = name
        # Add the resource node to the RAG
        rag.add_node(self.name, type='resource')

# Example usage
async def task_coroutine(task_name, resource1, resource2):
    task = CustomTask(current_task := asyncio.current_task(), name=task_name)
    await task.acquire(resource1.name)
    await asyncio.sleep(0.1)
    await task.acquire(resource2.name)
    await asyncio.sleep(0.1)
    await task.release(resource2.name)
    await task.release(resource1.name)

resource_a = Resource("Resource_A")
resource_b = Resource("Resource_B")

# Creating tasks
task1 = asyncio.create_task(task_coroutine("Task_1", resource_a, resource_b))
task2 = asyncio.create_task(task_coroutine("Task_2", resource_b, resource_a))

# Running the event loop
try:
    asyncio.run(asyncio.gather(task1, task2))
except RuntimeError as e:
    print(f"Exception caught: {e}")
```

[child ⬇️](#b6c29585-72e2-42dc-acc1-722073cdd9d6)

---

(other branch ⎇)
###### b6c29585-72e2-42dc-acc1-722073cdd9d6
[parent ⬆️](#f45eab83-6841-4049-87c6-81bd58a3f62b)
