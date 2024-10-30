# Generate a number 1~10

# Input from user?

# Check that input is a number between 1~10

# Check if number is the right guess, otherwise ask again.

from random import randint

# answer = randint(1, 10)
# # print(answer)

# while True:
#   try:
#     guess = int(input("Guess a number between 1~0 >> "))
#     # if int(guess) > 0 and int(guess) < 11:
#     if 0 < guess < 11:# another way of if condition
#       if guess == answer:
#         print(f"(: You are genious, system={answer}, yours={guess} :)")
#         break
#       else:
#         print("Try again!!")
#     else:
#       print("Number between 1~10")
#   except ValueError:
#     print("Please enter number between 1~10")
#     continue


# ------------------ #
# Below cose will be used by file path like:
# /usr/local/bin/python3 /Users/masoom2206/coading/python/learning/Udemy/RandomGame.py 5 15
# ------------------ #
# import sys
# first = int(sys.argv[1])
# last = int(sys.argv[2])
# answer = randint(first, last)
# print(answer)

# while True:
#   try:
#     guess = int(input(f"Guess a number between {first}~{last} >> "))
#     # if int(guess) > 0 and int(guess) < 11:
#     if first < guess < last:# another way of if condition
#       if guess == answer:
#         print(f"(: You are genious, system={answer}, yours={guess} :)")
#         break
#       else:
#         print("Try again!!")
#     else:
#       print(f"Number between {first}~{last}")
#   except ValueError:
#     print(f"Please enter number between {first}~{last}")
#     continue

answer = randint(1, 10)
counter = 0
while True:
  try:
    guess = int(input("Guess a number between 1~0 >> "))
    # if int(guess) > 0 and int(guess) < 11:
    if 0 < guess < 11:# another way of if condition
      if guess == answer:
        print(f"(: You are genious, system={answer}, yours={guess} :)")
        break
      else:
        counter += 1
        if counter == 3:
          print(f"Your all choices are wrong and you loss the game, the actual number is {answer}!")
          break
        else:
          print("Try again!!")
    else:
      print("Number between 1~10")
  except ValueError:
    print("Please enter number between 1~10")
    continue
