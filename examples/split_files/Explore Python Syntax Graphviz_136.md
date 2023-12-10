# Tool

```python
Processing state 1 at depth 0
Lookahead symbols for state 1: [0, 2, 8, 10, 14, 17, 26, 29, 39, 41, 44, 47, 53, 75, 106, 115, 116, 118, 121, 125, 126, 142, 144, 145, 151, 153, 174, 176, 203, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 258, 261, 278]
Next state for symbol 0 (end) from state 1 is 0
Processing state 0 at depth 1
Lookahead symbols for state 0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 155, 157, 158, 160, 162, 164, 166, 167, 168, 169, 170, 171, 172, 174, 176, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202]
Next state for symbol 0 (end) from state 0 is 0
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
Cell In[19], line 69
     66 # Generate regular expressions for a subset of states for demonstration
     67 # Here we start from state 1, which is commonly the initial state, and limit max_depth to 2 for debugging
     68 initial_state = 1
---> 69 generated_regex_debug = generate_regex_for_state_debug(initial_state, max_depth=2)
     71 # Show the generated regular expression for the initial state
     72 generated_regex_debug

Cell In[19], line 49, in generate_regex_for_state_debug(state, visited_states, depth, max_depth)
     46 print(f"Next state for symbol {symbol} ({node_kind}) from state {state} is {next_state}")
     48 # Recursive call for next_state
---> 49 next_state_regex = generate_regex_for_state_debug(next_state, visited_states, depth + 1, max_depth)
     51 # Form the regex part for this symbol
     52 symbol_regex = f"(?:{field_name} {node_kind} {next_state_regex})" if field_name else f"(?:{node_kind} {next_state_regex})"

Cell In[19], line 52, in generate_regex_for_state_debug(state, visited_states, depth, max_depth)
     49     next_state_regex = generate_regex_for_state_debug(next_state, visited_states, depth + 1, max_depth)
     51     # Form the regex part for this symbol
---> 52     symbol_regex = f"(?:{field_name} {node_kind} {next_state_regex})" if field_name else f"(?:{node_kind} {next_state_regex})"
     53     regex_parts.append(symbol_regex)
     55 # Compile into a single regex for this state

MemoryError: 

```

[child ⬇️](#e63c232a-af4d-49c3-9d10-4621f6e9f04b)

---

(main branch ⎇)
###### e63c232a-af4d-49c3-9d10-4621f6e9f04b
[parent ⬆️](#559fae71-0141-4853-abad-cec991e09fa6)
