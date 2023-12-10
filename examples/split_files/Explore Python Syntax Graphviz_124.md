# Tool

```python
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
Cell In[17], line 57
     54 # Generate regular expressions for a subset of states for demonstration
     55 # Here we start from state 1, which is commonly the initial state
     56 initial_state = 1
---> 57 generated_regex = generate_regex_for_state(initial_state)
     59 # Show the generated regular expression for the initial state
     60 generated_regex

Cell In[17], line 40, in generate_regex_for_state(state, depth, max_depth)
     37 node_kind = sqlite_lang.node_kind_for_id(symbol)
     39 # Recursive call for next_state
---> 40 next_state_regex = generate_regex_for_state(next_state, depth + 1, max_depth)
     42 # Form the regex part for this symbol
     43 symbol_regex = f"(?:{field_name} {node_kind} {next_state_regex})" if field_name else f"(?:{node_kind} {next_state_regex})"

Cell In[17], line 40, in generate_regex_for_state(state, depth, max_depth)
     37 node_kind = sqlite_lang.node_kind_for_id(symbol)
     39 # Recursive call for next_state
---> 40 next_state_regex = generate_regex_for_state(next_state, depth + 1, max_depth)
     42 # Form the regex part for this symbol
     43 symbol_regex = f"(?:{field_name} {node_kind} {next_state_regex})" if field_name else f"(?:{node_kind} {next_state_regex})"

Cell In[17], line 43, in generate_regex_for_state(state, depth, max_depth)
     40     next_state_regex = generate_regex_for_state(next_state, depth + 1, max_depth)
     42     # Form the regex part for this symbol
---> 43     symbol_regex = f"(?:{field_name} {node_kind} {next_state_regex})" if field_name else f"(?:{node_kind} {next_state_regex})"
     44     regex_parts.append(symbol_regex)
     46 # Compile into a single regex for this state

MemoryError: 

```

[child ⬇️](#a4b88ac1-ef38-48d2-9186-a4fd9dff9dd6)

---

(main branch ⎇)
###### a4b88ac1-ef38-48d2-9186-a4fd9dff9dd6
[parent ⬆️](#8246446b-8f88-437f-b1cc-1f0648ee40a3)
