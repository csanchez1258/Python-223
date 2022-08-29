#Name: Christian Sanchez
#Date: 08/24/2022
#File Purpose: Multiple hello functions

def helloworld():
    return "Hello World!"

def helloname(name):
    return "Hello " + name + "!"

def printlist(list):
    for x in list:
        print(x)

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i
    return fact

def oddoreven(x):
    find = x % 2
    if find == 0:
        return "even"
    if find == 1:
        return "odd"