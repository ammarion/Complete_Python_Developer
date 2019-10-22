def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    print(operation_value)
    if is_float:
        final = "{} {}".format(kwargs.get('message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message', 'The result is'), int(operation_value))
        return final


c1 = calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
c2 = calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
