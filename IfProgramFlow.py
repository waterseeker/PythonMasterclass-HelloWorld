# __author__ = 'dev'
# name = input("Please enter your name: ")
# # you can cast to an integer with int()
# # if you want to run > < = logic, you have to cast age to an int here
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You're old enough to vote.")
#     # you can have multiple lines of code in the same code blockß
#     print("Please put an X in the box.")
# else:
#     print("Sorry, {0}. You must be 18 years old to vote. Please come back in {1} years.".format(name, 18 - age))



# elif example
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print('Please guess higher.')
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it on your first guess!")

# refactoring the code to remove duplication
print("Please guess a number between 1 and 10.")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher.")
    else:
        print("Please guess lower.")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly.")
else:
    print("You got it in one!")