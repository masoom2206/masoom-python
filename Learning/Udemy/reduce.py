from functools import reduce
my_list = [1,2,3,4,5]
def accumulator(acc, item):
  print(acc, item)
  return acc + item

ne_item = reduce(accumulator, my_list, 0)

print(ne_item)