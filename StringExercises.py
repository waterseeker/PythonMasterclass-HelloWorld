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

# if you don't include the first number in the slice
# it'll start at the beginning of the string by default
# so myString[:3] will return the same things as myString[0:3]
print('--------------------------------------------------')
print(myString[:3])
print('and')
print(myString[0:3])
print('are the same.')
print('--------------------------------------------------')
# if you leave out the second number
# it'll skip the number of spaces == the first number and then print everything else to the end of the string.
print(myString[4:])
print('--------------------------------------------------')
# if you use negative numbers
# tit'll start from the end of the string and count back the # of spaces in the 1st number
# with the last letter in the string being #1
# and print out until the # of spaces from the end of the string = the second number
print(myString[-11:-2])
print('--------------------------------------------------')
# you can also skip characters
# if you use [X:Y:Z] format
# X = starting position
# Y = extracts all of the characters up to and including this
# Z = and prints out every Zth character starting with the character at position Z
print(myString)
print(myString[0:6:2])
print(myString[:6:2])
print('--------------------------------------------------')
# you can use this to ignore or print out characters at certain intervals.
# for example, you could print out only the commas in these numbers
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
# leaving out the middle number will continue the pattern to the end of the string
print("So 'numbers[1::3]' will print out the character at position 1(a comma), and the character\n"
      "every 3 positions forward from there (in this case also commas) until the end of the string.")
print(numbers[1::3])
print('--------------------------------------------------')
# you can cancatenate string literals without using the '+' operator
print("You " "can " "cancatenate " "string " "literals " "without " "using " "'+'.")

