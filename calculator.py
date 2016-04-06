"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    greeting ="""What equation would you like to perform?
Please enter prefix notation. For example: + 4 5
If you would like to quit, Enter 'q'"""

    user_equation = raw_input(greeting)
    token = user_equation.lstrip()
    token = token.split(" ")
    
    if token[0] == "q":
        print "Thanks for playing! See you next time."
        break
    elif token[0] == "+":
        print add(int(token[1]), int(token[2]))
    elif token[0] == "-":
        print subtract(int(token[1]), int(token[2]))
    elif token[0] == "*":
        print multiply(int(token[1]), int(token[2]))
    elif token[0] == "/":
        print divide(int(token[1]), int(token[2]))
    elif token[0] == "square":
        print square(int(token[1]))
    elif token[0] == "cube":
        print cube(int(token[1]))
    elif token[0] == "pow":
        print power(int(token[1]), int(token[2]))
    elif token[0] == "mod":
        print mod(int(token[1]), int(token[2]))
    else:
        print "Try again!"

        
