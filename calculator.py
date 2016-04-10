"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

greeting ="""Enter your equation using prefix notation with spaces as separation between inputs. For example: + 4 5
Type 'q' to quit the program.
Use + - * / as usual, and type square, cube, pow, or mod for other operations.
"""

print greeting

while True:    
    user_equation = raw_input("> ")
    strip = user_equation.lstrip()
    token = strip.replace("  ", " ")
    token = token.split(" ")
    
    operation = token[0]
    # If user wants to input multiple arguments:
    # tokens = token[1:]

    if operation == "q":
        print "Thanks for playing! See you next time."
        break
    
    elif len(token) < 2:
        print "Not enough input values."

    elif len(token) < 3:
        try:
            num1 = float(token[1])
            num2 = 0
        except ValueError:
            print "You must enter a number. Try again."

    else:
        try:
            num1 = float(token[1])
            num2 = float(token[2])
        except ValueError:
            print "You must enter a number. Try again."
    
    # if not num1.isdigit() or not num2.isdigit():
    #     print "Those aren't numbers. Try again."
    #     continue
    
    if operation == "+":
        print add(num1, num2)
    elif operation == "-":
        print subtract(num1, num2)
    elif operation == "*":
        print multiply(num1, num2)
    elif operation == "/":
        print divide(num1, num2)
    elif operation == "square":
        print square(num1)
    elif operation == "cube":
        print cube(num1)
    elif operation == "pow":
        print power(num1, num2)
    elif operation == "mod":
        print mod(num1, num2)
    else:
        print "Try again."
        continue


