# // OOPS Part 1 //

# Example Class

# class Student:
#   name = "Masoom"
# s1 = Student()
# print(s1)
# print(s1.name)
# s2 = Student()
# print(s2.name)

# -----------------------------------------

# class Student:
#   name = "Haider"
#   def __init__(self):
#     print("Adding Student in Database...")
# s1 = Student()

# -----------------------------------------

# class Student:
#   def __init__(self, fullname):
#     self.name = fullname
#     print("Adding Student in Database...")
# s1 = Student("Syed Masoom Haider")
# print("FullName = ", s1.name)
# s2 = Student("Rajesh Kumar")
# print("FullName = ", s2.name)

# -----------------------------------------

# class Student:

#   CollageName = "IGNOU"  # Class attributes
#   def __init__(self, fullname, marks):
#     self.name = fullname # Object attributes 
#     self.marks = marks
#     print("Adding Student in Database...")

# s1 = Student("Syed Masoom Haider", 98)
# print("FullName = ", s1.name, "\nAnd Marks = ", s1.marks)

# s2 = Student("Rajesh Kumar", 89)
# print("FullName = ", s2.name, "\nAnd Marks = ", s2.marks, "\nCollage Name = ", s2.CollageName)

# print("Only Collage Name = ", Student.CollageName)

# -----------------------------------------

# class Student:

#   CollageName = "IGNOU"  # Class attributes

#   def __init__(self, fullname, marks):
#     self.name = fullname # Object attributes 
#     self.marks = marks

#   def welcome(self):
#     print("Welcome", self.name, "From", self.CollageName, "You have total marks as", self.marks)

#   def getMarks(self):
#     return self.marks

#   def getName(self):
#     return self.name

# s1 = Student("Syed Masoom Haider", 98)

# s1.welcome()
# print(s1.getMarks())
# print(s1.getName())

# -----------------------------------------

# Practice Question

# class Student:

#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   def getAvg(self):
#     sum = 0
#     count = 0
#     for mark in self.marks:
#       sum += mark
#       count += 1
#     marksAvg = sum / count
#     print("Hello", self.name,"Your total marks is", sum," and your marks average is", marksAvg,"%")

#   @staticmethod #decorator
#   def welcome(): #a static method/function
#     print("Hello")

# s1 = Student("Masoom", [98, 76, 54, 55, 76])
# s1.getAvg()
# s2 = Student("Rajesh", [55, 42, 43, 54, 98, 78, 53, 23, 32])
# s2.getAvg()
# s2.welcome()

# -----------------------------------------

# Abstraction  >> Hide the internal functionality from user

# class Car:
#   def __int__(self):
#     self.clutch = False
#     self.brk = False
#     self.acklator = False
#   def startCar(self):
#     self.clutch = True
#     self.acklator = True
#     print("Car Started...")
# car = Car()
# car.startCar()

# -----------------------------------------

# Practice 2

class Account:
  def __init__(self, account_no, balance):
    self.account_no = account_no
    self.balance = balance
  def debit(self, amount):
    self.balance -= amount
    print("Yout amout", amount, "has been debited from you account.")
    print("Total Balance =", self.getBalance())
  def credit(self, amount):
    self.balance += amount
    print("Yout amout", amount, "has been credited from you account.")
    print("Total Balance =", self.getBalance())
  def getBalance(self):
    return self.balance
acc = Account(153042, 10530)
acc.debit(500)
acc.credit(1500)
acc.credit(40000)
acc.debit(15500)
acc.debit(22500)