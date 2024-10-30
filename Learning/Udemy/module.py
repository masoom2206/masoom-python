# import utility module file here
# import utility
# print(utility)

# function used from utility.py file after import
# print(utility.divide(6, 5))
# print(utility.multiply(4, 12))

# Function used from shopping package
# Packages are used to add multiple modules in a single package folder.
# import shopping.shoping_cart

# print(shopping.shoping_cart.buy("Apple"))

# Now import he buy function from shopping > new_shop folder
# import shopping.new_shop.shoping_cart
# print(shopping.new_shop.shoping_cart.buy("Banana"))

# There are another way to import the function and direclty use the function
# from shopping.new_shop.shoping_cart import buy
# print(buy("Kela"))

# Import from utility file
# from utility import multiply, divide
# print("Multiply", multiply(2,3))
# print("Divide", divide(4,3))

# Import the entire shoping_cart module
# from shopping.new_shop import shoping_cart
# print(shoping_cart.buy("Ball"))

# Import from utility file
# import utility
# print("Multiply:", utility.multiply(5,2))
# print("Divide:", utility.divide(5,2))
# print(max([2,4,7,9]))
# print("Max:", utility.max())


# Another way to Import from utility file
# from utility import divide, max, multiply
# print("Multiply:", multiply(5,2))
# print("Divide:", divide(5,2))
# print(max([2,4,7,9]))
# print("Max:", max()) # max function has overwrite here
