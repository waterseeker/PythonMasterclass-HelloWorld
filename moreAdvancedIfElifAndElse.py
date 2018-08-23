age = int(input("How old are you?"))

if age >= 16 and age <= 65:
    print("Have a good day at work!")

ageUsingParenthesesToMakeConditionsMoreExplicit = int(input("How old are you, really?"))

# using parentheses around conditions makes them easier to read
if (ageUsingParenthesesToMakeConditionsMoreExplicit >= 16) and (ageUsingParenthesesToMakeConditionsMoreExplicit == age):
    print("Using parentheses makes conditions easier to read.")

# you can also use the following syntax for AND
if 16 <= age <= 65:
    print("You can also use the if X >= Y >= Z syntax.")