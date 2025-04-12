# https://github.com/gregtwallace2/lab10-MFG-GTW
# Partner 1: Maria Guerra
# Partner 2: Gregory Wallace


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example

import math
def square_root(a):
    try:
        if a<0:
            raise ValueError("Cannot take square root of a negative number!")
        return math.sqrt(a)
    except ValueError as error:
        print(f"Error: {error}")
        return None

def hypotenuse (a,b):
    try:
        return math.hypot(a,b)
    except Exception as error:
        print(f"Unexpected error: {error}")
        return None


def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def logarithm(a,b):
    if a<=0 or a==1:
        raise ValueError("Logarithm base must be positive and not equal to 1! ")
    if b<=0:
        raise ValueError("Logarithm argument must be positive! ")
    return math.log(b,a)

def exponent(a,b):
    return a**b


import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("cannot divide by 0")
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if a <= 1:
        raise ValueError("log base must be greater than 0")
    if b <= 0:
        raise ValueError("log value must be greater than 0")

    return math.log(b, a)
    # use math library + raise ValueError

def exp(a, b):
    return a ** b
