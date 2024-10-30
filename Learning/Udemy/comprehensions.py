my_list = []
for char in "Hello":
  my_list.append(char)

# print(my_list)

# Now same functionality by list comprehensions
my_list = [char for char in "Heeelllllo"]
# print(my_list)

my_list2 = [num for num in range(0,10)]
# print(my_list2)

my_list3 = [num*2 for num in range(1,11)]
# print(my_list3)

my_list4 = [num for num in range(0,100) if num % 2 != 0]
# print(my_list4)

my_list5 = [num**2 for num in range(0,100) if num % 2 != 0]
# print(my_list5)


# Now same functionality by set comprehensions
my_list = {char for char in "Heeelllllo"}
# print(my_list)

my_list2 = {num for num in range(0,10)}
# print(my_list2)

my_list3 = {num*2 for num in range(1,11)}
# print(my_list3)

my_list4 = {num for num in range(0,100) if num % 2 != 0}
# print(my_list4)

my_list5 = {num**2 for num in range(0,100) if num % 2 != 0}
# print(my_list5)


# Now same functionality by Dictionary comprehensions
simple_dict = {
  'a': 1,
  'b': 2,
  'c': 3
}
my_dict = {key:value**2 for key, value in simple_dict.items()}
# print(my_dict)


simple_dict = {
  'a': 1,
  'b': 2,
  'c': 3
}
my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}
# print(my_dict)

my_dict = {num:num**2 for num in [2,5,9,7]}
# print(my_dict)

# Duplicate the value from list
some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'm', 'n']
duplicate = []
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicate:
      duplicate.append(value)

# print(duplicate)

# Now same the above functionality by list comprehensions
some_list = ['a', 'm', 'b', 'a', 'c', 'a', 'b', 'd', 'n', 'm', 'n']
duplicate = list(set([item for item in some_list if some_list.count(item) > 1]))
duplicate.sort()

print(duplicate)