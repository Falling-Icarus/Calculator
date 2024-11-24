from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
calculate = False
print(logo)
result = 0
while calculate == False:
    if result == 0:
        n1 = int(input("what is the first number?: "))
    question_operation = input(" +\n -\n *\n /\n Pick an operation: ")
    n2 = int(input("What is the next number?: "))
    operation = float(operations[question_operation](n1,n2))
    print(f"{n1} {question_operation} {n2} = {operation}")
    result = operation
    calculation_again = input(f"Type 'y' to continue calculating with {result}, or type 'n'to start a new calculation: ")
    if calculation_again == "y":
        n1 = result
    elif calculation_again == "n":
        print("\n" *100)
        print(logo)
        result = 0

