age = int(input("How old are you?"))

if age >= 16 and age <= 65:
    print("Have a good day at work!")

ageUsingParenthesesToMakeConditionsMoreExplicit = int(input("How old are you, really?"))

if (ageUsingParenthesesToMakeConditionsMoreExplicit >= 16) and (ageUsingParenthesesToMakeConditionsMoreExplicit == age):
    print("Using parentheses makes conditions easier to read.")