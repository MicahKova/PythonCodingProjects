def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a/b

def operations(a,b):
    if operations == "+":
        return add(a,b)
    elif operations == "-":
        return subtract(a,b)
    elif operations == "*":
        return multiply(a,b)
    elif operations == "/":
        return divide(a,b)

operations = {"+" : add,"-" : subtract, "*" : multiply, "/" : divide}


print("Welcome to calculator.")
a = float(input("What is your first number?\n"))
operation = input("Enter:\n + for add\n - for subtract \n * for multiply\n / for divide\n")
b = float(input("What is your second number?\n"))
result = operations[operation](a,b)
print(f"{a} {operation} {b} = {result}")


repeat = input("Type 'y' to continue calculating with the result, or type 'n' to start a new calculation:\n").lower()
while repeat == "y":
    a = result
    operation = input("Enter:\n + for add\n - for subtract \n * for multiply\n / for divide\n")
    b = float(input("What is your second number?\n"))
    result = operations[operation](a, b)
    print(f"{a} {operation} {b} {result}")
    repeat = input("Type 'y' to continue calculating with the result, or type 'n' to start a new calculation:\n ").lower()
    if repeat == "n":
        print("Welcome to the calculator!")
        a = float(input("What is the first number?\n "))
        operation = input("Enter:" "\n+ for add\n- for subtract\n* for multiply\n/ for divide\n")
        b = float(input("What is the second number?\n "))
        result = operations[operation](a, b)
        print(f"{a} {operation} {b} = {result}")

