
# This is just to number the console/terminal output on each questions
def qNum(num):
    print('\n')
    print(f'# {num}:')
# ====================================================


# Question 1 - Lists
qNum(1)


def get_word(sentence, n):
    # Only proceed if n is positive
    print(n)
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        # print(words)
        if n <= len(words):
            return(words[n-1])
        return("")


print(get_word('This is a lesson about lists', 4))  # Should print: lesson
print(get_word('This is a lesson about lists', -4))  # Nothing
print(get_word('Now we are cooking!', 1))  # Should print: Now
print(get_word('Now we are cooking!', 5))  # Nothing

# QUESTION 2 - Tuple
qNum(2)
# Lets use tuples to store information about a file: its name, its type and its size in bytes.
# Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.


def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size/1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21

# QUESTION 3 - Tuple and enumerate
qNum(3)
# Try out the enumerate function for yourself in this quick exercise.
# Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.


def skip_elements(elements):
    result = []
    for index, value in enumerate(elements):
        if index % 2 == 0:
            result.append(value)
    return result


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

# QUESTION 4 - List Comprehensions
qNum(4)
# THe odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension.
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.


def odd_numbers(n):
    return [x for x in range(0, n + 1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []
