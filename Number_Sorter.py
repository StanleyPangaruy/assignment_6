# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def isInt(n):
    try:
        floatN = float(n)
        intN = int(floatN)
    except ValueError:
        return False
    else:
        return floatN == intN

def isFloat(n):
    try:
        floatN = float(n)
    except ValueError:
        return False
    else:
        return True

#function for getting the user number input
def getNumber():
    firstNumber = input('1st number: ')
    if isInt(firstNumber):
        firstNumber = int(firstNumber)
    else:
        if isFloat(firstNumber):
            firstNumber = float(firstNumber)
    secondNumber = input('2nd number: ')
    if isInt(secondNumber):
        secondNumber = int(secondNumber)
    else:
        if isFloat(secondNumber):
            secondNumber = float(secondNumber)
    thirdNumber = input('3rd number: ')
    if isInt(thirdNumber):
        thirdNumber = int(thirdNumber)
    else:
        if isFloat(thirdNumber):
            thirdNumber = float(thirdNumber)
    fourthNumber = input('4th number: ')
    if isInt(fourthNumber):
        fourthNumber = int(fourthNumber)
    else:
        if isFloat(fourthNumber):
            fourthNumber = float(fourthNumber)
    return firstNumber, secondNumber, thirdNumber, fourthNumber

def numberarange(one,two,three,four):
    if one >= two and two >= three and three >= four:
        print(one,two,three,four)
    



# """

# 1,2,3,4
# 2,1,3,4
# 3,1,2,4
# 1,3,2,4
# 2,3,1,4
# 3,2,1,4
# 3,2,4,1
# 2,3,4,1
# 4,3,2,1
# 3,4,2,1
# 2,4,3,1
# 4,2,3,1
# 4,1,3,2
# 1,4,3,2
# 3,4,1,2
# 4,3,1,2
# 1,3,4,2
# 3,1,4,2
# 2,1,4,3
# 1,2,4,3
# 4,2,1,3
# 2,4,1,3
# 1,4,2,3
# 4,1,2,3
# """
a, b, c, d = getNumber()
numberarange(a,b,c,d)






