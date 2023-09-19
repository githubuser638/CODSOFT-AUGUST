# Calculator
# Calc.py
import sys
while(True):
    print('''\t     ---------------------------------
             Calculator Operations:-
             ---------------------------------
             1. Addition
             2. Subtraction
             3. Multiplication
             4. Division
             5. Floor Division
             6. Exit.
             ---------------------------------''')
    inp = int(input("Enter you choice (integer input only) :- "))
    match(inp):
        case 1:
            a = int(input("Enter first number:- "))
            b = int(input("Enter second number:- "))
            print("Addition ({},{}) is {}\n".format(a,b,a+b))
        case 2:
            a = int(input("Enter first number:- "))
            b = int(input("Enter second number:- "))
            print("Subtraction ({},{}) is {}\n".format(a,b,a-b))
        case 3:
            a = int(input("Enter first number:- "))
            b = int(input("Enter second number:- "))
            print("Multiplication ({},{}) is {}\n".format(a,b,a*b))
        case 4:
            a = int(input("Enter first number:- "))
            b = int(input("Enter second number:- "))
            print("Division ({},{}) is {}\n".format(a,b,a/b))
        case 5:
            a = int(input("Enter first number:- "))
            b = int(input("Enter second number:- "))
            print("Floor Division ({},{}) is {}\n".format(a,b,a//b))
        case 6:
            print("Thank You for using this program.\n")
            sys.exit()
        case _:
            print("Your entered choice is invalid, please try again\n")
            
