# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))

    print("Chose your operation: ")
    for operation in operations:
        print(f"{operation}")
    operation_symbol = input("Pick an operation from the list above: ")

    num2 = float(input("What's the second number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    should_continue = True

    while should_continue:
        user_continue = input("Do you want to do another operation? 'y' or 'n': ")
        if user_continue == "n":
            should_continue = False
            calculator()
        else:
            operation_symbol = input("Pick another operation: ")
            num3 = float(input("What's the next number?: "))
            new_answer = operations[operation_symbol](answer, num3)
            print(f"{answer} {operation_symbol} {num3} = {new_answer}")
            answer = new_answer

calculator()
