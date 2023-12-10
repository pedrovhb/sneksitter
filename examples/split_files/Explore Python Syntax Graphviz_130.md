# Tool

```python
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
Cell In[18], line 59
     56 # Generate regular expressions for a subset of states for demonstration
     57 # Here we start from state 1, which is commonly the initial state
     58 initial_state = 1
---> 59 generated_regex = generate_regex_for_state(initial_state)
     61 # Show the generated regular expression for the initial state
     62 generated_regex

Cell In[18], line 39, in generate_regex_for_state(state, visited_states, depth, max_depth)
     36 node_kind = sqlite_lang.node_kind_for_id(symbol)
     38 # Recursive call for next_state
---> 39 next_state_regex = generate_regex_for_state(next_state, visited_states, depth + 1, max_depth)
     41 # Form the regex part for this symbol
     42 symbol_regex = f"(?:{field_name} {node_kind} {next_state_regex})" if field_name else f"(?:{node_kind} {next_state_regex})"

Cell In[18], line 42, in generate_regex_for_state(state, visited_states, depth, max_depth)
     39     next_state_regex = generate_regex_for_state(next_state, visited_states, depth + 1, max_depth)
     41     # Form the regex part for this symbol
---> 42     symbol_regex = f"(?:{field_name} {node_kind} {next_state_regex})" if field_name else f"(?:{node_kind} {next_state_regex})"
     43     regex_parts.append(symbol_regex)
     45 # Compile into a single regex for this state

MemoryError: 

```

[child ⬇️](#38d93ec2-136c-4778-8f38-fa2d23724b22)

---

(main branch ⎇)
###### 38d93ec2-136c-4778-8f38-fa2d23724b22
[parent ⬆️](#fd50d689-d16a-4af9-84c7-90522756385b)
