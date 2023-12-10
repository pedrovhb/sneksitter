---
file: /home/pedro/Documents/chatgpt_export/Markdown/Custom Task Factory Override.md
heading_stack: <root> -> 2ab8dc66-9c51-4664-90e9-06291e31eb26 -> System -> b8afa332-1ea4-489a-809b-ea613254549b -> System -> aaa2f793-43f9-4f7d-b610-c0383df035ef -> User -> e51f6927-b9b1-45af-902f-ed18fb8f792f -> Assistant -> c0e1b261-c980-4a5f-b391-32529049bb4a -> Tool -> de2b3bf3-2dc0-4443-b496-b9989d9a7faa -> Assistant -> b7a1266d-90be-4300-ae02-79a0ca6ecfc3 -> Assistant -> 2e81c05c-a23c-4caf-a129-1e2533c68919 -> Tool -> 29673e15-8598-4546-a8b2-91dcc341abd3 -> Assistant -> aaa2dc8b-2afe-467b-9cb0-fef2e64c7057 -> User -> dc4a074b-2ef5-4fa3-bb90-2094af9666eb -> Assistant -> aaa269ee-9a58-44cb-980c-0c8b9ba11898 -> User -> 7785f4ab-a474-4361-9f01-95802d62b670 -> Assistant -> dfe64904-ae71-4b3c-be04-5854a684db3d -> Tool -> 9bf71f8d-8286-44f2-85e6-c09ea74adfc6 -> Assistant -> aaa219bf-0936-4f00-a962-6ef705160daf -> User -> 34efb5e6-8394-43e3-82a8-a5a82381e4d2 -> Assistant -> 60dddb70-837f-42a1-ba6e-e63f6141d185 -> Assistant -> aaa27460-184a-47e3-99f9-265884a48fb7 -> User -> c3d95b1a-3936-482a-82d0-034320c1d78a -> Assistant -> ccb1d924-5e80-4069-916d-d1136f8e58de -> Tool -> 6d156745-b263-47ed-9809-2e2147909933 -> Assistant -> aaa259c1-d2d8-4605-a976-a3ba28d47772 -> User -> f7791046-a63a-47f5-8cb2-fa18b8a72ab8 -> Assistant -> 69a2eeec-e3c7-4666-bc53-f8338f80a2bd -> Tool -> ded3e8c2-7045-4b54-ab70-754aff927d7c -> Assistant -> aaa2a0c9-fe29-4872-8cf3-3c2ef2f1f5ad -> User -> df3e4238-c6d3-4410-a49e-939fc8592c3d -> Assistant -> aaa2c059-de37-4e59-a75a-61cb1a07a38e -> User -> 469a8fb2-e7e3-4725-8102-b3c44c9aa145 -> Assistant -> b1a6c297-2055-4305-9445-5a992e1b92ef -> Assistant -> 552647be-cac6-4c23-9770-28ceedd74c83 -> Tool -> 3162a131-ffba-486e-aea5-02577a0dd079 -> Assistant -> aaa20173-dec2-4762-bf2f-74effbfd278e -> User -> ecc418a0-d805-475c-a697-88ff7f9222d4 -> Assistant -> 263c12af-b501-4357-b824-a2ae56be2d50 -> Tool -> 8d04e4ae-1fd0-4f44-8d29-339beb31bf4e -> Assistant -> aaa28efa-9b26-4bb4-9709-8c81455522c1 -> User -> b896fac8-ba75-42db-aeb0-83f8c07e993f -> Assistant -> 0d6441fa-564a-487c-a827-43f119897b5e -> Assistant -> 2bd5b431-8049-4c83-b5a2-ff4f57793794 -> Tool -> 5ed50cb1-9380-4319-9831-239c7f69c2cb -> Assistant -> aaa2df5f-a385-4016-9b2e-994f0f288676 -> User -> d1a60220-1126-4b73-86e6-c6cff386f4ad -> Assistant -> a76cd8fc-5884-4b32-b7e5-553bb6970b7c -> Assistant -> 262869e5-302e-43e5-a7cf-ce3ee7872d50 -> Tool -> 49f1cbc5-3d8b-470a-9b40-af1a38a58b94 -> Assistant -> aaa2c561-6ef0-4b6b-b684-b8bdd6c120ad -> User -> 64182d00-1812-40d2-a844-a62a375c3111 -> Assistant -> Objective -> Desired Features -> Challenges -> Possible Approaches -> aaa217cf-c3f9-4e63-86ae-281455b9c484 -> User -> a7f2582a-6998-4d74-9cd8-302dc23dc7a6 -> Assistant -> aaa23a80-c279-45c3-97a5-ad7ff0c413dd -> User -> e355d4a5-d4f7-4266-8086-ee91ad97bd19 -> Assistant -> c5f30c0a-30e4-4d6e-bdf4-a6860650a7b9 -> Tool -> 2167abc6-c1ba-4032-954c-f6b4244c51fb -> Assistant -> aaa28fad-eddd-465d-883b-0193b0e9f2f2 -> User -> ece7802a-3bdb-4f2d-89ad-4c326adcfc98 -> Assistant -> dfa785b3-5f09-44f5-863d-5a83fbd8647e -> Tool -> ae542501-4e95-4537-842a-b4649e94fd5b -> Assistant -> aaa2637d-a83c-4af1-962f-1f6655f5ebc9 -> User -> 6b68743c-3c57-4809-9516-8bc5a59cd315 -> Assistant -> dedca6d5-9880-4212-9d3d-8229c40eb3a2 -> Assistant
---
# Assistant

```python
# Refine the AsyncFlowGraph class for better debugging
class AsyncFlowGraph:
    def __init__(self):
        self.G = nx.DiGraph()
    
    def add_task(self, description):
        task = asyncio.current_task()
        task_id = id(task)
        self.G.add_node(task_id, type="Task", description=description)
        return task_id

    def add_future(self, description, future):
        future_id = id(future)
        self.G.add_node(future_id, type="Future", description=description)
        return future_id

    def add_edge(self, from_id, to_id, relationship):
        self.G.add_edge(from_id, to_id, type=relationship)

# Create a new instance of AsyncFlowGraph
flow_graph = AsyncFlowGraph()

# Refine Custom Future subclass for better debugging
class CustomFutureForGraphRefined(asyncio.Future):
    def __init__(self, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = flow_graph.add_future(description, self)
        
    def set_result(self, result):
        parent_task = asyncio.current_task()
        parent_task_id = id(parent_task)
        flow_graph.add_edge(parent_task_id, self.id, "sets_result")
        super().set_result(result)

# Refine Custom Task Factory for better debugging
def custom_task_factory_for_graph_refined(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    description = coro.__name__  # Using the coroutine function name for the description
    task_id = flow_graph.add_task(description)
    return task

# Set refined custom task factory
current_loop.set_task_factory(custom_task_factory_for_graph_refined)

# Reset the graph for debugging
G.clear()

# Run test functions to populate the refined graph
await render_main_for_graph()

# Draw the populated graph
draw_improved_graph(flow_graph.G)

# Display graph nodes and edges for debugging
flow_graph.G.nodes(data=True), flow_graph.G.edges(data=True)
```

[child ⬇️](#6c1d191d-36b1-4bef-b8ed-8ff304c67567)

---

(main branch ⎇)
###### 6c1d191d-36b1-4bef-b8ed-8ff304c67567
[parent ⬆️](#dedca6d5-9880-4212-9d3d-8229c40eb3a2)
