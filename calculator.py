"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

greeting ="""What equation would you like to perform?
Please enter prefix notation. For example: + 4 5
If you would like to quit, Enter 'q'
"""
print greeting

while True:    
    user_equation = raw_input(">>>")
    token = user_equation.lstrip()
    token = token.split(" ")

    if token[0] == "q":
        print "Thanks for playing! See you next time."
        break
    elif len(token) == 2:
        num1 = float(token[1])
        
        if token[0] == "square":
            print square(num1)
        elif token[0] == "cube":
            print cube(num1)
        else:
            print "Try Again."
        
    elif len(token) == 3:
        num1 = float(token[1])
        num2 = float(token[2])
        
        if token[0] == "+":
            print add(num1, num2)
        elif token[0] == "-":
            print subtract(num1, num2)
        elif token[0] == "*":
            print multiply(num1, num2)
        elif token[0] == "/":
            print divide(num1, num2)
        elif token[0] == "pow":
            print power(num1, num2)
        elif token[0] == "mod":
            print mod(num1, num2)
        else:
            print "Try Again."
    else:
        print "Try Again."
        continue

        
