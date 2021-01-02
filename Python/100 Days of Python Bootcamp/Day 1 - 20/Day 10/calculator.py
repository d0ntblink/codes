import art, os, time

def clear() :
    os.system('cls||clear')

def add(n1, n2):
    '''adds the two numbers together''' 
    return  (n1 + n2)

def subtract(n1, n2):
    '''first number subtract the second number'''
    return (n1 - n2)

def multiply(n1, n2):
    '''multiplies the two numbers'''
    return (n1 * n2)

def devide(n1, n2):
    '''first number devided by the second number'''
    return (n1 / n2)

def exponent(n1, n2):
    '''first number to the power of second number'''
    return (n1 ** n2)

def modulus(n1, n2):
    '''first number modulus the second number'''
    return (n1 % n2)

oprations = {
    "-": subtract,
    "+": add,
    "*": multiply,
    "^": exponent,
    "/": devide,
    "mod": modulus
}

isnew = "n"

clear()
print(art.logo)

while True:
    if isnew == 'q':
        print("Goodbye!")
        clear()
        break
    elif isnew == "y":
        num1 = result
    elif isnew == "n":
        clear()
        num1 = float(input("What is your first number ? "))

    for op,ex in oprations.items() :
        print(op , ex.__doc__)

    opration = input("\nChoose one of the available oprations : ")
    num2 = float(input("What is your second number ? "))

    function = oprations[opration]
    result = function(num1, num2)
    print(f"{num1} {opration} {num2} = {result}")

    isnew = input("Do you want to continue with your last result or quit ? (Y/N/Q) ").lower()