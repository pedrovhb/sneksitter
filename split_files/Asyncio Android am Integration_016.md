---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio Android am Integration.md
heading_stack: <root> -> 33028313-468b-4c7d-8352-6d2d1720ddca -> System -> 39ea25d0-5f9f-45ba-bf86-c730d4173350 -> System -> aaa27bdf-0126-4efe-993d-35b4823801e1 -> User -> 19604108-672c-4d31-99ac-0799fd1fd233 -> Assistant -> aaa200cc-93ac-4ba9-b80c-7d42d885a647 -> User -> 0d1d5bd6-4a44-44c5-8225-253c1660498c -> Assistant -> aaa2d7a8-e627-444c-b642-0016cca0ec5f -> User -> 3ff55b5a-274c-478b-bd3e-9258a0279985 -> Assistant
---
# Assistant

```python
from typing import List, Tuple, Optional

import asyncio

async def run_am_command(args: List[str]) -> Tuple[str, str]:
    cmd = ["am"] + args
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()

    return stdout.decode('utf-8'), stderr.decode('utf-8')

async def launch_activity(action: str, data_uri: Optional[str] = None, extras: Optional[List[str]] = None) -> Tuple[str, str]:
    args = ["start", "-a", action]
    
    if data_uri:
        args.extend(["-d", data_uri])
    
    if extras:
        args.extend(extras)
    
    return await run_am_command(args)

async def launch_waze(latitude: float, longitude: float) -> Tuple[str, str]:
    waze_uri = f"waze://?ll={latitude},{longitude}&navigate=yes"
    return await launch_activity("android.intent.action.VIEW", waze_uri)

# Example usage
async def main():
    latitude = 37.7749
    longitude = -122.4194
    stdout, stderr = await launch_waze(latitude, longitude)
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")

# Uncomment to run the example
# asyncio.run(main())
```

[child ⬇️](#d51f6070-5ab7-45c2-acb6-f9c08b10328e)

---

(main branch ⎇)
###### d51f6070-5ab7-45c2-acb6-f9c08b10328e
[parent ⬆️](#3ff55b5a-274c-478b-bd3e-9258a0279985)
