# Correcting the mistake: using the correct 'function_node' variable
print('Name:', extract_name(function_node.children_by_field_name('name')[0]))
print('Parameters Node:', function_node.children_by_field_name('parameters')[0])
print('Return Type Node:', function_node.children_by_field_name('return_type'))
print('Docstring Node:', function_node.children_by_field_name('docstring'))
print('Body Node:', function_node.children_by_field_name('body')[0])
== Output ==
Name: b''                                                                                                               
         Parameters Node: <Node type=parameters, start_point=(1, 20), end_point=(1, 58)>                                
                                                                                        Return Type Node: [<Node type=ty
pe, start_point=(1, 62), end_point=(1, 66)>]                                                                            
                                            Docstring Node: [<Node type="def", start_point=(1, 0), end_point=(1, 3)>, <N
ode type="->", start_point=(1, 59), end_point=(1, 61)>, <Node type=":", start_point=(1, 66), end_point=(1, 67)>]        
                                                                                                                Body Nod
e: <Node type=block, start_point=(2, 4), end_point=(3, 25)>


[child ⬇️](#2313e6bc-6aa0-483f-9dd6-6a47ea5ecd7f)

---

(main branch ⎇)
###### 2313e6bc-6aa0-483f-9dd6-6a47ea5ecd7f
[parent ⬆️](#515df655-8691-454e-8867-9f3f523c5897)
