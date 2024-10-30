# // Functions and Recursion //

# function definition
# def cal_sum(a, b): #parameters
#   sum = a + b
#   return sum

# # Add 4 and 5
# num = cal_sum(4, 5) # function call Argument
# print(num)

# # Add 9 and 13
# num = cal_sum(9, 13)
# print(num)

# def calc_avg(a, b, c):
#   sum = a + b + c
#   avg = sum / 3
#   return avg

# avg = calc_avg(10,20,30)
# print(avg)
# print("Masoom","Haider",sep="\t",end='Sir')

# def calNum(a=1, b=1):
#   d = a * b
#   return d
# print(calNum())
# print(calNum(5))
# print(calNum(5,7))

# def calFact(num):
#   fact = 1
#   for i in range(1, num+1):
#     fact *= i
#   return fact
# num = int(input("Enter number to find factorial: "))
# print(calFact(num))

# def checkNum(num):
#   if(num % 2 == 0):
#     return "Even"
#   else:
#     return "Odd"
# num = int(input("Enter the number to check odd/even: "))
# result = checkNum(num)
# print(result)

# Recursive function
# def show(n):
#   if(n == 0): # Base case
#     return
#   print(n)
#   show(n-1)
# show(5) #Print 5, 4, 3, 2, 1

# def fact(n):
#   if(n == 1 or n == 0):
#     return 1
#   x = n * fact(n-1)
#   return x
# print(fact(5))

# def calNum(n):
#   if(n == 0):
#     return 0
#   sum = n + calNum(n-1)
#   return sum
# print(calNum(5))

def printList(list, index=0):
  if(index == len(list)):
    return
  print(list[index])
  printList(list, index+1)
list = ['a', 'b', 'c', 'd', 'e', 'f']
printList(list)