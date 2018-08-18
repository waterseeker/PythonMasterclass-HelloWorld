parrot = "Norwegian Blue"
print(parrot)

# you can print a character at index X in a string by using
# print(yourStringHere[X])
# index is 0 based, so the thing in the first position is 0, not 1
x = 3
print('The character at index ' + str(x) + ' is ' + parrot[x] + '.')
# so how could I write a function in python
# that does/uses the same thing?
# take a string and an index as parameters
# and return the character at that index in the string that's passed in?
def returnCharacterAtIndexXFromString(a, b):
    return a[b]

testReturn = returnCharacterAtIndexXFromString('testString', 4)
print(testReturn)

#using variables
myString = 'The Spanish Inquisition'
myIndex = 4
testReturn = returnCharacterAtIndexXFromString(myString, myIndex)
print('This is the return from a function using variables. \nThe thing at index ' + str(myIndex) + ' is ' + testReturn + '.')

# you can also do negative indices
# these'll start from the end of the string
# so -1 would be the last character in the string.

lastLetterInTheString = myString[-1]
print('The last character in ' + myString + ' is ' + lastLetterInTheString + '.')

# you can access a slice of a string by passing 2 numbers
# the first number is the beginning index of the string
# and the second number is the length of the returned slice
print('The first 3 characters of ' + myString + ' are ' + myString[0:3] + '.')

# how can I use a for loop on the return of the slice to print
# the slice as a comma-separated list?
#
# get the slice
mySlice = myString[0:3]
# make an empty string to push to
insertedCommasIntoSlice = ""
# length of the slice
lengthOfSlice = len(mySlice)
# for loop
for i in range(lengthOfSlice):
    if i != lengthOfSlice - 1:
        insertedCommasIntoSlice += mySlice[i] + ", "
    else:
        insertedCommasIntoSlice += "and " + mySlice[i] + "."
print('The first 3 characters of ' + myString + ' are ' + insertedCommasIntoSlice)