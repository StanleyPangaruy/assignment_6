# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

#imports the specific method from a module
from random import randint
from operator import add

def add_quiz():
    #starting score    
    score = 0 
    item = 0
    #loops the code block
    for item in range(10):
        # gives random number from 0 to 99
        num1 = randint(0,99)
        num2 = randint(0,99)
        # the system adds the two randomly generated numbers
        sysAnswer = add(num1,num2)
        # asks for the user's input on the addition expression.
        userAnswer = int(input(f'{num1} + {num2} = '))
        if sysAnswer == userAnswer:
            print('Correct')
            score = score + 1
            item = item + 1
        else:
            print(f'Incorrect, Correct answer is {sysAnswer}')
            item = item + 1
        #if the number of items reaches 10, it ends the loop and prints the result summary.
        if item == 10: 
            print(f"Your final score is {score} out of 10.")    

add_quiz()


