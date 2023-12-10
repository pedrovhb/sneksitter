# Assistant

```python
class CharacterBasedStateMachine:
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

        for char in input_string:
            # Get valid next symbols for the current state
            valid_next_symbols = list(self.lang.lookahead_iterator(current_state))
            
            # Check if the current character corresponds to any valid next symbol
            valid_transition = False
            for symbol in valid_next_symbols:
                node_kind = self.lang.node_kind_for_id(symbol)
                if node_kind == char:
                    current_state = self.lang.next_state(current_state, symbol)
                    valid_transition = True
                    break

            if not valid_transition:
                return False

        return True

# Initialize the CharacterBasedStateMachine with SQLite language and initial state 1
state_machine = CharacterBasedStateMachine(sqlite_lang, initial_state=1)

# Test with some example strings
test_strings = ["SELECT", "INSERT", "INVALID_STRING"]
test_results = {s: state_machine.is_valid_string(s) for s in test_strings}

test_results
```

[child ⬇️](#5c7dde85-67b9-431f-94d7-884ab54c2ef9)

---

(main branch ⎇)
###### 5c7dde85-67b9-431f-94d7-884ab54c2ef9
[parent ⬆️](#ffe37cca-6b17-416b-ac86-dd229fa3d28f)
