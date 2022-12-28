name  = "Manny"
number  = len(name) * 3
# This .format Method will format the inputs from the variables given
print("Hello {}, your lucky number is {}".format(name, number))

# This {} is a PLACEHOLDER 
print("Your lucky number is {number}, {name}.".format(name=name, number=number))

# Output the price of an item with and without Tax
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
# this next line will only output 2 decimal places
# {:.2f} means formatting Float number 2 decimals
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

# Celcius to Fahrenheit fixing the result indentations and Format
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    # {:>3} - ">" means align to the right with "3" spaces
    # {:>6.2f} - ">" means align to the right with "6" spaces and ".2f" two Float decimal places
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
