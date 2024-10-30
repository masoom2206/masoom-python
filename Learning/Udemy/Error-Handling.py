# Error handling if user didn't enter integer number
# try:
#   age = int(input("Enter your age. "))
#   print(f"You are {age} years old.")
# except:
#   print("Please enter a number")


# Error handling if user didn't enter integer number and also continue the program
# while True:
#   try:
#     age = int(input("Enter your age. "))
#     print(f"You are {age} years old.")
#   except:
#     print("Please enter a number")
#   else:
#     print("Thank you!")
#     break

# ===================

# while True:
#   try:
#     age = int(input("Enter your age: "))
#     div = 10/age# If user provided zeroin input
#     print(f"You are {age} years old.")
#   except ValueError:
#     print("Please enter a number")
#   except ZeroDivisionError:
#     print("Please enter a number greater than zero.")
#   else:
#     print("Thank you!")
#     break

# ===================

# while True:
#   try:
#     age = int(input("Enter your age: "))
#     div = 10/age# If user provided zero in input
#     if age < 18:
#       print("Age must be greater than 18.")
#       continue
#     print(f"You are {age} years old.")
#   except ValueError:
#     print("Please enter a number")
#   except ZeroDivisionError:
#     print("Please enter a number greater than zero.")
#   else:
#     print("Thank you!")
#     break


# ===================


# def addNum(num1, num2):
#   try:
#     return num1 + num2
#   except:
#     print("Something is wrong!")

# addNum('1', 2)

# def addNum(num1, num2):
#   try:
#     return num1 + num2
#   except TypeError:
#     print("Please enter Number!")

# addNum('1', 2)


# def addNum(num1, num2):
#   try:
#     return num1 + num2
#   except TypeError as err:
#     print("Please enter Number!" + err)

# addNum('1', 2)


# def addNum(num1, num2):
#   try:
#     return num1 + num2
#   except TypeError as err:
#     print(f"Please enter Number! {err}")

# addNum('1', 2)


# def addNum(num1, num2):
#   try:
#     return num1 / num2
#   except (TypeError, ZeroDivisionError):
#     print("Error")

# addNum('3', 0)


# def addNum(num1, num2):
#   try:
#     return num1 / num2
#   except (TypeError, ZeroDivisionError) as err:
#     print(err)

# addNum(3, 0)


# while True:
#   try:
#     age = int(input("Enter your age: "))
#     div = 10/age# If user provided zero in input
#     if age < 18:
#       print("Age must be greater than 18.")
#       continue
#     print(f"You are {age} years old.")
#   except ValueError:
#     print("Please enter a number")
#   except ZeroDivisionError:
#     print("Please enter a number greater than zero.")
#   else:
#     print("Thank you!")
#     break
#   finally:
#     print("Okay, I am finally done.")


# while True:
#   try:
#     age = int(input("Enter your age: "))
#     div = 10/age# If user provided zero in input
#     if age < 18:
#       print("Age must be greater than 18.")
#       continue
#     print(f"You are {age} years old.")
#     raise ValueError("Hey cut it out by Masoom")
#   # except ValueError:
#   #   print("Please enter a number")
#   except ZeroDivisionError:
#     print("Please enter a number greater than zero.")
#   else:
#     print("Thank you!")
#     break


while True:
  try:
    age = int(input("Enter your age: "))
    # div = 10/age# If user provided zero in input
    if age <= 0:
      raise ZeroDivisionError("Please enter a number greater than zero.")
    elif age < 18:
      raise ValueError("Age must be greater than 18.")
    print(f"You are {age} years old.")
  except ValueError as err:
    print(err)
  except ZeroDivisionError as err:
    print(err)
  else:
    print("Thank you!")
    break