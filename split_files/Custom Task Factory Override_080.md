---
file: /home/pedro/Documents/chatgpt_export/Markdown/Custom Task Factory Override.md
heading_stack: <root> -> 2ab8dc66-9c51-4664-90e9-06291e31eb26 -> System -> b8afa332-1ea4-489a-809b-ea613254549b -> System -> aaa2f793-43f9-4f7d-b610-c0383df035ef -> User -> e51f6927-b9b1-45af-902f-ed18fb8f792f -> Assistant -> c0e1b261-c980-4a5f-b391-32529049bb4a -> Tool -> de2b3bf3-2dc0-4443-b496-b9989d9a7faa -> Assistant -> b7a1266d-90be-4300-ae02-79a0ca6ecfc3 -> Assistant -> 2e81c05c-a23c-4caf-a129-1e2533c68919 -> Tool -> 29673e15-8598-4546-a8b2-91dcc341abd3 -> Assistant -> aaa2dc8b-2afe-467b-9cb0-fef2e64c7057 -> User -> dc4a074b-2ef5-4fa3-bb90-2094af9666eb -> Assistant -> aaa269ee-9a58-44cb-980c-0c8b9ba11898 -> User -> 7785f4ab-a474-4361-9f01-95802d62b670 -> Assistant -> dfe64904-ae71-4b3c-be04-5854a684db3d -> Tool -> 9bf71f8d-8286-44f2-85e6-c09ea74adfc6 -> Assistant -> aaa219bf-0936-4f00-a962-6ef705160daf -> User -> 34efb5e6-8394-43e3-82a8-a5a82381e4d2 -> Assistant -> 60dddb70-837f-42a1-ba6e-e63f6141d185 -> Assistant -> aaa27460-184a-47e3-99f9-265884a48fb7 -> User -> c3d95b1a-3936-482a-82d0-034320c1d78a -> Assistant -> ccb1d924-5e80-4069-916d-d1136f8e58de -> Tool -> 6d156745-b263-47ed-9809-2e2147909933 -> Assistant -> aaa259c1-d2d8-4605-a976-a3ba28d47772 -> User -> f7791046-a63a-47f5-8cb2-fa18b8a72ab8 -> Assistant -> 69a2eeec-e3c7-4666-bc53-f8338f80a2bd -> Tool -> ded3e8c2-7045-4b54-ab70-754aff927d7c -> Assistant -> aaa2a0c9-fe29-4872-8cf3-3c2ef2f1f5ad -> User -> df3e4238-c6d3-4410-a49e-939fc8592c3d -> Assistant -> aaa2c059-de37-4e59-a75a-61cb1a07a38e -> User -> 469a8fb2-e7e3-4725-8102-b3c44c9aa145 -> Assistant -> b1a6c297-2055-4305-9445-5a992e1b92ef -> Assistant -> 552647be-cac6-4c23-9770-28ceedd74c83 -> Tool -> 3162a131-ffba-486e-aea5-02577a0dd079 -> Assistant -> aaa20173-dec2-4762-bf2f-74effbfd278e -> User -> ecc418a0-d805-475c-a697-88ff7f9222d4 -> Assistant -> 263c12af-b501-4357-b824-a2ae56be2d50 -> Tool -> 8d04e4ae-1fd0-4f44-8d29-339beb31bf4e -> Assistant -> aaa28efa-9b26-4bb4-9709-8c81455522c1 -> User -> b896fac8-ba75-42db-aeb0-83f8c07e993f -> Assistant -> 0d6441fa-564a-487c-a827-43f119897b5e -> Assistant
---
# Assistant

```python
# Reset graph for new example
G.clear()

# Async function to simulate rendering an element
async def render_element(element_id, future):
    await asyncio.sleep(0.1)
    print(f"Rendered element {element_id}")
    future.set_result(f"Element {element_id} done")

# Async function to simulate rendering a scene
async def render_scene(scene_id):
    print(f"Rendering scene {scene_id}")
    
    # Create futures for elements in the scene
    future1 = CustomFutureWithGraph()
    future2 = CustomFutureWithGraph()
    
    # Render elements
    task1 = asyncio.ensure_future(render_element(f"{scene_id}-E1", future1))
    task2 = asyncio.ensure_future(render_element(f"{scene_id}-E2", future2))
    
    await asyncio.gather(task1, task2)
    
    print(f"Rendered scene {scene_id}")

# Async function to simulate the main rendering task
async def render_main():
    print("Main rendering started")
    
    # Render scenes
    task1 = asyncio.ensure_future(render_scene("S1"))
    task2 = asyncio.ensure_future(render_scene("S2"))
    
    await asyncio.gather(task1, task2)
    
    print("Main rendering complete")

# Run main rendering task to populate the graph
await render_main()

# Visualize the graph
draw_graph(G)
```

[child ⬇️](#2bd5b431-8049-4c83-b5a2-ff4f57793794)

---

(main branch ⎇)
###### 2bd5b431-8049-4c83-b5a2-ff4f57793794
[parent ⬆️](#0d6441fa-564a-487c-a827-43f119897b5e)
