#  // Dictionary and set //

#  // Dictionary //

# info = {
#   "name": "Masoom",
#   "age": 47,
#   "Subject": ["PHP", "Drupal", "Python"],
#   "is_adult": True 
# }
# print(type(info))
# print(info)
info = {
  "name": "Masoom",
  "age": 47,
  "Subject": {"PHP", "Drupal", "Python"},
  "is_adult": True 
}
# print(type(info))
# print(list(info.keys()))
# print(info.values())
# print(info.items())
# print(info["name"])
# print(info["name2"])
# print(info.get("name2"))
# info.update({"city" : "Greater Noida"})
# new_info = {"city" : "Greater Noida"}
# info.update(new_info)
# print(info)

# // Set //

collection = {1, 2, 3, 4, 1, 2, 5, "hello", "world", "hello"}
# print(type(collection))
# print(collection)
# print(len(collection))
# Empty set
# collection = set()
# collection.add("Masoom")
# collection.add("Hello")
# collection.add("Haider")
# # collection.remove("Hello")
# print(type(collection))
# print(collection)
# print(collection.pop())

col1 = {1,2,3,9}
col2 = {7,8,9,3}
col3 = col1.union(col2) # Merge the set
col4 = col1.intersection(col2) # Get unique value from set
# print(col3)
# print(col4)

# Excersize


# marks = {}
# ch = int(input("Enter chamestry marks: "))
# marks.update({"ch": ch})
# mt = int(input("Enter math marks: "))
# marks.update({"mt": mt})
# en = int(input("Enter english marks: "))
# marks.update({"en": en})
# print("Here is your result: ", marks)


# col1 = {1, "1.0",2,3,9,"2.0","3.0"}
# print(col1)

# col1 = {
#   ("float", 9.0),
#   ("int", 9)
# }
# print(col1)