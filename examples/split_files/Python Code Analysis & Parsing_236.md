# Fixing the TypeError by decoding param.name
def reconstruct_function(function: Function) -> str:
    parameter_strs = []
    for param in function.parameters:
        param_str = param.name.decode('utf-8')
        if param.type:
            param_str += f': {param.type.decode('utf-8')}'
        if param.default:
            param_str += f' = {param.default.decode('utf-8')}'
        parameter_strs.append(param_str)
    parameters = ', '.join(parameter_strs)

    return_type = f' -> {function.return_type.decode('utf-8')}' if function.return_type else ''
    docstring = f'"""{function.docstring.decode('utf-8')}"""' if function.docstring else ''
    body = function.body.decode('utf-8') if function.body else ''

    return f'def {function.name.decode('utf-8')}({parameters}){return_type}:' + '\n' + docstring + '\n' + body

