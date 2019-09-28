# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# i = 0
# for item in my_list:
#     i += item
#
# print(i)
#

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'Index of 50 is: {i}')

