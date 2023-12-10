---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant -> e3e20cb1-d7af-4b3a-8989-0f635e7b7b37 -> Assistant -> 0f60f5d4-ccff-409d-a801-fe2e8e24b7e0 -> Tool -> 2dde9631-ce8a-470f-a73d-efdd18304420 -> Assistant -> efc03986-9e2b-44f4-b7a8-f1ea222b2fe6 -> Assistant -> 6ed08e43-230e-4b6e-a185-fa455f069e46 -> Tool -> b8da2c4b-9db2-47d7-a2af-389be4befc5f -> Assistant -> db2e1dd1-0795-480b-bc14-771d0eb39e4d -> Assistant -> e7105360-42e1-44dc-b634-fe0c00e4e999 -> Tool -> ca3c2937-19b7-4c14-9f94-a96c4aa48bf4 -> Assistant -> aaa241ef-101a-4eeb-93d2-e8d8919d06d9 -> User -> 0d4987c7-80b3-4264-a7cb-373f269f73d6 -> Assistant -> aaa2d51e-8b35-443b-8c51-50d3a8740574 -> User -> 4b0ff9a6-0c97-4d93-b7b8-d64c70c39fe0 -> Assistant -> aaa29522-caba-4582-81f4-fa790988a5cb -> User -> 2671227c-f5b3-4e6a-8bc8-cf8625b9df85 -> Assistant -> 0378287d-290e-4e7d-b03a-e96ab29bc45d -> Tool -> 8be38330-dba2-463c-acb5-18b403657055 -> Assistant -> c66b0691-c55b-4e68-96b1-91f3dc82f4b7 -> Assistant -> a3e0a4c8-fc88-4485-9059-7f406744f6b4 -> Tool -> 419e449b-8c14-40cc-a0c1-b3e7c21548f0 -> Assistant -> 736f7993-431a-4b09-ac29-e009d83997db -> Assistant -> aaa2ce72-49ee-49cc-8893-081472477efe -> User -> f6a699fc-9589-496c-bb9d-98b527929107 -> Assistant -> 589de901-2a5c-4250-85b4-341a154c4e14 -> Tool -> e56f4805-ab35-4bb2-9722-f0eec9acaf00 -> Assistant -> aaa22608-4043-42da-9c29-4a1a3e230baa -> User -> c8bd61ab-d7b3-4ea0-8ed8-a46f94890ef6 -> Assistant -> 159991f9-95da-4347-83e1-7b99538798c7 -> Tool -> 84a3281c-d2e7-4cab-b27c-9806745c1e1a -> Assistant -> aaa2be14-d179-458d-b54e-7c33eb48609e -> User -> 62b6f78a-e207-4caf-acf5-bc872a343ea3 -> Assistant -> 4fb74221-c79f-4794-bd21-74a14a2868bd -> Tool -> ebbc3941-713f-4615-9515-556f91842fda -> Assistant -> 19f6532d-da06-496e-92e8-c7cf8fcf7cf8 -> Assistant -> aaa20df5-4e26-41ea-a5d3-30d3962ad2ea -> User -> 6b0f7f5f-81a2-4a4b-b055-c61966bb7f2f -> Assistant -> a23783ae-2c26-493b-8b99-7d5f120745b8 -> Tool -> 5b40caa3-bc77-4696-9fea-f7947274addf -> Assistant -> aaa22b75-40f0-4a3e-acbd-e9c41ac296a8 -> User -> 66732f5a-e474-43b0-8314-d3fdd7833701 -> Assistant -> 93109907-c6bd-491d-968e-b612db687b94 -> Tool -> 25a38dc3-7e67-4b59-84f8-7feb728de447 -> Assistant -> aaa2510c-5d67-4b15-8887-bf2ba344dac5 -> User -> 4b8b2aa7-6ba9-469a-b4bb-3b422284aa9c -> Assistant -> 212fee89-5092-4740-8d09-8685b8dbb043 -> Tool -> 78495154-2bfc-4427-b10b-395157cf2877 -> Assistant -> aaa2a0ba-710a-463b-99fb-1f4e32aa9255 -> User -> b5b2bb6d-f015-48e5-bf0d-0986f2a81596 -> Assistant -> 656de68e-c572-4677-a02b-455a242ccc4f -> Tool -> cc242b00-a614-40ed-869f-01c6d635e217 -> Assistant -> aaa2ef16-eae4-49d1-97f1-2ab27d6e7b5e -> User -> 6573515a-447d-457d-9586-4344efb020c8 -> Assistant -> aaa2ad87-4fb6-4584-8d13-c50775a298cc -> User -> a1f50531-8c6f-4aae-95a8-1733fe5015a9 -> Assistant -> Alternatives to Mixins: -> aaa2010b-6b1f-465b-9985-89b40e46682f -> User -> b09ea480-346f-4390-8b15-d6ecd544fd4c -> Assistant
---
# Assistant

In Python, protocols are primarily used for structural type checking. They describe a contract that classes must adhere to but do not provide a mechanism for sharing implementation details. Unlike interfaces in some other languages, Python protocols do not define functionality; they define a "shape" that other classes should have.

However, you can pair protocols with concrete base classes that provide default implementations. In this way, you define the contract with a protocol and provide a base implementation in a separate class. Classes can then inherit from these base classes to get the default functionality, or implement the protocol from scratch if they need something different.

Here's a simplified example:

```python
from typing import Protocol

# Define the protocol
class Mappable(Protocol):
    async def map(self, iterable):
        pass

# Define a base class with default functionality
class MappableBase(Mappable):
    async def map(self, iterable):
        async for item in iterable:
            yield await self(item)

# Your main class could then use these base classes
class FuncWrapper(MappableBase):
    def __init__(self, func):
        self.func = func

    async def __call__(self, *args, **kwargs):
        return await self.func(*args, **kwargs)
```

In this setup, `Mappable` defines the contract (i.e., you must have a `map` method), and `MappableBase` provides a default implementation. `FuncWrapper` then inherits from `MappableBase` to get this default behavior.

While this approach provides a clean separation between interface and implementation, it's a bit more verbose than mixins and may be overkill for a library of this size. It's more commonly used in larger, more complex projects where you need a lot of flexibility in how classes can be extended.

Would you like to proceed with this approach, or would another be more to your liking?

[child ⬇️](#aaa2f5bc-607d-443c-9734-1eb042eab85f)

---

(main branch ⎇)
###### aaa2f5bc-607d-443c-9734-1eb042eab85f
[parent ⬆️](#b09ea480-346f-4390-8b15-d6ecd544fd4c)
