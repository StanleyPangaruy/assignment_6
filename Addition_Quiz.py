# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random
def questions():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1 + number2
    answer = int(input(f'1. {number1} + {number2} = '))
    if answer == total:
        print('Damn Youre good at this')
    else:
        print("so bad omegalul")

for i in range(10):
    questions()

#ten questions
#random functions call multiple times to create a new number. know the how many answers were right.