# User

Summarize in yaml format the reference for queries:

A query consists of one or more patterns, where each pattern is an S-expression that matches a certain set of nodes in a syntax tree. The expression to match a given node consists of a pair of parentheses containing two things: the node’s type, and optionally, a series of other S-expressions that match the node’s children. For example, this pattern would match any binary_expression node whose children are both number_literal nodes:

(binary_expression (number_literal) (number_literal))
Children can also be omitted. For example, this would match any binary_expression where at least one of child is a string_literal node:

(binary_expression (string_literal))
Fields
In general, it’s a good idea to make patterns more specific by specifying field names associated with child nodes. You do this by prefixing a child pattern with a field name followed by a colon. For example, this pattern would match an assignment_expression node where the left child is a member_expression whose object is a call_expression.

(assignment_expression
  left: (member_expression
    object: (call_expression)))
Negated Fields
You can also constrain a pattern so that it only matches nodes that lack a certain field. To do this, add a field name prefixed by a ! within the parent pattern. For example, this pattern would match a class declaration with no type parameters:

(class_declaration
  name: (identifier) @class_name
  !type_parameters)
Anonymous Nodes
The parenthesized syntax for writing nodes only applies to named nodes. To match specific anonymous nodes, you write their name between double quotes. For example, this pattern would match any binary_expression where the operator is != and the right side is null:

(binary_expression
  operator: "!="
  right: (null))
Capturing Nodes
When matching patterns, you may want to process specific nodes within the pattern. Captures allow you to associate names with specific nodes in a pattern, so that you can later refer to those nodes by those names. Capture names are written after the nodes that they refer to, and start with an @ character.

For example, this pattern would match any assignment of a function to an identifier, and it would associate the name the-function-name with the identifier:

(assignment_expression
  left: (identifier) @the-function-name
  right: (function))
And this pattern would match all method definitions, associating the name the-method-name with the method name, the-class-name with the containing class name:

(class_declaration
  name: (identifier) @the-class-name
  body: (class_body
    (method_definition
      name: (property_identifier) @the-method-name)))
Quantification Operators
You can match a repeating sequence of sibling nodes using the postfix + and * repetition operators, which work analogously to the + and * operators in regular expressions. The + operator matches one or more repetitions of a pattern, and the * operator matches zero or more.

For example, this pattern would match a sequence of one or more comments:

(comment)+
This pattern would match a class declaration, capturing all of the decorators if any were present:

(class_declaration
  (decorator)* @the-decorator
  name: (identifier) @the-name)
You can also mark a node as optional using the ? operator. For example, this pattern would match all function calls, capturing a string argument if one was present:

(call_expression
  function: (identifier) @the-function
  arguments: (arguments (string)? @the-string-arg))
Grouping Sibling Nodes
You can also use parentheses for grouping a sequence of sibling nodes. For example, this pattern would match a comment followed by a function declaration:

(
  (comment)
  (function_declaration)
)
Any of the quantification operators mentioned above (+, *, and ?) can also be applied to groups. For example, this pattern would match a comma-separated series of numbers:

(
  (number)
  ("," (number))*
)
Alternations
An alternation is written as a pair of square brackets ([]) containing a list of alternative patterns. This is similar to character classes from regular expressions ([abc] matches either a, b, or c).

For example, this pattern would match a call to either a variable or an object property. In the case of a variable, capture it as @function, and in the case of a property, capture it as @method:

(call_expression
  function: [
    (identifier) @function
    (member_expression
      property: (property_identifier) @method)
  ])
This pattern would match a set of possible keyword tokens, capturing them as @keyword:

[
  "break"
  "delete"
  "else"
  "for"
  "function"
  "if"
  "return"
  "try"
  "while"
] @keyword
Wildcard Node
A wildcard node is represented with an underscore (_), it matches any node. This is similar to . in regular expressions. There are two types, (_) will match any named node, and _ will match any named or anonymous node.

For example, this pattern would match any node inside a call:

(call (_) @call.inner)
Anchors
The anchor operator, ., is used to constrain the ways in which child patterns are matched. It has different behaviors depending on where it’s placed inside a query.

When . is placed before the first child within a parent pattern, the child will only match when it is the first named node in the parent. For example, the below pattern matches a given array node at most once, assigning the @the-element capture to the first identifier node in the parent array:

(array . (identifier) @the-element)
Without this anchor, the pattern would match once for every identifier in the array, with @the-element bound to each matched identifier.

Similarly, an anchor placed after a pattern’s last child will cause that child pattern to only match nodes that are the last named child of their parent. The below pattern matches only nodes that are the last named child within a block.

(block (_) @last-expression .)
Finally, an anchor between two child patterns will cause the patterns to only match nodes that are immediate siblings. The pattern below, given a long dotted name like a.b.c.d, will only match pairs of consecutive identifiers: a, b, b, c, and c, d.

(dotted_name
  (identifier) @prev-id
  .
  (identifier) @next-id)
Without the anchor, non-consecutive pairs like a, c and b, d would also be matched.

The restrictions placed on a pattern by an anchor operator ignore anonymous nodes.

Predicates
You can also specify arbitrary metadata and conditions associated with a pattern by adding predicate S-expressions anywhere within your pattern. Predicate S-expressions start with a predicate name beginning with a # character. After that, they can contain an arbitrary number of @-prefixed capture names or strings.

Tree-Sitter’s CLI supports the following predicates by default:

eq?, not-eq?, any-eq?, any-not-eq?
This family of predicates allows you to match against a single capture or string value.

The first argument must be a capture, but the second can be either a capture to compare the two captures’ text, or a string to compare first capture’s text against.

The base predicate is “#eq?”, but its complement “#not-eq?” can be used to not match a value.

Consider the following example targeting C:

((identifier) @variable.builtin
  (#eq? @variable.builtin "self"))
This pattern would match any identifier that is self or this.

And this pattern would match key-value pairs where the value is an identifier with the same name as the key:

(
  (pair
    key: (property_identifier) @key-name
    value: (identifier) @value-name)
  (#eq? @key-name @value-name)
)
The prefix “any-“ is meant for use with quantified captures. Here’s an example finding a segment of empty comments

((comment)+ @comment.empty
  (#any-eq? @comment.empty "//"))
Note that “#any-eq?” will match a quantified capture if any of the nodes match the predicate, while by default a quantified capture will only match if all the nodes match the predicate.

match?, not-match?, any-match?, any-not-match?
These predicates are similar to the eq? predicates, but they use regular expressions to match against the capture’s text.

The first argument must be a capture, and the second must be a string containing a regular expression.

For example, this pattern would match identifier whose name is written in SCREAMING_SNAKE_CASE:

((identifier) @constant
  (#match? @constant "^[A-Z][A-Z_]+"))
Here’s an example finding potential documentation comments in C

((comment)+ @comment.documentation
  (#match? @comment.documentation "^///\s+.*"))
Here’s another example finding Cgo comments to potentially inject with C

((comment)+ @injection.content
  .
  (import_declaration
    (import_spec path: (interpreted_string_literal) @_import_c))
  (#eq? @_import_c "\"C\"")
  (#match? @injection.content "^//"))
any-of?, not-any-of?
The “any-of?” predicate allows you to match a capture against multiple strings, and will match if the capture’s text is equal to any of the strings.

Consider this example that targets JavaScript:

((identifier) @variable.builtin
  (#any-of? @variable.builtin
        "arguments"
        "module"
        "console"
        "window"
        "document"))
This will match any of the builtin variables in JavaScript.

Note — Predicates are not handled directly by the Tree-sitter C library. They are just exposed in a structured form so that higher-level code can perform the filtering. However, higher-level bindings to Tree-sitter like the Rust Crate or the WebAssembly binding do implement a few common predicates like the #eq?, #match?, and #any-of? predicates explained above.

To recap about the predicates Tree-Sitter’s bindings support:

#eq? checks for a direct match against a capture or string
#match? checks for a match against a regular expression
#any-of? checks for a match against a list of strings
Adding not- to the beginning of any of these predicates will negate the match
By default, a quantified capture will only match if all of the nodes match the predicate
Adding any- before the eq or match predicates will instead match if any of the nodes match the predicate
The Query API
Create a query by specifying a string containing one or more patterns:

TSQuery *ts_query_new(
  const TSLanguage *language,
  const char *source,
  uint32_t source_len,
  uint32_t *error_offset,
  TSQueryError *error_type
);
If there is an error in the query, then the error_offset argument will be set to the byte offset of the error, and the error_type argument will be set to a value that indicates the type of error:

typedef enum {
  TSQueryErrorNone = 0,
  TSQueryErrorSyntax,
  TSQueryErrorNodeType,
  TSQueryErrorField,
  TSQueryErrorCapture,
} TSQueryError;
The TSQuery value is immutable and can be safely shared between threads. To execute the query, create a TSQueryCursor, which carries the state needed for processing the queries. The query cursor should not be shared between threads, but can be reused for many query executions.

TSQueryCursor *ts_query_cursor_new(void);
You can then execute the query on a given syntax node:

void ts_query_cursor_exec(TSQueryCursor *, const TSQuery *, TSNode);
You can then iterate over the matches:

typedef struct {
  TSNode node;
  uint32_t index;
} TSQueryCapture;

typedef struct {
  uint32_t id;
  uint16_t pattern_index;
  uint16_t capture_count;
  const TSQueryCapture *captures;
} TSQueryMatch;

bool ts_query_cursor_next_match(TSQueryCursor *, TSQueryMatch *match);
This function will return false when there are no more matches. Otherwise, it will populate the match with data about which pattern matched and which nodes were captured.

[child ⬇️](#0ca77f9c-ecfc-4df4-be6b-ec2c96eb4460)

---

(main branch ⎇)
###### 0ca77f9c-ecfc-4df4-be6b-ec2c96eb4460
[parent ⬆️](#aaa2fadc-e768-42c3-8f1d-1e2175896635)
