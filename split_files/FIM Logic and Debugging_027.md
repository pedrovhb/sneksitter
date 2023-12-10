---
file: /home/pedro/Documents/chatgpt_export/Markdown/FIM Logic and Debugging.md
heading_stack: <root> -> ccfb9a26-4159-40fe-b34e-021fbc2c3255 -> System -> ec3e3103-d827-4adc-88e3-b58200f32ea1 -> System -> aaa24904-7ec6-4e44-875c-31e21b7e874c -> User -> 3e42be5a-97b3-4ca4-9124-2ca3d4c32e56 -> Assistant -> aaa28121-a13e-461d-b618-50b1d0782f06 -> User -> 4e857123-36b1-4338-93ea-5120e13173e6 -> Assistant -> 758a5e3b-4420-4a7f-a358-2a439ec0d249 -> Tool -> db910fdc-c297-4dca-89b9-6f372fef740f -> Assistant -> 1. Recursive Factorial Function -> Prompt -> FIM Placeholder -> Test -> FIM Placeholder -> 2. 2D Point Class with Distance Calculation -> Prompt -> FIM Placeholder -> Test -> FIM Placeholder -> 3. Asynchronous URL Fetcher
---
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

