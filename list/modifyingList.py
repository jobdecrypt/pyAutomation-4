# APPEND - method adds a value to the lists
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

# INSERT - method gets the (index, value) and add the value to the lists
fruits.insert(0, "Orange")
print(fruits)

# REMOVE - method removes the value in the lists
fruits.remove("Melon")
print(fruits)

# POP - method also removes the value in the lists and returns the index that was removed
fruits.pop(3)
print(fruits)

# Assigning something else and add to the index position inside the lists
fruits[2] = "Strawberry"
print(fruits)

