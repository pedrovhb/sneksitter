---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio Android am Integration.md
heading_stack: <root> -> 33028313-468b-4c7d-8352-6d2d1720ddca -> System -> 39ea25d0-5f9f-45ba-bf86-c730d4173350 -> System -> aaa27bdf-0126-4efe-993d-35b4823801e1 -> User -> 19604108-672c-4d31-99ac-0799fd1fd233 -> Assistant
---
# Assistant

Certainly, to integrate with the `am` Android CLI tool using asyncio, you can use `asyncio.create_subprocess_exec` to run the commands asynchronously.

Here's a basic example. The code defines a function `run_am_command` which takes the `am` command arguments as a list of strings and runs it asynchronously. It returns stdout and stderr as strings.

```python
import asyncio

async def run_am_command(args: list[str]) -> tuple[str, str]:
    cmd = ["am"] + args
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    return stdout.decode('utf-8'), stderr.decode('utf-8')

# Example usage
async def main():
    stdout, stderr = await run_am_command(["start", "-n", "com.example.app/.MainActivity"])
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")

if __name__ == "__main__":
    asyncio.run(main())
```

In this example, the `am` command used is `am start -n com.example.app/.MainActivity`. Replace `com.example.app/.MainActivity` with the actual activity you want to start.

Would you like to proceed with this or refine it further?

[child ⬇️](#aaa200cc-93ac-4ba9-b80c-7d42d885a647)

---

(main branch ⎇)
###### aaa200cc-93ac-4ba9-b80c-7d42d885a647
[parent ⬆️](#19604108-672c-4d31-99ac-0799fd1fd233)
