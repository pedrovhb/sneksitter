---
file: /home/pedro/Documents/chatgpt_export/Markdown/Detecting Deadlocks in asyncio.md
heading_stack: <root> -> 37087476-f357-4c07-bb9a-cbd6f7ce8936 -> System -> 18a374ea-54f7-408a-829d-f60766f75e3a -> System -> aaa207d7-d8c9-4cfe-a09c-7a8c955a3979 -> User -> ce028723-44f2-4667-b510-9f27ad1b64ea -> Assistant -> Detecting Deadlocks in `asyncio` -> aaa22514-b1a5-43b2-be50-0b517693a92e -> User -> 387cf5fb-37d4-4a9b-8cdf-f50ec9986d1f -> Assistant -> Components of a Resource Allocation Graph -> Using Resource Allocation Graphs to Detect Deadlocks -> Implementing RAG in Python with `asyncio` -> aaa25dfd-3475-43cd-a062-f771187415f1 -> User -> f45eab83-6841-4049-87c6-81bd58a3f62b -> Assistant -> b6c29585-72e2-42dc-acc1-722073cdd9d6 -> Tool -> 753a37e7-4caf-4283-bc69-e6c3ed4d8a11 -> Assistant -> aaa24cd5-6313-4ab5-a8e0-3a01a36a2f91 -> User -> d256a5c8-25d4-4e12-8f23-2358fbfd0ebf -> Assistant -> 42feadbe-1395-40c0-8f20-3278284ea227 -> Tool -> 49db48c7-24df-495b-9e1a-171433d17971 -> Assistant -> 965a481d-04d0-46a9-ab43-b3503dc2e2b4 -> Assistant -> e7b40687-7008-42a1-9460-98541fd4c617 -> Tool -> ee95b322-1edd-4e67-a989-8a8ab39f88e8 -> Assistant -> 9fe1e873-9643-4edc-a95f-5cf8d519587e -> Assistant -> 6a55030b-9fe3-4cc7-8594-eae302b08e33 -> Tool -> 806bbcf3-849c-4b42-9a54-63fb197b0ec9 -> Assistant -> 7c10e2c3-6394-49c8-b0e5-b6698e1a565a -> Assistant -> 54845f93-f188-4521-92fb-73eab95ebcfb -> Tool -> 975536f5-3987-424a-ab40-f6786a573335 -> Assistant -> a7772d41-6cbc-42ab-b02a-6b4212f7b7f4 -> Assistant -> 93112e53-5832-48a0-9298-226568732913 -> Tool -> b15b384e-18ad-4f96-83f2-4860a21407b6 -> Assistant -> 299a560a-e87e-4fb8-aff4-c17228986602 -> Assistant -> 3b4f9e2f-512a-422f-b90e-f9678b6f85de -> Assistant -> aaa2ca36-73da-4a0c-a9d7-179bd806f9e9 -> User -> b108cf81-249e-47a3-82b1-791d88ae8486 -> Assistant
---
# Assistant

```python
# Importing necessary modules
import asyncio
import networkx as nx
from typing import Union, Callable

# Initialize the Resource Allocation Graph (RAG)
rag = nx.DiGraph()

# Custom Lock class to represent resources
class CustomLock:
    def __init__(self, name: str):
        self.name = name
        self._lock = asyncio.Lock()
        
    async def acquire(self):
        # Add request edge from task to resource in RAG
        task_name = asyncio.current_task().get_name()
        rag.add_edge(task_name, self.name, type='request')
        
        await self._lock.acquire()
        
        # Convert request edge to assignment edge in RAG
        rag[task_name][self.name]['type'] = 'assignment'
        
    def release(self):
        # Remove assignment edge from RAG
        task_name = asyncio.current_task().get_name()
        rag.remove_edge(task_name, self.name)
        
        self._lock.release()

# Custom Task Factory
def custom_task_factory(loop: asyncio.AbstractEventLoop,
                        coro: Union[Callable, asyncio.Future],
                        name: str = None) -> asyncio.Task:
    task = loop.create_task(coro)
    if name:
        task.set_name(name)
    
    # Add task node to RAG
    rag.add_node(name, type='task')
    return task

# Set custom task factory
asyncio.get_running_loop().set_task_factory(custom_task_factory)

# Function to detect cycles in RAG
def detect_deadlock() -> bool:
    return len(list(nx.simple_cycles(rag))) > 0

# Test tasks and resources
async def worker(lock: CustomLock, name: str):
    asyncio.current_task().set_name(name)
    await lock.acquire()
    await asyncio.sleep(1)
    lock.release()

async def main():
    lock1 = CustomLock('Lock1')
    
    task1 = asyncio.create_task(worker(lock1, 'Task1'))
    task2 = asyncio.create_task(worker(lock1, 'Task2'))
    
    await asyncio.gather(task1, task2)
    
    if detect_deadlock():
        print("Deadlock detected.")
    else:
        print("No deadlock detected.")

# Execute the main coroutine
await main()
```

[child ⬇️](#e3d44ddc-eb25-43a2-925c-4f17ff61feac)

---

(main branch ⎇)
###### e3d44ddc-eb25-43a2-925c-4f17ff61feac
[parent ⬆️](#b108cf81-249e-47a3-82b1-791d88ae8486)
