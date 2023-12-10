---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (14).md
heading_stack: <root> -> b421fd60-2b52-4eee-9122-5a7806574998 -> System -> 0e0de881-5a7b-4301-9643-ccff084a4ddf -> System -> aaa24362-c889-42c5-afec-aae36a2536d8 -> User -> 5e125b51-4948-41c1-bdf3-93b510bdb1af -> Assistant -> Ideal API Design -> Helper Classes -> Class -> Decorator -> AnnotatedAttribute -> BaseClass -> CodeBlock -> Recursive Code Generation -> Handling Indentation -> Example Implementation -> aaa2b636-9271-4157-9924-1a308fab5317 -> User -> 3c3b81e1-8cd2-4341-91c2-7b030a68f9a1 -> Assistant -> Leveraging Dataclasses -> aaa2a536-29ee-411d-9f01-afe2796f7425 -> User -> ad160486-5d4d-45c6-83bb-efd81a90f8a0 -> Assistant -> Leveraging Dataclasses -> Concerns for a Robust Implementation -> Patterns and Techniques to Borrow -> aaa2ec09-e316-4cbb-b846-830f33c67f26 -> User -> a5788519-835a-45b5-b51d-528548cac670 -> Assistant -> 61aee1c3-e68d-40ae-809a-afc5d1724485 -> Tool -> 762c81fb-e886-4720-99d8-96aa98924ec0 -> Assistant -> a144d99e-52e8-4fbe-a36c-44d0f6b900d5 -> Assistant -> 65b27eb5-58f3-4b78-8ed6-c8c5a63ee58b -> Tool -> fd21876b-41e9-488e-a016-1196a389464a -> Assistant -> aaa2cc47-c3e4-41dd-b91f-9362a6cdc798 -> User -> adafa997-35c7-4e33-a059-887b09c0a065 -> Assistant -> 99c4ae27-09c1-4daf-a555-984d41627cd8 -> Tool -> 3f5c52b8-9cd5-4e33-a2db-aaaaa7ae66ae -> Assistant -> 7b3671ef-bbee-4ece-b946-3ea76b1c42ab -> Tool -> 41eb0b88-68d3-4f18-ac08-7dd7cbc0f8ab -> Assistant -> aaa242ae-a7de-4212-826a-5a06552dea7d -> User -> 6ad68595-4acf-4c55-b440-675b26d544ea -> Assistant -> 7279eb99-ce1f-44d2-b97d-13fb2be34713 -> Tool -> 9fdb06ab-a47d-4ed5-af6e-6ee6403e882f -> Assistant -> d237f1fe-6157-47cf-a72d-efc52f906d3e -> Tool -> 630afad1-5e04-457f-85b2-c57cacfed9b5 -> Assistant -> ecddbe34-eb76-4039-947f-146b22cd0e58 -> Tool -> d83574cc-b31e-46a2-b2f1-096f97e7a0d9 -> Assistant -> aaa223ad-09ad-4ce7-b1e3-af8f44c309e3 -> User -> 839ca330-0499-4806-9c1f-aed269f7f0eb -> Assistant -> 24d9917e-f952-44a7-9f8d-df39b92ab387 -> Tool -> 50458fd2-0605-4051-8517-abd2174c186a -> Assistant -> aaa2c392-bbec-489e-bb8d-988e4be56d9e -> User -> 7e239652-e5a7-4dba-a063-61b565e869bc -> Assistant -> 825ded95-be9e-4b87-bdea-c3ef377fdc4d -> Tool -> b024130a-44b4-4517-894a-6dd2f6254945 -> Assistant -> ec95673e-a6f7-4473-a2b5-9ef93a151bc7 -> Tool -> Test the code generation functions -> 5c8e55d4-4313-4b32-a1fd-306783220837 -> Assistant -> 1e5c8a07-9f73-424d-955d-6eaed4d4e7fb -> Tool -> Test the code generation functions -> c8d8d161-e953-4a92-9e27-bea47c3a57e6 -> Assistant -> aaa22760-2acf-4aa0-8a65-24dd28efc160 -> User -> ff247c3e-27ac-408a-9dd5-1ddfb91db297 -> Assistant -> ae5f6065-5782-435e-b0f7-2f5b858a37ca -> Tool -> 85d257c4-4dbf-41f7-ba29-d664fa6be18c -> Assistant -> 5770ce90-232d-4d9e-829e-b435557f96e6 -> Tool -> 22eb2d61-05a9-4d90-8859-a244a26148a1 -> Assistant -> aaa20b4d-1b30-468a-8f4d-d3f645105568 -> User -> 4a06a807-ac53-4bfa-a5c8-83eceec233cb -> Assistant -> 6b0bb932-72f5-4f38-969f-6544c26fce02 -> Tool -> Test the Parameter, Function, and Module classes -> ffd06f5a-243d-4195-a6f2-73766c87b8ee -> Assistant -> 0b72deb1-12bb-45f6-9dcd-3c7b674e96b8 -> Tool -> Test the Parameter, Function, and Module classes
---
# Test the Parameter, Function, and Module classes

def test_new_classes():
    # Test Parameter
    param1 = Parameter(name='x', type='int')
    param2 = Parameter(name='y', type='str', default='default')
    assert param1.name == 'x'
    assert param1.type == 'int'
    assert param1.default is None
    assert param2.name == 'y'
    assert param2.type == 'str'
    assert param2.default == 'default'

    # Test Function
    func = Function(name='my_func', is_async=False, return_type='None', parameters=[param1, param2])
    assert func.name == 'my_func'
    assert func.is_async == False
    assert func.return_type == 'None'
    assert func.parameters == [param1, param2]

    # Test Module
    mod = Module(name='my_module', functions=[func], classes=[])
    assert mod.name == 'my_module'
    assert mod.functions == [func]
    assert mod.classes == []

    # Test add_function and add_class in Module
    func2 = Function(name='another_func', is_async=True, return_type='str', parameters=[])
    cls = Class(name='Person', bases=[], decorators=[], attributes=[])
    mod.add_function(func2)
    mod.add_class(cls)
    assert mod.functions == [func, func2]
    assert mod.classes == [cls]

    # Test for function name conflict
    try:
        mod.add_function(func2)
    except ValueError as e:
        assert str(e) == 'Function with name another_func already exists.'

    # Test for class name conflict
    try:
        mod.add_class(cls)
    except ValueError as e:
        assert str(e) == 'Class with name Person already exists.'

    print('All new class tests passed!')

test_new_classes()
== Output ==
All new class tests passed!


[child ⬇️](#329e5be8-7353-4730-829a-38e896190d9a)

---

(main branch ⎇)
###### 329e5be8-7353-4730-829a-38e896190d9a
[parent ⬆️](#0b72deb1-12bb-45f6-9dcd-3c7b674e96b8)
