# User

Some cool ideas I think 
  could make sense:

- query composition is great.
 - queries could be built piecewise and composed.
  - Django is a great example, its **kwargs double underscore for nested attribute access is a great idea and could provide a lot of value here.
  - Another great couple of ideas from django are Q, F, and friends.
  - Surrogates for predicates are cool (tm)

Some unorganized, written but not read, possibly broken or nonsense wild ideas in API design:

q1 = Q(lambda node: node.parent.type == "function_def")
