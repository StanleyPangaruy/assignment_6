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
def getNumber():
    num1 = input('1st number: ')
    if isInt(num1):
        num1 = int(num1)
    else:
        if isFloat(num1):
            num1 = float(num1)
    num2 = input('2nd number: ')
    if isInt(num2):
        num2 = int(num2)
    else:
        if isFloat(num2):
            num2 = float(num2)
    num3 = input('3rd number: ')
    if isInt(num3):
        num3 = int(num3)
    else:
        if isFloat(num3):
            num3 = float(num3)
    num4 = input('4th number: ')
    if isInt(num4):
        num4 = int(num4)
    else:
        if isFloat(num4):
            num4 = float(num4)
    return num1, num2, num3, num4


def numSort(a,b,c,d):
    high = max(a,b,c,d) #returns an item with the highest value
    low = min(a,b,c,d) #returns an item with the lowest value
    if high == a:
        if low == d:
            if b > c:
                print(a,b,c,d)
            else:
                print(a,c,b,d)
        elif low == b:
            if c > d:
                print(a,c,d,b)
            else:
                print(a,d,c,b)
        else:
            if b > d:
                print(a,b,d,c)
            else:
                print(a,d,b,c)
    elif high == b:
        if low == d:
            if a > c:
                print(b,a,c,d)
            else:
                print(b,c,a,d)
        elif low == c:
            if d > a:
                print(b,d,a,c)
            else:
                print(b,a,d,c)
        else:
            if d > c:
                print(b,d,c,a)
            else:
                print(b,c,d,a)
    elif high == c:
        if low == d:
            if a > b:
                print(c,a,b,d)
            else:
                print(c,b,a,d)
        elif low == a:
            if d > b:
                print(c,d,b,a)
            else:
                print(c,b,d,a)
        else:
            if d > a:
                print(c,d,a,b)
            else:
                print(c,a,d,b)
    else:
        if low == a:
            if c > b:
                print(d,c,b,a)
            else:
                print(d,b,c,a)
        elif low == b:
            if c > a:
                print(d,c,a,b)
            else:
                print(d,a,c,b)
        else:
            if b > a:
                print(d,b,a,c)
            else: 
                print(d,a,b,c)

x,y,z,s = getNumber()
numSort(x,y,z,s)
    










