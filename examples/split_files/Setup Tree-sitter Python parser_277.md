# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[15], line 4
      1 import setup_env
      3 # Re-initializing the parser and language objects
----> 4 PY_LANGUAGE = setup_env.tsl.get_language("python")
      5 parser = setup_env.tsl.get_parser("python")
      7 # Parse the sample code to generate a syntax tree

AttributeError: module 'setup_env' has no attribute 'tsl'

```

[child ⬇️](#8aedc1e2-f327-4ae4-9433-2ed881257273)

---

(other branch ⎇)
###### 8aedc1e2-f327-4ae4-9433-2ed881257273
[parent ⬆️](#ec160e42-1f13-45b9-beee-988d7076c36e)
