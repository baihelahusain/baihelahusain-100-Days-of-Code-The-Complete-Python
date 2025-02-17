import art
print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2
calc = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }


def calculator():
    n = float(input('Enter any no:\n'))
    while True:
        for i in calc:
            print(i)
        operation = input('Enter the symbol you want to perform the operation + - * /:\n')
        m = float(input('Enter the 2nd number\n'))
        ans = (calc[operation](n1=n,n2=m))
        user = input(f"Do you want to contiue the calculation with {ans}:")
        if user == 'yes':
            n = ans
        else:
            print(100*'\n')
            calculator()
            break
calculator()

