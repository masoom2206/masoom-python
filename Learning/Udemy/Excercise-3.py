my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# found = ""
# for item in my_list:
#   if my_list.count(item) > 1 and item != found:
#     found = item
#     print(item, "-- Count = ", my_list.count(item))

duplicate = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)
print(duplicate)
