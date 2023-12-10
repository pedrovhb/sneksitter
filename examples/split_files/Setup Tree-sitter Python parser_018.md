# User

I'd like to see examples of pattern matching as such:

query = PY_LANGUAGE.query("""
(function_definition
  name: (identifier) @function.def)

(call
  function: (identifier) @function.call)
""")

captures = query.captures(tree.root_node)
assert len(captures) == 2
assert captures[0][0] == function_name_node
assert captures[0][1] == "function.def"

[child ⬇️](#953ccdca-be2f-4765-bdf5-13151dff1986)

---

(main branch ⎇)
###### 953ccdca-be2f-4765-bdf5-13151dff1986
[parent ⬆️](#aaa293e9-a16a-4dcb-bf1e-e1a857731e97)
