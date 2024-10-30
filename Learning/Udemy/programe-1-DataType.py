# name = input("What is your anme? ")
# print("Hellooooo " + name)
# print("Hell0", name)


# print(2 / 4)
# print(9 // 4)

# print(round(3.68749, 2))

# print(abs(-2.5))

# print(20 + 3 * 4)

# Square root calculation

# import math
# print(math.sqrt(4))

# print(bin(55))
# print(int("0b110111", 2))

# name = "Masoom"
# age = 45

# print(f"Hello {name} you are {age} years old.")

# name = "Masoom"
# print(name[0:4:1])

# birth_year = input("What year were you born? ")
# age = 2024 - int(birth_year)
# print(f"Your age is: {age}")

# user = input("User name : ")
# password = input("Password : ")
# pass_len = len(password)
# print(f"Hello {user}, your password {'*' * pass_len} is {pass_len} letter long.")


# li = [1, 2, 3, 4]
# li[0] = 11
# new_li = li[:]
# new_li[0] = 111
# print(li)
# print(new_li)



user = {
  'fName': "Masoom",
  'lName': "Haider"
}
print(user.get("fName", "Raj"))
print(user.get("age", 45))