# Debugging the TypeError by printing the types of all variables involved in string concatenation
def debug_reconstruct_function(function: Function) -> None:
    parameter_strs = []
    for param in function.parameters:
        param_str = param.name
        print(f'param_str: {param_str}, type: {type(param_str)}')
        if param.type:
            print(f'param.type: {param.type}, type: {type(param.type)}')
            param_str += f': {param.type}'
        if param.default:
            print(f'param.default: {param.default}, type: {type(param.default)}')
            param_str += f' = {param.default}'
        parameter_strs.append(param_str)
    parameters = ', '.join(parameter_strs)

    print(f'function.return_type: {function.return_type}, type: {type(function.return_type)}')
    return_type = f' -> {function.return_type}' if function.return_type else ''

    print(f'function.docstring: {function.docstring}, type: {type(function.docstring)}')
    docstring = f'"""{function.docstring}"""' if function.docstring else ''

    print(f'function.body: {function.body}, type: {type(function.body)}')
    body = function.body if function.body else ''

    print(f'function.name: {function.name}, type: {type(function.name)}')
    reconstructed_code = f'def {function.name}({parameters}){return_type}:' + '\n' + docstring + '\n' + body
    print(f'reconstructed_code: {reconstructed_code}, type: {type(reconstructed_code)}')

