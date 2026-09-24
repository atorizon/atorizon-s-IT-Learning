# A very simple calculator that only calculates 2 numbers.
# This practice mainly exercises my fundamentals in functions and a bit of match-case statements.

def numbers():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    return num1, num2

def add():
    num1,num2=numbers()
    sum=num1+num2
    print(f'\nSum: {sum}')

def sub():
    num1,num2=numbers()
    diff=num1-num2
    print(f'\nDifference: {diff}')

def multiply():
    num1,num2=numbers()
    prod=num1*num2
    print(f'\nProduct: {prod}')

def divide():
    num1,num2=numbers()
    quo=num1/num2
    print(f'\nQuotient: {quo}')

def function_match():
    operation=input("Enter an arithmetic operation (+, -, *, /): ")
    match operation:
        case "+":
            add()
        case "-":
            sub()
        case "*":
            multiply()
        case "/":
            divide()
        case _:
            print("Invalid Operation.")

while True:
    function_match()
    operation_again=input("Would you like to do another calculation? (y/n): ")

    if operation_again=="n":
        print("Exiting calculator...")
        break