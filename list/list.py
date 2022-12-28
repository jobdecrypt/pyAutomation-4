# sample list
# the first index in the list is 0 not 1. So it's 0,1,2,3,4,5,6...
x = ['Now', 'we', 'are', 'cooking']
print(type(x))
print(x)
print(len(x))
print(x[1])

# this is the slice. The first value is the FIRST Value to Slice and the second value is the LENGTH from "Zero" index
print(x[3:0])  # this will output "we"
# The next line will print out of range
# print(x[4]) # Out of range, because our list only have 3 indices


# 