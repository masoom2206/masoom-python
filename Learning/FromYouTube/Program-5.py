# Loops in Python

# Print Hello 5 times
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# Using loop

# count = 1
# while count <= 5:
#   print("Hello", count)
#   count += 1
# print(count)

# i = 1
# while i <= 5:
#   print(i)
#   i += 1
# print("Loop end", i)

# i = 5
# while i >= 1:
#   print(i)
#   i -= 1
# print("Loop end", i)

# Excersize

# i = 1
# while i <= 10:
#   print(i*17)
#   i += 1
# print("Loop end Table of 2", i)

# num = int(input("Enter number for table: "))
# i = 1
# while i <= 10:
#   print(i*num)
#   i += 1
# print("Loop end Table of 2", i)


# i = 1
# while i <= 10:
#   n = i*i
#   i += 1
#   print(n)
# print("Loop end", i)


# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# # while idx <= len(num)-1:
# while idx < len(num):
#   print(num[idx])
#   idx += 1
# print("End Loop")

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# search = int(input("Search the number: "))
# idx = 0
# while idx < len(num):
#   if(num[idx] == search):
#     print("Indexof value: ", idx)
#     print("Found the value: ", search)
#     break # Break the loop
#   else:
#     print("Finding...")
#   idx += 1
# print("End Loop")

# i = 1
# while i <= 5:
#   if(i == 3):
#     i += 1
#     continue # Skip rest lines
#   print(i)
#   i += 1
# print("End loop")

# i = 1
# while i <= 10:
#   if(i % 2 != 0):
#     i += 1
#     continue # Skip rest lines
#   print(i)
#   i += 1
# print("End loop")

# ---------------------------------------------------- #
# list = [9,3,"D",0,"M"]
# for el in list:
#   print(el)
# print("Loop Ended")

# nums = (2,0,8,9,3,4,6)
# for val in nums:
#   print(val)
# print("Loop Ended")

# str = "Masoom Haider"
# for val in str:
#   print(val)
# else:
#   print("Loop Ended")

# ---------------------------------------- #
# // range(start?, stop, step?) //

# for el in range(5): # range(start)
#   print(el)

# for el in range(1, 4): # range(start, stop)
#   print(el)

# for el in range(1, 5, 2): # range(start, stop, step)
#   print(el)

# for el in range(2, 10, 2): # Print even number
#   print(el)

# for el in range(1, 10, 2): # Print odd number
#   print(el)

# for el in range(100, 0, -1): # print 100 to 1
#   print(el)

# n = int(input("Enter the number "))
# for i in range(1, 11): # print table of any number
#   print(n*i)


# for i in range(5): # This loop will use in future
#   pass
# print("End")


# Excersize
# n = 6
# z = 0
# for i in range(1, n):
#   z += i
#   print(i+i)
# print("Total = ",z)


# n = 6
# z = 1
# for i in range(1, n):
#   z *= i
#   print(i+i)
# print("Total = ",z)

# n = 5
# z = 1
# i = 1
# while i <= n:
#   z *= i
#   i += 1
#   print(i+i)
# print("Total = ",z)


# find the number divided by 1 - 10 Ans is 2520

i = 1
finalNumber = 0
while i > finalNumber:
  z = 0
  for x in range(1, 11, 1):
    if(i % x == 0):
      z += 1
    if(z == 10):
      finalNumber = i
  if(finalNumber == 0 and z != 10):
    i += 1
print("Final number = ",finalNumber)
