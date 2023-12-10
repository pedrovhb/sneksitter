### Proposed API Changes

1. **`__getitem__`**: Overloaded to initiate the construction of a new node or child node. Captures can be passed as arguments.

    ```python
    def __getitem__(self, item: Union[str, Tuple[str, str]]) -> 'QueryBuilder':
        ...
    ```

2. **`__getattr__`**: Overloaded to allow field names as attributes.

    ```python
    def __getattr__(self, name: str) -> 'QueryBuilder':
        ...
    ```

3. **`or_()`**: Remains the same to signify the end of one pattern and start of another.

4. **`predicate()`**: Now accepts a callable, allowing for more Pythonic conditional logic.

    ```python
    def predicate(self, func: Callable) -> 'QueryBuilder':
        ...
    ```

5. **`start_anchor()` and `end_anchor()`**: Remains the same for specifying anchors.

6. **`wildcard()`**: Remains the same for adding a wildcard.

7. **`build()`**: Constructs the final S-expression, with validations.

    ```python
    def build(self) -> str:
        ...
    ```

