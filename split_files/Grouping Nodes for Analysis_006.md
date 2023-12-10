---
file: /home/pedro/Documents/chatgpt_export/Markdown/Grouping Nodes for Analysis.md
heading_stack: <root> -> 6db24c38-564f-43d4-b8c9-2fec4e4db353 -> System -> 2953287f-20e5-44fb-a584-4bfe4f961bbb -> System -> aaa23f50-fb72-4433-a7f7-075d9fdfe0f3 -> User
---
# User

How can we sanely group function/parameter nodes in an output such as this from some processed tree-sitter queries?

(<Node type=call, start_point=(2, 1), end_point=(2, 26)>, 'function.decorator')
(<Node type=identifier, start_point=(2, 1), end_point=(2, 10)>, 'decorator.name')
(<Node type=argument_list, start_point=(2, 10), end_point=(2, 26)>, 'decorator.args')
(<Node type=identifier, start_point=(3, 1), end_point=(3, 11)>, 'decorator.name')
(<Node type=identifier, start_point=(3, 1), end_point=(3, 11)>, 'function.decorator')
(<Node type=function_definition, start_point=(4, 0), end_point=(31, 58)>, 'function')
(<Node type=identifier, start_point=(4, 4), end_point=(4, 20)>, 'function.name')
(<Node type=parameters, start_point=(4, 20), end_point=(4, 66)>, 'function.parameters')
(<Node type=identifier, start_point=(4, 21), end_point=(4, 29)>, 'function.parameter.name')
(<Node type=type, start_point=(4, 31), end_point=(4, 34)>, 'function.parameter.type')
(<Node type=identifier, start_point=(4, 36), end_point=(4, 51)>, 'function.parameter.name')
(<Node type=type, start_point=(4, 53), end_point=(4, 57)>, 'function.parameter.type')
(<Node type=false, start_point=(4, 60), end_point=(4, 65)>, 'function.parameter.default')
(<Node type=type, start_point=(4, 70), end_point=(4, 90)>, 'function.return')
(<Node type=block, start_point=(5, 4), end_point=(31, 58)>, 'function.body_contents')
(<Node type=string, start_point=(5, 4), end_point=(8, 7)>, 'function.docstring')
(<Node type=block, start_point=(5, 4), end_point=(31, 58)>, 'function.body_contents')
(<Node type=string, start_point=(5, 4), end_point=(8, 7)>, 'function.docstring')
(<Node type=identifier, start_point=(34, 1), end_point=(34, 5)>, 'decorator.name')
(<Node type=identifier, start_point=(34, 1), end_point=(34, 5)>, 'function.decorator')
(<Node type=function_definition, start_point=(35, 0), end_point=(38, 46)>, 'function')
(<Node type=identifier, start_point=(35, 4), end_point=(35, 9)>, 'function.name')
(<Node type=parameters, start_point=(35, 9), end_point=(35, 73)>, 'function.parameters')
(<Node type=identifier, start_point=(35, 10), end_point=(35, 16)>, 'function.parameter.name')
(<Node type=type, start_point=(35, 18), end_point=(35, 21)>, 'function.parameter.type')
(<Node type=identifier, start_point=(35, 23), end_point=(35, 31)>, 'function.parameter.name')
(<Node type=type, start_point=(35, 33), end_point=(35, 36)>, 'function.parameter.type')
(<Node type=identifier, start_point=(35, 38), end_point=(35, 58)>, 'function.parameter.name')
(<Node type=type, start_point=(35, 60), end_point=(35, 64)>, 'function.parameter.type')
(<Node type=false, start_point=(35, 67), end_point=(35, 72)>, 'function.parameter.default')
(<Node type=type, start_point=(35, 77), end_point=(35, 93)>, 'function.return')
(<Node type=block, start_point=(36, 4), end_point=(38, 46)>, 'function.body_contents')


[child ⬇️](#b5e935e4-8ecf-4850-ac07-4d63ba79b17e)

---

(main branch ⎇)
###### b5e935e4-8ecf-4850-ac07-4d63ba79b17e
[parent ⬆️](#aaa23f50-fb72-4433-a7f7-075d9fdfe0f3)
