---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (14).md
heading_stack: <root> -> b421fd60-2b52-4eee-9122-5a7806574998 -> System -> 0e0de881-5a7b-4301-9643-ccff084a4ddf -> System -> aaa24362-c889-42c5-afec-aae36a2536d8 -> User -> 5e125b51-4948-41c1-bdf3-93b510bdb1af -> Assistant -> Ideal API Design -> Helper Classes -> Class -> Decorator -> AnnotatedAttribute -> BaseClass -> CodeBlock -> Recursive Code Generation -> Handling Indentation -> Example Implementation -> aaa2b636-9271-4157-9924-1a308fab5317 -> User -> 3c3b81e1-8cd2-4341-91c2-7b030a68f9a1 -> Assistant -> Leveraging Dataclasses -> aaa2a536-29ee-411d-9f01-afe2796f7425 -> User -> ad160486-5d4d-45c6-83bb-efd81a90f8a0 -> Assistant -> Leveraging Dataclasses -> Concerns for a Robust Implementation -> Patterns and Techniques to Borrow -> aaa2ec09-e316-4cbb-b846-830f33c67f26 -> User -> a5788519-835a-45b5-b51d-528548cac670 -> Assistant -> 61aee1c3-e68d-40ae-809a-afc5d1724485 -> Tool -> 762c81fb-e886-4720-99d8-96aa98924ec0 -> Assistant -> a144d99e-52e8-4fbe-a36c-44d0f6b900d5 -> Assistant -> 65b27eb5-58f3-4b78-8ed6-c8c5a63ee58b -> Tool -> fd21876b-41e9-488e-a016-1196a389464a -> Assistant -> aaa2cc47-c3e4-41dd-b91f-9362a6cdc798 -> User -> adafa997-35c7-4e33-a059-887b09c0a065 -> Assistant -> 99c4ae27-09c1-4daf-a555-984d41627cd8 -> Tool -> 3f5c52b8-9cd5-4e33-a2db-aaaaa7ae66ae -> Assistant -> 7b3671ef-bbee-4ece-b946-3ea76b1c42ab -> Tool -> 41eb0b88-68d3-4f18-ac08-7dd7cbc0f8ab -> Assistant -> aaa242ae-a7de-4212-826a-5a06552dea7d -> User -> 6ad68595-4acf-4c55-b440-675b26d544ea -> Assistant -> 7279eb99-ce1f-44d2-b97d-13fb2be34713 -> Tool -> 9fdb06ab-a47d-4ed5-af6e-6ee6403e882f -> Assistant -> d237f1fe-6157-47cf-a72d-efc52f906d3e -> Tool -> 630afad1-5e04-457f-85b2-c57cacfed9b5 -> Assistant -> ecddbe34-eb76-4039-947f-146b22cd0e58 -> Tool -> d83574cc-b31e-46a2-b2f1-096f97e7a0d9 -> Assistant -> aaa223ad-09ad-4ce7-b1e3-af8f44c309e3 -> User -> 839ca330-0499-4806-9c1f-aed269f7f0eb -> Assistant -> 24d9917e-f952-44a7-9f8d-df39b92ab387 -> Tool -> 50458fd2-0605-4051-8517-abd2174c186a -> Assistant -> aaa2c392-bbec-489e-bb8d-988e4be56d9e -> User -> 7e239652-e5a7-4dba-a063-61b565e869bc -> Assistant -> 825ded95-be9e-4b87-bdea-c3ef377fdc4d -> Tool -> b024130a-44b4-4517-894a-6dd2f6254945 -> Assistant -> ec95673e-a6f7-4473-a2b5-9ef93a151bc7 -> Tool -> Test the code generation functions -> 5c8e55d4-4313-4b32-a1fd-306783220837 -> Assistant -> 1e5c8a07-9f73-424d-955d-6eaed4d4e7fb -> Tool -> Test the code generation functions -> c8d8d161-e953-4a92-9e27-bea47c3a57e6 -> Assistant -> aaa22760-2acf-4aa0-8a65-24dd28efc160 -> User -> ff247c3e-27ac-408a-9dd5-1ddfb91db297 -> Assistant -> ae5f6065-5782-435e-b0f7-2f5b858a37ca -> Tool
---
# Tool

==== Cell ID: 7df83cc4-3d0d-45e8-953a-7cb43ce1432a
Cell Type: code
Cell State: not_run
== Source ==
from typing import Union, List, Optional
from dataclasses import dataclass

@dataclass
class Parameter:
    name: str
    type: str
    default: Optional[Union[str, int, float, bool]] = None

@dataclass
class Function:
    name: str
    is_async: bool
    return_type: str
    parameters: List[Parameter]
    docstring: Optional[str] = None

@dataclass
class Module:
    name: str
    functions: List[Function]
    classes: List[Class]

    def add_function(self, function: Function):
        if any(f.name == function.name for f in self.functions):
            raise ValueError(f'Function with name {function.name} already exists.')
        self.functions.append(function)

    def add_class(self, cls: Class):
        if any(c.name == cls.name for c in self.classes):
            raise ValueError(f'Class with name {cls.name} already exists.')
        self.classes.append(cls)


[child ⬇️](#85d257c4-4dbf-41f7-ba29-d664fa6be18c)

---

(main branch ⎇)
###### 85d257c4-4dbf-41f7-ba29-d664fa6be18c
[parent ⬆️](#ae5f6065-5782-435e-b0f7-2f5b858a37ca)
