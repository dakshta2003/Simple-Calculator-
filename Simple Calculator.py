def calculator():
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /,%): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/' and num2 != 0:
        print("Result:", num1 / num2)
    elif op == '%':
        print("Result:",num1%num2)
    else:
        print("Invalid input!")

calculator()
