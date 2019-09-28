some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)

some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates = []
for item in some_list:
    if some_list.count(item) > 1:
        duplicates.append(item)
print(list(set(duplicates)))