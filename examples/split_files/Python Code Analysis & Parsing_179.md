# Let's print the text content of these nodes.
name_node = [child for child in function_node.children if child.type == 'identifier'][0]
block_node = [child for child in function_node.children if child.type == 'block'][0]
print('Name Node Text:', name_node.text.decode('utf-8'))
print('Block Node Text:', block_node.text.decode('utf-8'))
== Output ==
Name Node Text: example_function                                                                                        
                                Block Node Text: '''This is a docstring.'''                                             
                                                                               print(param1, param2)


[child ⬇️](#aaa2984d-4402-44f6-9e18-80341c4ad3b4)

---

(main branch ⎇)
###### aaa2984d-4402-44f6-9e18-80341c4ad3b4
[parent ⬆️](#a456192a-716c-4476-b58c-ea5c2bc357a5)
