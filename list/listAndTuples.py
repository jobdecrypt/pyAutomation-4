animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for animal in animals:
    chars += len(animal)

print('Total characters: {}, Average length: {}'.format(chars, chars/len(animals)))

# Enumerate function with tuples

winners = ['Ashley', 'Dylan', 'Reese']
# The values in tuple are the index and person
# enumerate will enumerate the values in winners list
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# For example you have a tuple called "people" which the first value is the email and the second value is the full name of the person's email

def full_emails(people):
    result = []
    for email, name in people:
        result.append('{} <{}>'.format(name, email))
    return result

print(full_emails([('alex@example.com', 'Alex Diego')]))

