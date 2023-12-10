# Tool

```python
module                                   | @simple_decorator def simple_func(): pass @decorator_with_args("arg1", 2) def...
 decorated_definition                    | @simple_decorator def simple_func(): pass
  decorator                              | @simple_decorator
   @ | 
   identifier                            | simple_decorator
  function_definition                    | def simple_func(): pass
   def | 
   identifier                            | simple_func
   parameters                            | ()
    ( | 
    ) | 
   : | 
   block                                 | pass
    pass_statement                       | pass
     pass | 
 decorated_definition                    | @decorator_with_args("arg1", 2) def func_with_args(): pass
  decorator                              | @decorator_with_args("arg1", 2)
   @ | 
   call                                  | decorator_with_args("arg1", 2)
    identifier                           | decorator_with_args
    argument_list                        | ("arg1", 2)
     ( | 
     string                              | "arg1"
      " | 
      " | 
     , | 
     integer                             | 2
     ) | 
  function_definition                    | def func_with_args(): pass
   def | 
   identifier                            | func_with_args
   parameters                            | ()
    ( | 
    ) | 
   : | 
   block                                 | pass
    pass_statement                       | pass
     pass | 
 decorated_definition                    | @decorator1 @decorator2 def multiple_decorators(): pass
  decorator                              | @decorator1
   @ | 
   identifier                            | decorator1
  decorator                              | @decorator2
   @ | 
   identifier                            | decorator2
  function_definition                    | def multiple_decorators(): pass
   def | 
   identifier                            | multiple_decorators
   parameters                            | ()
    ( | 
    ) | 
   : | 
   block                                 | pass
    pass_statement                       | pass
     pass | 
 decorated_definition                    | @decorator_with_args("arg1", 2) @simple_decorator def...
  decorator                              | @decorator_with_args("arg1", 2)
   @ | 
   call                                  | decorator_with_args("arg1", 2)
    identifier                           | decorator_with_args
    argument_list                        | ("arg1", 2)
     ( | 
     string                              | "arg1"
      " | 
      " | 
     , | 
     integer                             | 2
     ) | 
  decorator                              | @simple_decorator
   @ | 
   identifier                            | simple_decorator
  function_definition                    | def multiple_decorators_mixed(): pass
   def | 
   identifier                            | multiple_decorators_mixed
   parameters                            | ()
    ( | 
    ) | 
   : | 
   block                                 | pass
    pass_statement                       | pass
     pass | 

```

[child ⬇️](#dc0fc767-7dcc-4b01-9b92-9f6b0043bc88)

---

(main branch ⎇)
###### dc0fc767-7dcc-4b01-9b92-9f6b0043bc88
[parent ⬆️](#8a08c651-f58b-4807-9a34-f3a310bd984c)
