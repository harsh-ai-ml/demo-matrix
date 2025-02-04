#calculate basic function applications

import math

def test():
    print("Enter the first number")
    x = float(input())
    print("Enter the second number")
    y = float(input())
    print("Enter an operation (+, -, *, /)")
    operation = input()
    if operation == '+':
        print(x + y)
    elif operation == '-':
        print(x - y)
    elif operation == '*':
        print(x * y)
    elif operation == '/':
        print(x / y)
    else:
        print("Invalid operation")

test()