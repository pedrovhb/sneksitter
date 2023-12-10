---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (2).md
heading_stack: <root> -> e7c9baec-ffab-4c2e-bbb4-561fd977d430 -> System -> 536e0e74-8c30-49ea-ae85-f83cc1361c13 -> System -> aaa29187-c9e6-4055-a115-71076813ffbc -> User -> cc136d1c-37a8-4c4a-b365-9b8369a2b895 -> Assistant -> Approaches: -> Generalized to ASTs: -> Code Example: -> a238746d-f3e1-4b77-a9b7-ba0f5e8f7049 -> Assistant -> 29d82439-fb56-42eb-afe8-8ca15db19eb8 -> Tool -> f1219ce2-4490-4271-881d-328b7eed1acf -> Assistant -> aaa2c008-0c05-4714-90ce-395abd9559a8 -> User -> b4bb145a-3220-4564-b3ee-c5ec6c3ac485 -> Assistant -> 8d058de8-bf7e-4d33-8add-ff38a294ccf3 -> Tool -> 82fca1ae-6c6b-4948-a056-d75568771d51 -> Assistant -> aaa22bef-f9a9-4ccd-a7ee-a32f715e1298 -> User -> b4eff856-22ed-48d6-9914-b5d88ad5900c -> Assistant -> Design: -> 104bd562-86a6-4f4a-bc9f-a0547164b28e -> Assistant -> 16e122ab-f2db-436e-828f-bfa39aa4f7ed -> Tool -> b02c5db1-9ad5-4939-8bd8-aa59a9c6b557 -> Assistant -> 9b2d3607-c709-4fc4-8538-ebf92d3bde56 -> Assistant -> c5b8c212-728c-4fe8-8f3a-a7b4f0192f92 -> Tool -> fe53cc43-94fc-46e7-baed-171a6da9377d -> Assistant -> 731821cf-5d1e-4c27-b899-a28ff2d41032 -> Assistant -> c8cf863a-b329-4cba-8005-96a60c18cb54 -> Tool -> 8c1e076f-bf22-4db6-b3cc-b1d454083d70 -> Assistant -> 3e5448cd-a45f-44cb-9797-7ae40e130e15 -> Assistant -> 297959ae-169f-4b53-9891-613369d0854b -> Tool -> aff97488-cebd-4a1e-ad04-0c9d3a03b30c -> Assistant -> eb960eec-89da-43cd-b077-5c250e9e6679 -> Assistant -> aaa2f12c-7872-4c97-95e7-3a566eb298c1 -> User -> 113323f2-22d5-4ed0-a704-0b4e4f274da8 -> Assistant -> 5a3a56cf-7fd0-4562-a2a4-374e323618b8 -> Assistant -> b50ddbca-f9e1-457c-a3a1-28a0bb6c8937 -> Tool -> 423fbc8d-44b6-4889-ac81-c99528175c6e -> Assistant -> 46eeff61-a13f-4b14-bae4-5a12532fd5cd -> Assistant -> b877108a-0486-4fda-8b27-917137da182c -> Tool -> 6a1dbfa1-50dc-4ec2-a823-ba7465ca03cf -> Assistant -> 5357c495-f4d7-491c-8ff5-933e3cae577a -> Assistant
---
# Assistant

```python
# Update the resolve method to pass only the data dictionary to the predicate functions

class QueryWrapper(Generic[NodeT, EdgeT]):
    # ... (other methods unchanged)
    
    def resolve(self) -> Iterable[NodeT]:
        """Evaluates the query stack and returns nodes that satisfy it."""
        return [(node, data) for node, data in self.graph.nodes(data=True) if self.evaluate_stack(data)]

# Reinitialize QueryWrapper and rebuild query
my_queriable = QueryWrapper[NodeT, EdgeT](G)
my_queriable.add_predicate((N == "module").predicate)
my_queriable.add_predicate(((N == "function_definition") | (N == "class_definition") | (N == "decorated_definition")).predicate, logical_op="or")

# Re-run resolve
print(my_queriable.resolve())
```

[child ⬇️](#d6397c3c-320d-479c-8b59-d13f856dd636)

---

(main branch ⎇)
###### d6397c3c-320d-479c-8b59-d13f856dd636
[parent ⬆️](#5357c495-f4d7-491c-8ff5-933e3cae577a)
