my_list = [1,2,3,4,5,6,7,8,9]
def multiply_by2(item):
  return item * 2
new_list = list(map(multiply_by2, my_list))
print(new_list)