# class SuperList(list):
#
#     def __len__(self):
#         return 100
#
#
# SuperList1 = SuperList()
#
# print(len(SuperList1))
#
# SuperList1.append(4)
# print(SuperList1[0])
#
from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capi(item):
    return item.upper()


new_items = list(map(capi, my_pets))
print(new_items)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))