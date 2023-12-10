#### Plan

1. **Initialize State**: Start with `state = START`.

2. **Iterate through Parameters**: Loop through the child nodes (parameters) provided by Tree-Sitter.

3. **Depth-First Traversal**: For each child node that has its own children (e.g., `typed_default_parameter`), use depth-first traversal to extract its details like type annotation, default value, and so on.

    3.1 For depth-first traversal, encapsulate this logic in a separate helper function.

4. **State Transition Logic**: Apply the FSM based on the current node and update the state accordingly.

    4.1 If an invalid transition occurs, raise an appropriate exception.

5. **Parameter Object Creation**: Based on the state and traversed node details, create `Parameter` objects with all the relevant attributes.

6. **Collect Parameter Objects**: Append each processed `Parameter` object to a list.

7. **Return Result**: After looping through all child nodes, return the list of `Parameter` objects.

