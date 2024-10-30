from random import randint

answer = randint(1, 10)
def runGame(guess, answer):
  if 0 < int(guess) < 11:# another way of if condition
    if guess == answer:
      print(f"(: You are genious, system={answer}, yours={guess} :)")
      return True
    else:
      print("Try again!!")
      return False
  else:
    print("Number between 1~10")
    return False

if __name__ == "__main__":
  while True:
    try:
      guess = int(input("Guess a number between 1~0 >> "))
      # if int(guess) > 0 and int(guess) < 11:
      if runGame(guess, answer):
        break
    except ValueError:
      print("Please enter number between 1~10")
      continue
