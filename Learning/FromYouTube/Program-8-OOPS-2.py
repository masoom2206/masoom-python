# del keyword
# Use to delete object properties or object itself

# class student:
#   def __init__(self, name):
#     self.name = name

# s1 = student("Masoom")
# print(s1.name)
# del s1.name
# del s1
# print(s1.name)

# ----------------------------------

# Private(Like) attribute and method
# To make attribute as private use __

# class Account:
#   def __init__(self, acc_no, acc_pass):
#     self.acc_no = acc_no
#     self.__acc_pass = acc_pass
#   def reset_pass(self):
#     return self.__acc_pass
#   def __get_det(self):
#     return self.acc_no
#   def get_acc(self):
#     return self.__get_det()

# ac1 = Account("220677", "Mas@2206")
# print("Account:", ac1.acc_no)
# print(ac1.reset_pass())
# print(ac1.get_acc())
# print("Pass:", ac1.__acc_pass) # Error due to private attribute

# ----------------------------------
# Inheritance
# single level inheritance

# class Car:
#   color = "Black"
#   @staticmethod
#   def start():
#     print("Car Started...")

#   @staticmethod
#   def stop():
#     print("Car Stopped!!!")

# class ToyattaCar(Car):
#   def __init__(self, name):
#     self.name = name

# c1 = ToyattaCar("Fortuner")
# c2 = ToyattaCar("Fortuner2")
# c1.start()
# print(c1.name)
# c2.stop()
# print(c2.name)
# print(c2.color)

# Multi level inheritance

# class Car:
#   color = "Black"
#   @staticmethod
#   def start():
#     print("Car Started...")

#   @staticmethod
#   def stop():
#     print("Car Stopped!!!")

# class ToyattaCar(Car):
#   def __init__(self, brand):
#     self.brand = brand

# class Fortuner(ToyattaCar):
#   def __init__(self, type):
#     self.type = type

# c1 = Fortuner("Diesel")
# print(c1.type)
# c1.start()


# Multiple inheritance

# class A:
#   varA = "This is Class A"
# class B:
#   varB = "This is Class B"

# class C(A, B):
#   varC = "This is Class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# super() method

# class Car:
#   def __init__(self, type):
#     self.type = type
#   color = "Black"
#   @staticmethod
#   def start():
#     print("Car Started...")

#   @staticmethod
#   def stop():
#     print("Car Stopped!!!")

# class ToyattaCar(Car):
#   def __init__(self, brand, type):
#     super().__init__(type)
#     self.brand = brand


# c1 = ToyattaCar("Toyatta", "Diesel")
# print(c1.type)
# c1.start()

# @staticClass

# class Person:
#   name = "Rahul"
#   # def changeName(self, Rname):
#   #   # self.__class__.name = Rname
#   #   # Person.name = Rname
#   #   self.name = Rname
#   @classmethod
#   def changeName(cls, name):
#     cls.name = name

# p1 = Person()
# p1.changeName("Masoom")
# print(p1.name)
# print(Person.name)


# @properity

# class Student:
#   def __init__(self, phy, chem, math):
#     self.phy = phy
#     self.chem = chem
#     self.math = math
#   @property
#   def calculatePercentage(self):
#     return str((self.phy + self.chem + self.math) / 3 )+ "%"
  
# s1 = Student(35, 55, 65)
# print(s1.calculatePercentage)
# s1.phy = 55
# print(s1.calculatePercentage)

# Polymorthism  # Operator Overloading

# print(2 + 5)
# print("Hello" + "World")
# print([1, 2, 3] + [7, 8, 9])

# class Complex:
#   def __init__(self, real, imagenary):
#     self.real  = real
#     self.imagenary = imagenary

#   def showNumber(self):
#     print(self.real, "i", self.imagenary, "j")

#   def addComplex(self, num2):
#     newReal = self.real + num2.real
#     newImagenary = self.imagenary + num2.imagenary
#     return Complex(newReal, newImagenary)

#   def __add__(self, num2): # Dunder function for add
#     newReal = self.real + num2.real
#     newImagenary = self.imagenary + num2.imagenary
#     return Complex(newReal, newImagenary)

#   def __sub__(self, num2): # Dunder function for add
#     newReal = self.real - num2.real
#     newImagenary = self.imagenary - num2.imagenary
#     return Complex(newReal, newImagenary)

# num1 = Complex(2, 6)
# num1.showNumber()

# num2 = Complex(3, 7)
# num2.showNumber()

# num3 = num1.addComplex(num2)
# num3.showNumber()

# num4 = num1 + num2
# num4.showNumber()
# num4 = num1 + num3
# num4.showNumber()
# num4 = num3 + num2
# num4.showNumber()

# num4 = num2 - num1
# num4.showNumber()


# Practice Question

# class Circle:
#   def __init__(self, radius):
#     self.radius = radius

#   def area(self): # pie r square
#     return (22/7) * self.radius ** 2
  
#   def perimeter(self): # 2 pie r
#     return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


class Order:
  def __init__(self, item, price):
    self.item = item
    self.price = price
  
  def __gt__(self, order2):
    return self.price > order2.price
  
ord1 = Order("chips", 20)
ord2 = Order("tea", 15)
print(ord1 >  ord2)