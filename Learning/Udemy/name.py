# print __name__ from import file.
from utility import divide, multiply
from shopping.new_shop import shoping_cart

print(shoping_cart.buy("Ball"))
print("Multiply:", multiply(5,2))
print("Divide:", divide(5,2))

# print("name", __name__)
if __name__ == '__main__':
  print("Please run this.")
