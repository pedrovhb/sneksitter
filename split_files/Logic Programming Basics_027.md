---
file: /home/pedro/Documents/chatgpt_export/Markdown/Logic Programming Basics.md
heading_stack: <root> -> aae83d65-0c6b-4610-b472-2aec0cdb80b3 -> System -> cd5f65ce-2de1-48c1-aa94-c4163a6f79bd -> System -> aaa22cbb-606f-41d0-b4ae-e591f21bb854 -> User -> e29cce05-dbd4-4728-8c1b-c03f43a7b92e -> Assistant -> Core Components -> How It Works -> Execution Flow: -> aaa2ae6d-a9b8-41f7-87e8-a93920624bd0 -> User -> a699099e-00cf-49be-8eb0-38733c577fa0 -> Assistant -> ac90bca6-5a7a-4d60-9a92-0a011029e761 -> Tool -> 380dfda5-d15a-451f-8e90-19b93624240d -> Assistant -> aaa2c7ad-b00f-44e2-9de9-6d855dc585f8 -> User -> 7ef98a9f-1f7c-4b2d-92df-6e588b7a0d9f -> Assistant -> 437c6506-4d99-402e-8217-957b6ba049be -> Assistant -> 5396381e-bdc1-40fd-96d1-064bd4af05fc -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[2], line 96
     93 query_interface = QueryInterface(core_logic)
     95 # Perform a chained query
---> 96 results = query_interface.filter(father="John").filter(ancestor="Jim").execute()
     97 results

Cell In[2], line 58, in QueryInterface.execute(self)
     56 def execute(self) -> List[Dict[str, Any]]:
     57     subst = {}
---> 58     return self.core_logic.query_all(self.conditions, subst)

Cell In[2], line 37, in CoreLogic.query_all(self, conditions, subst)
     35 else:
     36     first, *rest = conditions
---> 37     for new_subst in self.query(first, subst):
     38         results.extend(self.query_all(rest, new_subst))
     39 return results

Cell In[2], line 19, in CoreLogic.query(self, goal, subst)
     17 for fact in self.facts:
     18     if fact['predicate'] == goal['predicate']:
---> 19         new_subst = unify(fact['args'], goal['args'], subst.copy())
     20         if new_subst is not None:
     21             results.append(new_subst)

Cell In[2], line 71, in unify(term1, term2, subst)
     69     return unify_var(term2, term1, subst)
     70 elif isinstance(term1, list) and isinstance(term2, list):
---> 71     return unify(term1[1:], term2[1:], unify(term1[0], term2[0], subst))
     72 return None

Cell In[2], line 71, in unify(term1, term2, subst)
     69     return unify_var(term2, term1, subst)
     70 elif isinstance(term1, list) and isinstance(term2, list):
---> 71     return unify(term1[1:], term2[1:], unify(term1[0], term2[0], subst))
     72 return None

IndexError: list index out of range

```

[child ⬇️](#e4917662-5c51-4664-a4a7-54ac891ba2d3)

---

(main branch ⎇)
###### e4917662-5c51-4664-a4a7-54ac891ba2d3
[parent ⬆️](#5396381e-bdc1-40fd-96d1-064bd4af05fc)
