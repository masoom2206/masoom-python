import re

string = "search inside of this text please, this is a string!"

# print("inside" in string)# retuen => True

# if re.search("this is", string):
#   print("Found")
# else:
#   print("Not Found")

# a = re.search("this", string)
# print(a)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

# pattern = re.compile("this")

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(b)

# pattern = re.compile(r"([a-zA-Z]).([a])")

# a = pattern.search(string)
# print(a.group())
# print(a.group(1))
# print(a.group(2))


pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = "masoom2206@gmail.com"
# string = "masoom2206"
email = input("Enter your email address: ")
try:
  userEmail = pattern.search(email)
  if  userEmail:
    print("This is a valid email")
    # At least 8 char lon, contain any letter and symbol(#$%@)
    # passPattern = re.compile(r"(([a-zA-Z0-9])+([@#$%&-_]?){8,})")
    passPattern = re.compile(r"[a-zA-Z0-9@#$%&-_]{8,}")
    password = input("Enter your passwors: ")
    userPass = passPattern.search(password)
    if userPass:
      print(email,password)
    else:
      print("Wrong Password!")
  else:
    print("This is not a valid email.")
except:
  print("Please enter email.")