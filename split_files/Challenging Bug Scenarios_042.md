---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior -> aaa2da28-e469-4aab-accc-b52d7aa18433 -> User -> 24b2a49b-4ec7-4808-8cb2-7a985f77921f -> Assistant -> Scenario 1: Nested Async Calls Hiding a Deadlock -> Scenario 2: Data Corruption due to Inconsistent Global State -> Scenario 3: Intermittent Failure due to Uninitialized Variable -> Scenario 4: Floating-Point Error in Financial Calculation -> aaa2f2f6-ffae-4515-a01d-078e412919d2 -> User -> ea8eacaa-5157-4848-b99b-ba96457a30cb -> Assistant -> Possible Ideas for Complex Scenario -> Selected Scenario: Time Series Data Analysis for Stock Prices -> aaa2c237-68df-47bf-9959-baeb804e76b0 -> User -> eb42b169-6cb1-45a4-9f6d-5175e7cd6d59 -> Assistant -> Revised Scenario: Web Server Request Handler -> Context -> Bug -> Twists -> aaa26fef-a7d8-43cb-a41f-1d1f07b4b07c -> User -> 0469f307-315f-4abd-a1ce-0079b4c214b0 -> Assistant -> aaa299f1-d3ee-4781-809d-87cb8c9b9767 -> User -> 9830efd5-bea1-4d3e-b660-7eb64cc3ad84 -> Assistant
---
# Assistant

```python
from typing import Dict, Tuple, Callable, Any
import json
from collections import OrderedDict

# Initialize the cache and its max size
CACHE_SIZE = 3
cache = OrderedDict()

# Middleware to cache responses
def caching_middleware(route_handler: Callable[[Dict[str, Any]], str]) -> Callable[[Dict[str, Any]], str]:
    def wrapper(request: Dict[str, Any]) -> str:
        if request['method'] == 'GET':
            if request['path'] in cache:
                return cache[request['path']]
        
        response = route_handler(request)
        
        if request['method'] == 'GET':
            if len(cache) >= CACHE_SIZE:
                cache.popitem(last=False)  # Remove the oldest item
            cache[request['path']] = response

        return response
    
    return wrapper

# Simulated route handlers
@caching_middleware
def handle_user_info(request: Dict[str, Any]) -> str:
    if request['method'] == 'POST':
        return json.dumps({"status": "user updated"})
    return json.dumps({"user": "John Doe"})

@caching_middleware
def handle_product_info(request: Dict[str, Any]) -> str:
    return json.dumps({"product": "Laptop"})

# Route table
ROUTES: Dict[str, Callable[[Dict[str, Any]], str]] = {
    '/user': handle_user_info,
    '/product': handle_product_info,
}

# Simulated web server request handler
def handle_request(request: Dict[str, Any]) -> None:
    path = request['path']
    route_handler = ROUTES.get(path)
    
    if not route_handler:
        print("404 Not Found")
        return
    
    response = route_handler(request)
    print(f"Response: {response}")

# Simulated incoming requests
requests = [
    {"method": "GET", "path": "/user", "headers": {}},
    {"method": "GET", "path": "/product", "headers": {}},
    {"method": "GET", "path": "/product", "headers": {}},  # Filling the cache
    {"method": "POST", "path": "/user", "headers": {"Content-Type": "application/json"}},  # Should trigger cache eviction
    {"method": "GET", "path": "/user", "headers": {}},  # Should not return cached POST response
]

# Handle incoming requests
for request in requests:
    handle_request(request)

```

[child ⬇️](#453b2f6c-2787-45cf-b480-48b77cfcb1bc)

---

(main branch ⎇)
###### 453b2f6c-2787-45cf-b480-48b77cfcb1bc
[parent ⬆️](#9830efd5-bea1-4d3e-b660-7eb64cc3ad84)
