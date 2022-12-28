# Creating lists in a shorter way
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

# One liner code the same as aboce using List Comprehension
# start the lists with x*7 or any equation then FOR loop after
multiples2 = [x*7 for x in range(1,11)]
print(multiples2)


# List Comprehension - create new lists based on sequences and ranges
# Usually a one liner code

# Ex:
languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C']
# same as the one liner above we start the line with an equation then followed by a for loop
lengths = [len(language) for language in languages]
print(lengths)

# Ex2:
# the following will have a conditional IF right after we set a specific range
z = [x for x in range(0,101) if x % 3 == 0]
print(z)