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
