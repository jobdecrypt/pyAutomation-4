# TUPLE - Sequences of elements of any type, that are immutable.  Also written in brackets.

# Sample Tuple
# The position of the elements inside the tuple have meaning.
fullname = ('Grace', 'M', 'Hopper')

# this function returns 3 elements which is a Tuple


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
# Check the type if it's a Tuple
print(type(result))
# this will result into a Tuple of hours, minutes, remaining_seconds
print(result)

# Assigning Variable name to the Tuple result which is => (1, 23, 20)
hours, minutes, seconds = result
print(hours, minutes, seconds)


