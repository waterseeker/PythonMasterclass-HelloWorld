__author__ = 'dev'
# you can cast numbers to strings by using the str() method
age = 24 # a number
print("I am " + str(age) + " years old.")
print("--------------------------------------------------------------------------------")

# you can do the same thing by using a 'replacement field'

print("I am {0} years old.".format(age))
print("--------------------------------------------------------------------------------")

# the number you pass into the {}, corresponds to the index of the argument passed to .format()
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}.".format(31, "January", "March", "May",
        "July", "August", "October", "December"))
print("--------------------------------------------------------------------------------")

# you can use triple quotes to break a string over multiple lines
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))
print("--------------------------------------------------------------------------------")

# an old way of doing something like this is...
print("I am %d years old" % age)
print("I am %d %s, %d %s old." % (age, "years", 6, "months"))
print("--------------------------------------------------------------------------------")

# the ** operator is used to raise to a power
# so X ** Y = X to the power of Y
print("The ** operator is used to raise to a power.")
print("2 to the power of 9 is {0}.".format(2 ** 9))
print("--------------------------------------------------------------------------------")
# if you use a number before the letter in the %X operation
# the number is the # of spaces that the replacement will use
# for example, the following assigns 2 spaces for the first set of numbers
# and 4 for the second.
# this helps to format the output to make it easier to read.
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))
# if you don't assign the # of spaces, it makes it harder to read in this instance
print("--------------------------------------------------------------------------------")
print("Without assigning spaces, the output is harder to read")
for i in range(1, 12):
    print("No. %d squared is %d and cubed is %d" %(i, i ** 2, i ** 3))