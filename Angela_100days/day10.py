# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

continue_calculation = True
while continue_calculation:
    num1 = int(input("What's the first number? "))
    operation_symbol = input("Pick an operation (+, -, *, /): ")
    num2 = int(input("What's the second number? "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    user_wish = input("Do you want to cantinue in a calculation (y/n)? ")
    if user_wish == "n":
        continue_calculation = False
