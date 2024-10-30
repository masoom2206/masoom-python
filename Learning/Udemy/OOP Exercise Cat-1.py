class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age

cat1 = Cat("cat1", 5)
cat2 = Cat("cat2", 7)
cat3 = Cat("cat3", 3)

def oldest_cat(*avg):
  return max(avg)

print(f"Oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old")