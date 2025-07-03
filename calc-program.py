Operater = input("Enter the operator (+ - * / **): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if Operater == "+":
    result = num1 + num2
    print(round(result, 3))
elif Operater == "-":
    result = num1 - num2
    print(round(result, 3))
elif Operater == "*":
    result = num1 * num2
    print(round(result, 3))
elif Operater == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = num1 / num2
        print(round(result, 3))
elif Operater == "**":
    result = num1 ** num2
    print(round(result, 3))
else:
    print(f"{Operater} is not a valid operator.")
