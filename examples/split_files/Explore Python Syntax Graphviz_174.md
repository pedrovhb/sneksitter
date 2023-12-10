# Assistant

```python
class TokenBasedStateMachine:
    def __init__(self, lang, initial_state=1):
        self.lang = lang
        self.initial_state = initial_state

    def is_valid_string(self, input_string):
        """
        Check if a given string is valid according to the SQLite grammar.

        Parameters:
        - input_string: The string to validate.

        Returns:
        - bool: True if the string is valid, otherwise False.
        """
        current_state = self.initial_state
        token_buffer = ""  # Buffer to accumulate characters into tokens

        for char in input_string:
            token_buffer += char  # Add the character to the token buffer

            # Get valid next symbols for the current state
            valid_next_symbols = list(self.lang.lookahead_iterator(current_state))
            valid_next_kinds = [self.lang.node_kind_for_id(symbol) for symbol in valid_next_symbols]

            # Check if the current token buffer corresponds to any valid next symbol
            if token_buffer in valid_next_kinds:
                # Transition to the next state based on the current token
                symbol = valid_next_symbols[valid_next_kinds.index(token_buffer)]
                current_state = self.lang.next_state(current_state, symbol)
                
                # Clear the token buffer
                token_buffer = ""
            else:
                # Check if the token buffer could potentially lead to a valid token
                if not any(kind.startswith(token_buffer) for kind in valid_next_kinds):
                    return False

        # Final validation: Check if the token buffer forms a valid token in the final state
        if token_buffer:
            valid_next_symbols = list(self.lang.lookahead_iterator(current_state))
            valid_next_kinds = [self.lang.node_kind_for_id(symbol) for symbol in valid_next_symbols]
            if token_buffer not in valid_next_kinds:
                return False

        return True

# Initialize the TokenBasedStateMachine with SQLite language and initial state 1
token_based_state_machine = TokenBasedStateMachine(sqlite_lang, initial_state=1)

# Test with some example strings
test_strings_token_based = ["SELECT", "INSERT", "INVALID_STRING"]
test_results_token_based = {s: token_based_state_machine.is_valid_string(s) for s in test_strings_token_based}

test_results_token_based
```

[child ⬇️](#46ebd8f7-d8aa-46ef-bce6-e07289275446)

---

(main branch ⎇)
###### 46ebd8f7-d8aa-46ef-bce6-e07289275446
[parent ⬆️](#2231bdb5-fad2-42c1-8f2d-94c3a9e0dd7e)
