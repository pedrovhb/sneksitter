### Example Code:

Let's start by setting up a minimal example. For simplicity, let's consider the AST of a small JavaScript code snippet, and we'll try to query functions defined in the code.

```javascript
// Example JavaScript code
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}
```

The corresponding Tree-sitter AST might look something like this (simplified):

```json
{
  "type": "program",
  "children": [
    {
      "type": "function_declaration",
      "name": "add",
      "parameters": ["a", "b"]
    },
    {
      "type": "function_declaration",
      "name": "subtract",
      "parameters": ["a", "b"]
    }
  ]
}
```

We can represent this AST as Problog facts:

```prolog
function(add, [a, b]).
function(subtract, [a, b]).
```

Now, let's write code to convert a Tree-sitter AST to Problog facts and then query it using Problog.

[child ⬇️](#6cdbec38-13cd-4dd5-8040-93187532675b)

---

(main branch ⎇)
###### 6cdbec38-13cd-4dd5-8040-93187532675b
[parent ⬆️](#be9a8c0c-0d5d-436e-b112-e245cc79de57)
