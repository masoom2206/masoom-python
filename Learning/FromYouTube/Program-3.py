# Lists and Tuples

# List example [1, 2, 3]
# Tuple example (1, 2, 3)

# student = ["Karan", 67.7, 30, "Delhi"]
# print(student)
# student[0] = "Pawan"
# print(student)

marks = [4, 3, 5, 6, 2, 9]
# marks.append(12)
# print(marks)
# marks.append(1)
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)
marks.reverse()
print(marks)
# marks.insert(2, 55)
# print(marks)
# marks.remove(2)
# print(marks)
# marks.pop(2)
# print(marks)

# M1 = input("Your 1st movie: ")
# M2 = input("Your 1st movie: ")
# M3 = input("Your 1st movie: ")
# list = [M1, M2, M3]
# print("Your movies name=> ",list)

# Palindrome list
list1 = [1,2,3,2,1]
list2 = [1,2,3]

list1_copy = list1.copy()
list1_copy.reverse()
list2_copy = list2.copy()
list2_copy.reverse()
if(list1_copy == list1):
  print("Palindrome")
else:
  print("Not Palindrome")
if(list2_copy == list2):
  print("Palindrome")
else:
  print("Not Palindrome")