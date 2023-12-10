---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio Android am Integration.md
heading_stack: <root> -> 33028313-468b-4c7d-8352-6d2d1720ddca -> System -> 39ea25d0-5f9f-45ba-bf86-c730d4173350 -> System -> aaa27bdf-0126-4efe-993d-35b4823801e1 -> User -> 19604108-672c-4d31-99ac-0799fd1fd233 -> Assistant -> aaa200cc-93ac-4ba9-b80c-7d42d885a647 -> User -> 0d1d5bd6-4a44-44c5-8225-253c1660498c -> Assistant
---
# Assistant

To launch Waze with a specific target location, you'd typically use a command like:

```bash
am start -a "android.intent.action.VIEW" -d "waze://?ll=latitude,longitude&navigate=yes"
```

Here's how you can implement this functionality using the `run_am_command` function:

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

async def launch_waze(latitude: float, longitude: float) -> tuple[str, str]:
    waze_uri = f"waze://?ll={latitude},{longitude}&navigate=yes"
    args = ["start", "-a", "android.intent.action.VIEW", "-d", waze_uri]
    return await run_am_command(args)

# Example usage
async def main():
    latitude = 37.7749
    longitude = -122.4194
    stdout, stderr = await launch_waze(latitude, longitude)
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")

if __name__ == "__main__":
    asyncio.run(main())
```

This defines a `launch_waze` function that takes latitude and longitude as parameters and constructs the `am` command accordingly. Then it uses `run_am_command` to execute the command.

Would you like to add more features or is this sufficient for now?

[child ⬇️](#aaa2d7a8-e627-444c-b642-0016cca0ec5f)

---

(main branch ⎇)
###### aaa2d7a8-e627-444c-b642-0016cca0ec5f
[parent ⬆️](#0d1d5bd6-4a44-44c5-8225-253c1660498c)
