# myFile = open('/files/text-file.text')
# myFile = open('Udemy/files/text-file.text')

# print(myFile.read())
# myFile.seek(0)# move the cursore to beginning of the file.
# print(myFile.read())

# print(myFile.readline())
# print(myFile.readline())
# print(myFile.readline())

# print(myFile.readlines())# It's retuen list which contain entire line one by one.

# myFile.close()

# # ------------------------------------------ # Here you don't need to use close() function
# with open('Udemy/files/text-file.text', mode='r') as myFile:# defaulr mode always read(r)
#   # print(myFile)
#   print(myFile.read())


# # ------------------------------------------ # Use read and write mode
# with open('Udemy/files/text-file.text', mode='r+') as myFile:# defaulr mode always read(r)
#   text = myFile.write("Hello Its me Masoom!")
#   print(text)


# # ------------------------------------------ # use append mode
# with open('Udemy/files/text-file.text', mode='a') as myFile:# defaulr mode always read(r)
#   text = myFile.write("\nHello Its me Masoom!")
#   print(text)


# # ------------------------------------------ # use append mode
# with open('Udemy/files/text-file-2.text', mode='w') as myFile:# defaulr mode always read(r)
#   text = myFile.write("Hello Its me Masoom!\nHow are you")
#   print(text)


# # ------------------------------------------ # use append mode
# with open('/Users/masoom2206/coading/python/learning/Udemy/files/text-file-2.text', mode='r') as myFile:# defaulr mode always read(r)
#   text = myFile.read()
#   print(text)

# # ------------------------------------------ # use append mode
# with open('./Udemy/files/text-file-2.text', mode='r') as myFile:# defaulr mode always read(r)
#   text = myFile.read()
#   print(text)


# # ------------------------------------------ # use append mode
# with open('../learning/Udemy/files/text-file-2.text', mode='r') as myFile:# defaulr mode always read(r)
#   text = myFile.read()
#   print(text)


# # ------------------------------------------ # use append mode
# try:
#   with open('../learning/Udemy/files/text-my-file.text', mode='r') as myFile:# defaulr mode always read(r)
#     text = myFile.read()
#     print(text)
# except FileNotFoundError as err:
#   print("Your file does not exist.")
#   raise err


