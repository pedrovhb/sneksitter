### API Design

#### Node Construction and Capture

The `.node()` method will initiate the construction of a new node. The `.capture_as()` method would be used to specify the capture name for the preceding node or field.

```python
def node(self, type: str) -> 'QueryBuilder':
    ...

def capture_as(self, name: str) -> 'QueryBuilder':
    ...
```

#### Field Qualification

To add a field to a node, we'll use the `.field()` method.

```python
def field(self, name: str) -> 'QueryBuilder':
    ...
```

#### Grouping and Nesting

The `.end()` method will signify the end of a nested query, essentially "closing" a node or a field, allowing you to continue with the parent query.

```python
def end(self) -> 'QueryBuilder':
    ...
```

#### Anchors and Wildcards

Anchors and wildcards can be added using `.anchor_start()`, `.anchor_end()`, and `.wildcard()` methods.

```python
def anchor_start(self) -> 'QueryBuilder':
    ...

def anchor_end(self) -> 'QueryBuilder':
    ...

def wildcard(self) -> 'QueryBuilder':
    ...
```

#### Predicates

Predicates like `eq?` can be added using the `.predicate()` method, which takes the predicate name and its arguments.

```python
def predicate(self, name: str, *args) -> 'QueryBuilder':
    ...
```

