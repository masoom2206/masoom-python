# Decorator

# def my_decorator(func):
#   def wrap_func():
#     print("***************")
#     func()
#     print("***************")
#   return wrap_func

# @my_decorator
# def hello():
#   print("Hay Helllooooo!")

# # hello()

# @my_decorator
# def bye():
#   print("Hay see you later!")

# # bye()

# def hello2():
#   print("Hay Helllooooo!")

# hello3 = my_decorator(hello2)

# # hello3()

# my_decorator(hello2)()


# def my_decorator(func):
#   def wrap_func(s):
#     print("***************")
#     func(s)
#     print("***************")
#   return wrap_func

# @my_decorator
# def hello(greeting):
#   print(greeting)

# hello("Hiiiii")


# def my_decorator(func):
#   def wrap_func(s, e):
#     print("***************")
#     func(s, e)
#     print("***************")
#   return wrap_func

# @my_decorator
# def hello(greeting, emoji):
#   print(greeting, emoji)

# hello("Hiiiii", ":)")


# def my_decorator(func):
#   def wrap_func(*args, **kwards):
#     print("***************")
#     func(*args, **kwards)
#     print("***************")
#   return wrap_func

# @my_decorator
# def hello(greeting, emoji = ":("):
#   print(greeting, emoji)

# hello("Hiiiii")


# Check the function execution time

# from time import time
# def performance(fu):
#   def wrapper(*args, **kwards):
#     t1 = time()
#     result = fu(*args, **kwards)
#     t2 = time()
#     print(f"It's took {t2-t1} second")
#     return result
#   return wrapper

# @performance
# def long_time():
#   num = 0
#   for i in range(10000000):
#     num += i
#     # print(num)
#   return num

# print(long_time())


# **********************Excercise**********************

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Sorna",
    "valid": True,  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
