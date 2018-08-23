import random
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

fingers = int(input("How many fingers am I holding up?"))

computerFingers = random.randint(1,11)
if (fingers < 0) or (fingers > 10):
    print("What kind of hands do you think I have?")
elif fingers == computerFingers:
    print("Great guess, you got it!")
else:
    print("Womp womp. Better luck next time.")