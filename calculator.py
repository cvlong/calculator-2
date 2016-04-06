"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    user_equation = raw_input("What equation would you like to perform? \nPlease enter in prefix notation. For example: + 4 5\n")
    token = user_equation.split(" ")
    if token[0] == "q":
        break
    elif token[0] == "+":
        print add(int(token[1]), int(token[2]))
