# METHODS - A Function associated with a specifice class

# Changing Characters
# using "index" method

pets = "Cats & Dogs"

# this will output the index position number of the given string inside the pets variable strings
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
# this will only prints the 1st 's' index position which is index '3' and not the 2nd one. Although there's two of them on the given var
print(pets.index("s"))

# Error
# print(pets.index('x')) # this will throw an error because there's no 'x' in pets var

# Finding words or characters inside a given var strings
# this will print out False because there's no word "Dragons" in our strings var pets
print("Dragons" in pets)
print("cats" in pets)  # this will print out False because it is case sensitive
print("Cats" in pets)  # this will print out True
