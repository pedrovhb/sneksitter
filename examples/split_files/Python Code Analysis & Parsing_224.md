# Debugging by isolating the part of the code causing the TypeError
def debug_reconstruct_function(function: Function) -> None:
    parameter_strs = []
    for param in function.parameters:
        param_str = param.name
        if param.type:
            param_str += f': {param.type}'
        if param.default:
            try:
                param_str += f' = {param.default.decode("utf-8")}'
            except TypeError as e:
                print(f'TypeError encountered: {e}')
                print(f'Type of param.default: {type(param.default)}')
        parameter_strs.append(param_str)
    parameters = ', '.join(parameter_strs)

    return_type = f' -> {function.return_type.decode("utf-8")}' if function.return_type else ''
    docstring = f'"""{function.docstring.decode("utf-8")}"""' if function.docstring else ''
    body = function.body.decode('utf-8') if function.body else ''

    print(f'Type of function.name: {type(function.name)}')
    print(f'Type of parameters: {type(parameters)}')
    print(f'Type of return_type: {type(return_type)}')
    print(f'Type of docstring: {type(docstring)}')
    print(f'Type of body: {type(body)}')

