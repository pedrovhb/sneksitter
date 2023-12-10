---
file: /home/pedro/Documents/chatgpt_export/Markdown/Logic Programming Basics.md
heading_stack: <root> -> aae83d65-0c6b-4610-b472-2aec0cdb80b3 -> System -> cd5f65ce-2de1-48c1-aa94-c4163a6f79bd -> System -> aaa22cbb-606f-41d0-b4ae-e591f21bb854 -> User -> e29cce05-dbd4-4728-8c1b-c03f43a7b92e -> Assistant -> Core Components -> How It Works -> Execution Flow: -> aaa2ae6d-a9b8-41f7-87e8-a93920624bd0 -> User -> a699099e-00cf-49be-8eb0-38733c577fa0 -> Assistant -> ac90bca6-5a7a-4d60-9a92-0a011029e761 -> Tool -> 380dfda5-d15a-451f-8e90-19b93624240d -> Assistant -> aaa2c7ad-b00f-44e2-9de9-6d855dc585f8 -> User -> 7ef98a9f-1f7c-4b2d-92df-6e588b7a0d9f -> Assistant -> 437c6506-4d99-402e-8217-957b6ba049be -> Assistant
---
# Assistant

```python
from typing import List, Dict, Any, Union

# Base class to handle core logic programming
class CoreLogic:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, predicate: str, *args: Any) -> None:
        self.facts.append({"predicate": predicate, "args": list(args)})

    def add_rule(self, predicate: str, args: List[Any], conditions: List[Dict[str, Any]]) -> None:
        self.rules.append({"predicate": predicate, "args": args, "conditions": conditions})

    def query(self, goal: Dict[str, Any], subst: Dict[str, Any]) -> List[Dict[str, Any]]:
        results = []
        for fact in self.facts:
            if fact['predicate'] == goal['predicate']:
                new_subst = unify(fact['args'], goal['args'], subst.copy())
                if new_subst is not None:
                    results.append(new_subst)

        for rule in self.rules:
            if rule['predicate'] == goal['predicate']:
                new_subst = unify(rule['args'], goal['args'], subst.copy())
                if new_subst is not None:
                    for subgoals in self.query_all(rule['conditions'], new_subst):
                        results.append(subgoals)
        return results

    def query_all(self, conditions: List[Dict[str, Any]], subst: Dict[str, Any]) -> List[Dict[str, Any]]:
        results = []
        if not conditions:
            return [subst]
        else:
            first, *rest = conditions
            for new_subst in self.query(first, subst):
                results.extend(self.query_all(rest, new_subst))
        return results


# High-level Query Interface
class QueryInterface:
    def __init__(self, core_logic: CoreLogic):
        self.core_logic = core_logic
        self.conditions = []

    def filter(self, **kwargs: Any) -> 'QueryInterface':
        new_instance = QueryInterface(self.core_logic)
        new_instance.conditions = self.conditions.copy()
        for key, value in kwargs.items():
            condition = {"predicate": key.split("__")[0], "args": [value]}
            new_instance.conditions.append(condition)
        return new_instance

    def execute(self) -> List[Dict[str, Any]]:
        subst = {}
        return self.core_logic.query_all(self.conditions, subst)

# Unification functions remain the same as before
def unify(term1: Any, term2: Any, subst: Dict[str, Any]) -> Union[Dict[str, Any], None]:
    if subst is None:
        return None
    elif term1 == term2:
        return subst
    elif isinstance(term1, str) and term1.isupper():
        return unify_var(term1, term2, subst)
    elif isinstance(term2, str) and term2.isupper():
        return unify_var(term2, term1, subst)
    elif isinstance(term1, list) and isinstance(term2, list):
        return unify(term1[1:], term2[1:], unify(term1[0], term2[0], subst))
    return None

def unify_var(var: str, x: Any, subst: Dict[str, Any]) -> Dict[str, Any]:
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    else:
        subst[var] = x
        return subst

# Initialize Core Logic
core_logic = CoreLogic()
core_logic.add_fact("father", "John", "Jim")
core_logic.add_fact("father", "Jim", "Jack")
core_logic.add_fact("mother", "Marry", "Jim")
core_logic.add_rule("parent", ["X", "Y"], [{"predicate": "father", "args": ["X", "Y"]}, {"predicate": "mother", "args": ["X", "Y"]}])
core_logic.add_rule("ancestor", ["X", "Y"], [{"predicate": "parent", "args": ["X", "Y"]}])
core_logic.add_rule("ancestor", ["X", "Y"], [{"predicate": "parent", "args": ["X", "Z"]}, {"predicate": "ancestor", "args": ["Z", "Y"]}])

# Initialize Query Interface
query_interface = QueryInterface(core_logic)

# Perform a chained query
results = query_interface.filter(father="John").filter(ancestor="Jim").execute()
results
```

[child ⬇️](#5396381e-bdc1-40fd-96d1-064bd4af05fc)

---

(main branch ⎇)
###### 5396381e-bdc1-40fd-96d1-064bd4af05fc
[parent ⬆️](#437c6506-4d99-402e-8217-957b6ba049be)
