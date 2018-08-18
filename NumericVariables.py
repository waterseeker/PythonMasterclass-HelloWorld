a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# python returns a float as the result of division by default
print(a // b)
# if you want to force it to return the result as a whole number, you
# have to use the '//' operator
print(a % b)

# demonstrating some problems you might run into with / and // in for loops

# this returns 1, 2, 3
for i in range(1, 4):
    print('The index is ' + str(i))

# this will give us an error
# 'TypeError: 'float' object cannot be interpreted as an integer'
# because the return of a/b is, by default, a floating point number
#
# for i in range(1, a / b):
#     print(i)

# if we use the '//' operator, the code will run
# because it forces the return to be a whole number (int)
for i in range(1, a//b):
    print('The index using the // operator is ' + str(i))

# python follows the order of operations.
# good ole PEMDAS
# Parentheses and other grouping symbols
# Exponents
# Multiplication and division from left to right
#   so if there is a division operation before you get to the multiplication
#   you perform that division first
# Then Addition and Subtraction from left to right
#   with the same caveat... if you run into a subtraction operation before
#   you hit addition, you calculate that subtraction first.
print(a + b / 3 - 4 * 12)
print('These both return ' + str(8 * 3 / 2))
print('These both return ' + str(8 / 2 * 3))

print('But these both return ' + str(8 * 3 // 2))
print('But these both return ' + str(8 // 2 * 3))

# you can force an order of operations by using parentheses
print('This forces left-to-right calculation and returns ' + str((((a + b) / 3) - 4) * 12))

# you can also use variables to store the steps of the calculation
# to control the flow of operations
# or make the code a little easier to follow for the reader

c = a + b
d = c / 3
e = d - 4
print('You can control the order of operations by using variables too! The answer is ' + str(e * 12))