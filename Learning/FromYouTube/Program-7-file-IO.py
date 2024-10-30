# file = open("demo.txt")
# read = file.read()
# file.close()
# print(read)
# print(type(read))

# file = open("demo.txt", "rt")
# # read = file.read()
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# file.close()
# # print(read)
# print(line1)
# print(line2)
# print(line3)
# print(type(line1))


# file = open("demo.txt", "w")
# file.write("-------\nThis file is for testing purpose.\n-------")
# file.close

# file = open("demo.txt", "a")
# file.write("""\nThis is demo.txt file.
# \nI am leaning python.
# \nI will use this file text in Python I/O program.""")
# file.close

# file = open("demo.txt", "rt")
# read = file.read()
# print(read)
# file.close()


# file = open("demo2.txt", "a+")
# file.write("My Name is Masoom")
# read = file.read()
# print(read)
# file.close()


# file = open("demo2.txt", "r+")
# file.write("My Name is Masoom\n")
# read = file.read()
# print(read)
# file.close()

# with open("demo.txt", "rt") as file:
#   data = file.read()
#   print(data)

# Delete file with the help of Python module

# import os
# os.remove("demo2.txt")


# Practice code

# file = open("practice.txt", "a+")
# file.write("""Hello every one
# We are learning file I/O
# using Python
# I am a programmer of Drupal(PHP)""")

# with open("practice.txt", "r") as file:
#   data = file.read()

# print(data)
# new_data = data.replace("Java", "Python")

# with open("practice.txt", "w") as file:
#   file.write(new_data)

# print(new_data)

# word = "learning"
# with open("practice.txt", "r") as file:
#   data = file.read()
#   if(data.find(word) != -1):
#     print("Found")
#   else:
#     print("Not Found")

# def checkForWord(word):
#   with open("practice.txt", "r") as file:
#     data = file.read()
#     if(data.find(word) != -1):
#       print("Found")
#     else:
#       print("Not Found")
# checkForWord("learningb")

# def checkForLine(word):
#   data = True
#   lineNumber = 1
#   with open("practice.txt", "r") as file:
#     while data:
#       data = file.readline()
#       if(word in data):
#         print("Found")
#         print(lineNumber)
#         return
#       else:
#         lineNumber += 1
#         print("Not Found")
# checkForLine("learning")

count = 0
with open("numberFile.txt", "r") as file:
  data = file.read()
  nums = data.split(",")
  print(nums)
  for val in nums:
    if(int(val) % 2 == 0):
      count += 1
print(count)