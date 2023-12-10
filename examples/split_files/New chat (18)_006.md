# User

I'm trying to parse function parameters from the following tree-sitter format. Please suggest a sane way to do control flow for getting varargs, positional, kwarg, type annotation, etc based on this wild, wild structure:

parser = tree_sitter_languages.get_parser("python")
    tree = parser.parse(
        d(
            """
            def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
                '''This is a docstring.
            
                Args:
                    x: This is x
                    z: This is z
                    w: This is w
            
                Returns:
                    The sum of x and y
            
                Raises:
                    ValueError: If x is negative
            
                Examples:
                    >>> foo(1, 2)
                    3
                '''
                return x + y
            """
        )
        .encode()
        .strip()
    )
    """
    module                                   | def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w:...
     function_definition                     | def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w:...
      identifier                             | foo
      parameters                             | (*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w:...
       typed_parameter                       | *vararg: str
        list_splat_pattern                   | *vararg
         identifier                          | vararg
        type                                 | str
         identifier                          | str
       identifier                            | x
       default_parameter                     | y=1
        identifier                           | y
        integer                              | 1
       positional_separator                  | /
       default_parameter                     | f="a string default"
        identifier                           | f
        string                               | "a string default"
       keyword_separator                     | *
       typed_default_parameter               | z: int=5
        identifier                           | z
        type                                 | int
         identifier                          | int
        integer                              | 5
       typed_default_parameter               | w: Callable[P, T]=print
        identifier                           | w
        type                                 | Callable[P, T]
         subscript                           | Callable[P, T]
          identifier                         | Callable
          identifier                         | P
          identifier                         | T
        identifier                           | print
       dictionary_splat_pattern              | **kwargs
        identifier                           | kwargs
      type                                   | int
       identifier                            | int
      block                                  | '''This is a docstring. Args: x: This is x z: This is z w: This is w...
       expression_statement                  | '''This is a docstring. Args: x: This is x z: This is z w: This is w...
        string                               | '''This is a docstring. Args: x: This is x z: This is z w: This is w...
       return_statement                      | return x + y
        binary_operator                      | x + y
         identifier                          | x
         identifier                          | y
     """

[child ⬇️](#95861e20-24b9-49e9-be62-3c256f5e4720)

---

(main branch ⎇)
###### 95861e20-24b9-49e9-be62-3c256f5e4720
[parent ⬆️](#aaa242ce-7fcb-4865-bc06-4b38eb8a2fdd)
