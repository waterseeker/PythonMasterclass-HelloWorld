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