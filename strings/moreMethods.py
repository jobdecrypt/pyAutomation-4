# More Methods in formatting

# Upper Method
# this will capitalize all the strings of "Mountains"
print("Mountains".upper())

# Lower Method
# this will minimizes all the strings of "Mountains"
print("Mountains".lower())

# Strip Method - removes spaces, tabs, new line, whitespaces
print(' yes '.strip())  # prints 'yes' without whitespace

# Lstrip Method - removes LEFT whitespaces
print(' yes '.lstrip())  # prints 'yes' without whitespace

# Rstrip Method - removes RIGHT whitespaces
print(' yes '.lstrip())  # prints 'yes' without whitespace

# Count - will count how many times the Substring appears
print("The number of tiems e occurs in this string is 4".count("e"))

# Endswith - returns a string that ends with substring
print("Forest".endswith("rest"))  # returns True

# Isnumeric - returns boolean wether the string is Numeric
print("Forest".isnumeric())  # returns False
print("12345".isnumeric())  # returns True
# NOTE: to CONVERT the Numeric strings we can use the "int()" function
print(int('123456') + int('543210'))

# Join - this will join strings like the "+" sign to concatenante strings
print(" ".join(['This', 'is', 'a', 'phrase', 'joined', 'by', 'spaces']))
print("...".join(['This', 'is', 'a', 'phrase',
      'joined', 'by', 'triple', 'dots']))

# Split - this will Split the whitespaces between the given strings and can have a parameter ex: .split(,) - which split by the comma
print("This is an example for splitting whitespace".split())
print("This, is, an, example, for, splitting, comma's".split(","))

