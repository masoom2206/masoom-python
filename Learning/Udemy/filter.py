my_list = [1,2,3,4,5,6,7,8,9]
def get_odd(item):
  return item % 2 != 0
new_list = list(filter(get_odd, my_list))
print(new_list)