### Surrogates for Predicates (`Q`, `F`, and friends)

The use of `Q` objects in Django's ORM to encapsulate queries in a reusable object is fantastic. We could have `Q` objects for queries and perhaps `A` objects for attributes. These objects could be composed using bitwise operators (`&`, `|`, `~`), much like in Django.

