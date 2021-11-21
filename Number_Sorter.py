# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

#defines if the number is and integer
def isInt(n):
    try:
        floatN = float(n)
        intN = int(floatN)
    except ValueError:
        return False
    else:
        return floatN == intN

#defines if the number is a float
def isFloat(n):
    try:
        floatN = float(n)
    except ValueError:
        return False
    else:
        return True

#function for getting the user number input and identifies its type
def getNumbers():
    num1 = input('Enter 1st number: ')
    if isInt(num1):
        num1 = int(num1)
    else:
        if isFloat(num1):
            num1 = float(num1)
    num2 = input('Enter 2nd number: ')
    if isInt(num2):
        num2 = int(num2)
    else:
        if isFloat(num2):
            num2 = float(num2)
    num3 = input('Enter 3rd number: ')
    if isInt(num3):
        num3 = int(num3)
    else:
        if isFloat(num3):
            num3 = float(num3)
    num4 = input('Enter 4th number: ')
    if isInt(num4):
        num4 = int(num4)
    else:
        if isFloat(num4):
            num4 = float(num4)
    return num1, num2, num3, num4


def numSort(n1,n2,n3,n4):
    high = max(n1,n2,n3,n4) #returns an item with the highest value
    low = min(n1,n2,n3,n4) #returns an item with the lowest value
    if high == n1:
        if low == n4:
            if n2 > n3:
                print(f'In descending order: {n1}, {n2}, {n3}, {n4}')
            else:
                print(f'In descending order: {n1} ,{n3} ,{n2}, {n4}')
        elif low == n2:
            if n3 > n4:
                print(f'In descending order: {n1}, {n3}, {n4}, {n2}')
            else:
                print(f'In descending order: {n1}, {n4}, {n3}, {n2}')
        else:
            if n2 > n4:
                print(f'In descending order: {n1}, {n2}, {n4}, {n3}')
            else:
                print(f'In descending order: {n1}, {n4}, {n2}, {n3}')
    elif high == n2:
        if low == n4:
            if n1 > n3:
                print(f'In descending order: {n2}, {n1}, {n3}, {n4}')
            else:
                print(f'In descending order: {n2}, {n3}, {n1}, {n4}')
        elif low == n3:
            if n4 > n1:
                print(f'In descending order: {n2}, {n4}, {n1}, {n3}')
            else:
                print(f'In descending order: {n2}, {n1}, {n4}, {n3}')
        else:
            if n4 > n3:
                print(f'In descending order: {n2}, {n4}, {n3}, {n1}')
            else:
                print(f'In descending order: {n2}, {n3}, {n4}, {n1}')
    elif high == n3:
        if low == n4:
            if n1 > n2:
                print(f'In descending order: {n3}, {n1}, {n2}, {n4}')
            else:
                print(f'In descending order: {n3}, {n2}, {n1}, {n4}')
        elif low == n1:
            if n4 > n2:
                print(f'In descending order: {n3}, {n4}, {n2}, {n1}')
            else:
                print(f'In descending order: {n3}, {n2}, {n4}, {n1}')
        else:
            if n4 > n1:
                print(f'In descending order: {n3}, {n4}, {n1}, {n2}')
            else:
                print(f'In descending order: {n3}, {n1}, {n4}, {n2}')
    else:
        if low == n1:
            if n3 > n2:
                print(f'In descending order: {n4}, {n3}, {n2}, {n1}')
            else:
                print(f'In descending order: {n4}, {n2}, {n3}, {n1}')
        elif low == n2:
            if n3 > n1:
                print(f'In descending order: {n4}, {n3}, {n1}, {n2}')
            else:
                print(f'In descending order: {n4}, {n1}, {n3}, {n2}')
        else:
            if n2 > n1:
                print(f'In descending order: {n4}, {n2}, {n1}, {n3}')
            else: 
                print(f'In descending order: {n4}, {n1}, {n2}, {n3}')

nOne,nTwo,nThree,nFour = getNumbers()
numSort(nOne,nTwo,nThree,nFour)