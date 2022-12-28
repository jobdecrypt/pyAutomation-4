# Slice - The portion of a string that can contain more than one character; also sometimes called a substring

color = "Orange"
print(color[1:4]) # we do a range here form index '1' to '4'

fruit = 'Pineapple' 
print(fruit[:4]) # the range is from index '0' to index '4' 
print(fruit[4:]) # the range is from index '4' to the end of index

# Adding through Slice [:]

print(fruit[:3] + fruit[3:]) # prints out Pineapple

# Creating New Strings and Fixing typo's

message = "A kong string with a silly typo"
# message[2] = "l" # this will throw an error because Python Strings are not MUTABLE

# here we make a new string from the old message variable
newMessage = message[0:2] + 'l' + message[3:]
print(newMessage)

# Changing Characters
