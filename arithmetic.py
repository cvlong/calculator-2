def add(num1, num2):
    """return the sum of two input integers"""

    return num1 + num2


def subtract(num1, num2):
    """return the second input subtracted from the first input"""

    return num1 - num2


def multiply(num1, num2):
    """multiply two inputs together"""

    return num1 * num2


def divide(num1, num2):
    """divide the first input by the second input; return a float"""
    # Need to turn at least argument to float for division to
    # not be integer division
    
    return float(num1) / float(num2) 


def square(num1):
    """return the square of the input"""
    
    return num1 ** 2


def cube(num1):
    """return the cube of the input"""
    
    return num1 ** 3


def power(num1, num2):
    """raise the first input by the second input"""

    return num1 ** num2


def mod(num1, num2):
    """return the remainder when the first input is divided by the second input""" 
    
    return num1 % num2


# Look into *args
# def add(*arg):
