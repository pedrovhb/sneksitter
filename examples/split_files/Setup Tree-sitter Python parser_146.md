# or: q1 = Q.filter(parent__type="function_def")
q2 = ...
attr = A().parent.type
attr2 = A().children["block"].named_children[0].type
q3 = attr != attr2
q4 = (q1 & q2) | q3
