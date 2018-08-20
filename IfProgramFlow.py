__author__ = 'dev'
name = input("Please enter your name: ")
# you can cast to an integer with int()
# if you want to run > < = logic, you have to cast age to an int here
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You're old enough to vote.")
    # you can have multiple lines of code in the same code blockß
    print("Please put an X in the box.")
else:
    print("Sorry, {0}. You must be 18 years old to vote. Please come back in {1} years.".format(name, 18 - age))