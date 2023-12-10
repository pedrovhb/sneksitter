---
file: /home/pedro/Documents/chatgpt_export/Markdown/Logic Programming Basics.md
heading_stack: <root> -> aae83d65-0c6b-4610-b472-2aec0cdb80b3 -> System -> cd5f65ce-2de1-48c1-aa94-c4163a6f79bd -> System -> aaa22cbb-606f-41d0-b4ae-e591f21bb854 -> User -> e29cce05-dbd4-4728-8c1b-c03f43a7b92e -> Assistant -> Core Components -> How It Works -> Execution Flow: -> aaa2ae6d-a9b8-41f7-87e8-a93920624bd0 -> User -> a699099e-00cf-49be-8eb0-38733c577fa0 -> Assistant -> ac90bca6-5a7a-4d60-9a92-0a011029e761 -> Tool -> 380dfda5-d15a-451f-8e90-19b93624240d -> Assistant -> aaa2c7ad-b00f-44e2-9de9-6d855dc585f8 -> User -> 7ef98a9f-1f7c-4b2d-92df-6e588b7a0d9f -> Assistant -> 437c6506-4d99-402e-8217-957b6ba049be -> Assistant -> 5396381e-bdc1-40fd-96d1-064bd4af05fc -> Tool -> e4917662-5c51-4664-a4a7-54ac891ba2d3 -> Assistant -> aaa2d531-9e41-4df6-8dfb-12e26fdc8d3b -> User -> 20adabdc-0aee-4aa7-a720-66e6ba58c74f -> Assistant
---
# Assistant

```python
from typing import NamedTuple, Union, Dict, List, Type
from collections import namedtuple
from functools import reduce

# Define immutable data structures using NamedTuple
Fact = NamedTuple("Fact", [("predicate", str), ("args", tuple)])
Rule = NamedTuple("Rule", [("predicate", str), ("args", tuple), ("conditions", tuple)])
Condition = NamedTuple("Condition", [("predicate", str), ("args", tuple)])

# Define immutable update function for dictionary
def immutable_dict_update(d: Dict[str, Any], update_dict: Dict[str, Any]) -> Dict[str, Any]:
    new_dict = d.copy()
    new_dict.update(update_dict)
    return new_dict

# CoreLogic class
class CoreLogic:
    def __init__(self):
        self.facts = set()
        self.rules = set()

    def add_fact(self, fact: Fact) -> None:
        self.facts.add(fact)

    def add_rule(self, rule: Rule) -> None:
        self.rules.add(rule)

    def query(self, goal: Condition, subst: Dict[str, Any]) -> List[Dict[str, Any]]:
        results = []
        for fact in self.facts:
            if fact.predicate == goal.predicate:
                new_subst = unify(fact.args, goal.args, subst.copy())
                if new_subst is not None:
                    results.append(new_subst)

        for rule in self.rules:
            if rule.predicate == goal.predicate:
                new_subst = unify(rule.args, goal.args, subst.copy())
                if new_subst is not None:
                    for subgoals in self.query_all(rule.conditions, new_subst):
                        results.append(subgoals)
        return results

    def query_all(self, conditions: tuple, subst: Dict[str, Any]) -> List[Dict[str, Any]]:
        if not conditions:
            return [subst]
        else:
            first, *rest = conditions
            return reduce(lambda acc, new_subst: acc + self.query_all(rest, new_subst),
                          self.query(first, subst), [])

# Query Interface class with operator overrides
class QueryInterface:
    def __init__(self, core_logic: CoreLogic):
        self.core_logic = core_logic
        self.conditions = set()

    def __or__(self, other: 'QueryInterface') -> 'QueryInterface':
        new_instance = QueryInterface(self.core_logic)
        new_instance.conditions = self.conditions | other.conditions
        return new_instance

    def __and__(self, other: 'QueryInterface') -> 'QueryInterface':
        new_instance = QueryInterface(self.core_logic)
        new_instance.conditions = self.conditions & other.conditions
        return new_instance

    def filter(self, condition: Condition) -> 'QueryInterface':
        new_instance = QueryInterface(self.core_logic)
        new_instance.conditions = self.conditions | {condition}
        return new_instance

    def execute(self) -> List[Dict[str, Any]]:
        subst = {}
        return self.core_logic.query_all(tuple(self.conditions), subst)

# Unification remains the same
def unify(term1: Any, term2: Any, subst: Dict[str, Any]) -> Union[Dict[str, Any], None]:
    if subst is None:
        return None
    elif term1 == term2:
        return subst
    elif isinstance(term1, str) and term1.isupper():
        return unify_var(term1, term2, subst)
    elif isinstance(term2, str) and term2.isupper():
        return unify_var(term2, term1, subst)
    elif isinstance(term1, tuple) and isinstance(term2, tuple):
        return unify(term1[1:], term2[1:], unify(term1[0], term2[0], subst))
    return None

def unify_var(var: str, x: Any, subst: Dict[str, Any]) -> Dict[str, Any]:
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    else:
        return immutable_dict_update(subst, {var: x})

# Initialize Core Logic
core_logic = CoreLogic()
core_logic.add_fact(Fact("father", ("John", "Jim")))
core_logic.add_fact(Fact("father", ("Jim", "Jack")))
core_logic.add_fact(Fact("mother", ("Marry", "Jim")))
core_logic.add_rule(Rule("parent", ("X", "Y"), (Condition("father", ("X", "Y")), Condition("mother", ("X", "Y")))))
core_logic.add_rule(Rule("ancestor", ("X", "Y"), (Condition("parent", ("X", "Y")),)))
core_logic.add_rule(Rule("ancestor", ("X", "Y"), (Condition("parent", ("X", "Z")), Condition("ancestor", ("Z", "Y")))))

# Initialize Query Interface
query_interface_1 = QueryInterface(core_logic).filter(Condition("father", ("John", "Y")))
query_interface_2 = QueryInterface(core_logic).filter(Condition("ancestor", ("X", "Jim")))

# Perform a chained query
results = (query_interface_1 | query_interface_2).execute()
results
```

[child ⬇️](#20cb1851-f662-44da-a982-b5b70224b48e)

---

(main branch ⎇)
###### 20cb1851-f662-44da-a982-b5b70224b48e
[parent ⬆️](#20adabdc-0aee-4aa7-a720-66e6ba58c74f)
