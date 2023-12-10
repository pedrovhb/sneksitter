---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Pydantic Model.md
heading_stack: <root> -> 0762e539-3141-4568-97e1-8e2f28a26a31 -> System -> 7310dbb5-540b-40ba-ba28-f730ab506660 -> System -> aaa26adf-0eb0-4d7d-93a7-d9d284b5c9f3 -> User -> c6015848-a2ab-4b8c-8922-7bf89d9fdf34 -> Assistant -> Models -> 1. `ParameterModel` -> 2. `DecoratorModel` -> 3. `FunctionModel` -> Methods -> Class Method in `FunctionModel` -> Instance Method in `FunctionModel` -> aaa2eb12-3770-4c5c-a7d3-11878ab54370 -> User -> 0dd09b46-e035-48e5-b69f-280b00736c87 -> Assistant -> 02c086bb-208a-49fb-93b3-54248d0f2aa5 -> Tool -> 03e8d8b9-74a8-4a74-a1bf-aec328fe0a7c -> Assistant -> aaa26425-589c-40d9-908e-333cab56319e -> User -> 9e70ce7f-89db-47ac-85b9-7d73fd7ab640 -> Assistant -> 9cb5bb3a-3cd2-4945-b8b9-01e102f6b2ab -> Tool -> 4b953605-0288-49bf-8ce8-041f4a25504d -> Assistant -> 1801b898-5c26-4e7a-af26-d7268e8c01b5 -> Assistant -> 855176a8-5adb-411e-a098-cae3b880d095 -> Assistant -> 22bbc826-60cc-4070-af85-31471f4bf1de -> Tool -> e3ed333b-ba18-4842-b480-3f634245d238 -> Assistant -> aaa2ded3-1a21-484d-9326-598b00f61110 -> User -> 5b0b16af-8e39-4842-b887-04965d88167a -> Assistant -> 82554842-e6c7-4a6c-953b-8778ad13f907 -> Tool -> 9e6d99ad-6826-402d-b2df-17c8435586f0 -> Assistant -> 8ea69820-2e45-4f03-a531-0caeea4ca772 -> Assistant -> c8a255a2-f1db-4668-b976-619d18cc4c9a -> Tool -> e5a85609-e6ea-4263-800f-599e24019950 -> Assistant -> 7077a825-b4ed-4044-aeb4-4c2eef133509 -> Assistant -> 27051524-a0d0-48c2-b51f-127049bbddc3 -> Tool -> 8080c22e-9466-44bf-8bd6-5688b064d583 -> Assistant -> aaa239f7-a854-420f-9afa-841001491865 -> User -> cabb6712-685d-49e8-8af7-837ea6277f43 -> System -> a3034118-ba1f-4ee0-b487-daa540cdf236 -> Assistant -> 2f7d2cd2-9aa9-4ca1-a42f-53296be00132 -> Tool -> 8ff07254-af54-49bf-8e6f-8e2801ba7184 -> Assistant -> 2e959f2c-486e-444b-a6cf-8bb8eda6a77d -> Tool -> 77161e88-66bd-481a-b462-51820df15a4b -> Assistant -> f9e86d22-1f27-4bd6-8664-7cb72c386b6b -> Assistant -> aaa2b611-e6c8-4bed-b99d-34a0efb777c4 -> User -> 20eb6f92-e97d-4bff-9548-cc674656cf49 -> Assistant -> 54e67c7c-bc03-4f36-9a83-4e77d9e68e9e -> Tool -> ff52ba1a-d5dd-4037-9d27-6e145a9268d0 -> Assistant -> aaa29597-3ee2-4b63-9d66-7e46d9b21223 -> User -> 7c7f1290-7903-4e49-bf88-07a3a14b7058 -> System -> 1b7bfd49-3f89-426d-ae55-8eeef11d4dd9 -> Assistant -> d3eb6a26-715c-4221-a8e5-ceb1817d908b -> Tool -> ed67e3c8-b4b6-4a7d-99e4-fe956d0fdf3c -> Assistant -> 2173b865-5c1c-4c3f-9005-a5727e436499 -> Assistant -> 65dc3678-4ca8-401b-98c6-df2d399679f7 -> Tool -> 3ccd7b6b-5544-4705-9e60-fc850b1a15cb -> Assistant -> aaa269bb-1cbd-4747-b22d-3ad163b40814 -> User -> 04f43ec6-ff4c-4b29-b23e-61767df38267 -> Assistant -> cfd79b3a-4a67-4a85-8803-76cca4b9d9d5 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[14], line 62
     59 import math
     61 # Represent the module as a ModuleModel
---> 62 module_model = ModuleModel.from_module(math)
     64 class_model, module_model

Cell In[14], line 39, in ModuleModel.from_module(cls, module_obj)
     37         classes.append(class_model)
     38     elif callable(attr_value):
---> 39         function_model = FunctionModel.from_function(attr_value)
     40         functions.append(function_model)
     42 return cls(name=name, classes=classes, functions=functions)

Cell In[6], line 12, in FunctionModel.from_function(cls, func)
     10 @classmethod
     11 def from_function(cls, func: Callable) -> 'FunctionModel':
---> 12     func_details = inspect.signature(func)
     13     name = func.__name__
     14     docstring = func.__doc__

File /usr/lib/python3.8/inspect.py:3105, in signature(obj, follow_wrapped)
   3103 def signature(obj, *, follow_wrapped=True):
   3104     """Get a signature object for the passed callable."""
-> 3105     return Signature.from_callable(obj, follow_wrapped=follow_wrapped)

File /usr/lib/python3.8/inspect.py:2854, in Signature.from_callable(cls, obj, follow_wrapped)
   2851 @classmethod
   2852 def from_callable(cls, obj, *, follow_wrapped=True):
   2853     """Constructs Signature for the given callable object."""
-> 2854     return _signature_from_callable(obj, sigcls=cls,
   2855                                     follow_wrapper_chains=follow_wrapped)

File /usr/lib/python3.8/inspect.py:2308, in _signature_from_callable(obj, follow_wrapper_chains, skip_bound_arg, sigcls)
   2304     return _signature_from_function(sigcls, obj,
   2305                                     skip_bound_arg=skip_bound_arg)
   2307 if _signature_is_builtin(obj):
-> 2308     return _signature_from_builtin(sigcls, obj,
   2309                                    skip_bound_arg=skip_bound_arg)
   2311 if isinstance(obj, functools.partial):
   2312     wrapped_sig = _signature_from_callable(
   2313         obj.func,
   2314         follow_wrapper_chains=follow_wrapper_chains,
   2315         skip_bound_arg=skip_bound_arg,
   2316         sigcls=sigcls)

File /usr/lib/python3.8/inspect.py:2119, in _signature_from_builtin(cls, func, skip_bound_arg)
   2117 s = getattr(func, "__text_signature__", None)
   2118 if not s:
-> 2119     raise ValueError("no signature found for builtin {!r}".format(func))
   2121 return _signature_fromstr(cls, func, s, skip_bound_arg)

ValueError: no signature found for builtin <built-in function hypot>

```

[child ⬇️](#bed60de6-ffa2-49ba-aea6-ca1d4c3e835d)

---

(other branch ⎇)
###### bed60de6-ffa2-49ba-aea6-ca1d4c3e835d
[parent ⬆️](#cfd79b3a-4a67-4a85-8803-76cca4b9d9d5)
