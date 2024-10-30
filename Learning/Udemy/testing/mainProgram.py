def do_stuff(num):
  if num:
    try:
      return int(num) + 5
    except ValueError as err:
      return err
  elif num == 0:
    return "Please enter the number greater than zero(0)"
  else:
    return "Please enter a number"

def do_stuff_multiply(num):
  return num * num

def do_stuff_true():
  return True

