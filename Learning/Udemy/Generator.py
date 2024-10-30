# range is a generator

# range(100)
# list(range(100))

# def make_list(num):
#   result = []
#   for i in range(num):
#     result.append(i**2)
#   return result

# my_list = make_list(100)
# print(my_list)


#################################
# # Custom generator: Table of given number

# def customGeneratorFunction(num):
#   for i in range(1, 11, 1):
#     yield i*num
# def createTable():
#   number = int(input("Enter the number to create the number table: "))
#   table = []
#   for item in customGeneratorFunction(number):
#     table.append(item)
#   return table
# my_table = createTable()
# print(my_table)
# -------------------

# gen = customGeneratorFunction(3)
# print(next(gen))
# print(next(gen))
# print(next(gen))
#################################

#################################
# # Under the hood of generators

# def special_for(iterable):
#   interator = iter(iterable)
#   while True:
#     try:
#       print(interator)
#       print(next(interator))
#     except StopIteration:
#       break
# special_for([1,2,3,4,5])
# ---------------------
# class MyGen():
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration
# gen = MyGen(0,10)
# for item in gen:
#   print(item)
#################################

#################################
# Exercise: Fibonacci Numbers
# ------------------ FAIL
# def fib(num):
#   fibList = []
#   first = 0
#   second = 0
#   for item in range(0, (num+1)):
#     fibList.append(first+second)
#     print("1", first+second)
#     first = second
#     print("2", first)
#     print("3", second)
#     second = item
#     print("3", item)
#   return fibList
# fibNum = fib(20)
# print(fibNum)
# # --------------------- FAIL
# def fib(num):
#   first = 0
#   second = 1
#   fibList = [first, second]
#   for item in range(0, (num+1)):
#     # yield first
#     temp = first
#     first = second
#     second = temp + second
#     fibList.append(first+second)
#   return fibList
# fibNum = fib(20)
# print(fibNum)
# ---------------------PASS
# def fib(num):
#   first = 0
#   second = 1
#   for item in range(num+1):
#     yield first
#     temp = first
#     first = second
#     second = temp + second
# fibList = []
# for x in fib(20):
#   fibList.append(x)
# print(fibList)
# # --------------------- PASS
def fib(num):
  first = 0
  second = 1
  fibList = []
  for item in range(0, (num+1)):
    fibList.append(first)
    temp = first
    first = second
    second = temp + second
  return fibList
fibNum = fib(20)
print(fibNum)
#################################