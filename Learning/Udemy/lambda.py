from functools import reduce
my_list = [6,4,5,8,3,9,2]

# Map with lambda
new_list = list(map(lambda item: item * 2, my_list))

print(new_list)

# Filter with lambda
new_filter = list(filter(lambda item: item %2 != 0, my_list))

print(new_filter)

# Reduce with lambda
new_reduce = reduce(lambda acc, item: acc + item, my_list)

print(new_reduce)

# Square my list
my_list = [5, 4, 3]

square_list = list(map(lambda num: num ** 2, my_list))

print(square_list)

#list sort by second item
my_list = [(0, 2), (4, 3), (10, -1), (6, 9), (3, 8)]
my_list.sort(key = lambda item: item[1])

print(my_list)