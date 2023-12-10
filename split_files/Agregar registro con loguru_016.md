---
file: /home/pedro/Documents/chatgpt_export/Markdown/Agregar registro con loguru.md
heading_stack: <root> -> bbc2eee3-d0e6-4dd5-a236-8aa929a8d323 -> System -> ce7fde3a-941f-4b7f-ac86-97a263e435dc -> System -> aaa26063-605a-4e6d-929e-590ee6e356d6 -> User -> f4b54abd-ea04-45dc-9235-d973f24c1a64 -> Assistant -> aaa2cf6b-49d5-489c-827b-3b1cdfb42d70 -> User -> 3cbcefc7-86a2-43c3-ab36-af1b0c4b80cc -> Assistant -> aaa22a4e-9be3-4101-83a6-e79c030b39b7 -> User -> b2576e34-4a1e-4fd0-ab10-0a6ad58bae62 -> Assistant
---
# Assistant

Certainly, to make sure that exceptions in asyncio tasks are raised immediately, we'll set up an exception handler that re-raises the caught exception.

Here's the modified code:

```python
from loguru import logger
import asyncio

def handle_exception(loop, context):
    msg = context.get("exception", context["message"])
    logger.error(f"Caught exception: {msg}")
    raise msg

# Set the custom exception handler
asyncio.get_event_loop().set_exception_handler(handle_exception)

class AsyncStreamer(BaseStreamer):
    # ... (existing code unchanged)

class AsyncTexter:
    # ... (existing code unchanged)

async def main(model, tokenizer):
    # ... (existing code unchanged)
```

The `handle_exception` function will act as our custom exception handler for the asyncio loop. When an exception occurs in an asyncio Task, this function will log the error and then re-raise the exception.

After defining this function, we set it as the exception handler for the asyncio event loop by using `asyncio.get_event_loop().set_exception_handler(handle_exception)`.

With this setup, any exceptions that occur during the asyncio operations will be immediately raised and logged.

---
