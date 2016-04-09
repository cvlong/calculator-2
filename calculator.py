"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

greeting ="""What equation would you like to perform?
(Please use prefix notation. For example: + 4 5
To quit the program, enter 'q'
"""
print greeting

while True:    
    user_equation = raw_input(">")
    token = user_equation.lstrip()
    token = token.replace("  ", " ")
    token = token.split(" ")
    
    token[0] = operation
    # If user wants to input multiple arguments:
    # tokens = token[1:]

    if operation == "q":
        print "Thanks for playing! See you next time."
        break
    elif len(token) == 2:
        num1 = float(token[1])
        
        if operation == "square":
            print square(num1)
        elif operation == "cube":
            print cube(num1)
        else:
            print "Try again."
        
    elif len(token) == 3:
        num1 = float(token[1])
        num2 = float(token[2])
        
        if operation == "+":
            print add(num1, num2)
        elif operation == "-":
            print subtract(num1, num2)
        elif operation == "*":
            print multiply(num1, num2)
        elif operation == "/":
            print divide(num1, num2)
        elif operation == "pow":
            print power(num1, num2)
        elif operation == "mod":
            print mod(num1, num2)
        else:
            print "Try again."
    else:
        print "Try again."
        continue


