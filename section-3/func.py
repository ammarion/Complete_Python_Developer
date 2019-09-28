def names(first, last):
    def more_names(a, b):
        return f'{a} {b}'
    return more_names(first, last)


ammar = names('Ammar', 'Alim')
print(ammar)