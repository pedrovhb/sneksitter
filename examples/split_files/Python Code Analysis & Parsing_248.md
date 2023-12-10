# Fixing the AttributeError by removing unnecessary decode calls
def reconstruct_function(function: Function) -> str:
    parameter_strs = []
    for param in function.parameters:
        param_str = param.name
        if param.type:
            param_str += f': {param.type}'
        if param.default:
            param_str += f' = {param.default}'
        parameter_strs.append(param_str)
    parameters = ', '.join(parameter_strs)

    return_type = f' -> {function.return_type}' if function.return_type else ''
    docstring = f'"""{function.docstring}"""' if function.docstring else ''
    body = function.body if function.body else ''

    return f'def {function.name}({parameters}){return_type}:' + '\n' + docstring + '\n' + body

