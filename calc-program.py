Operater = input("Enter the operater (+ - * / **)")

num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

# print(num1 + num2)
# print(round(result,3))
if Operater == "+":
  result = num1 +num2
  print(round(result,3))
elif Operater =="-":
 result = num1-num2
 print(round(result,3))
elif Operater =="*":
  result = num1 *num2
  print(round(result,3))
elif Operater =="/":
  result = num1 /num2
  print(round(result,3))
elif Operater =="**":
  result = num1 /num2
  print(round(result,3))
else:
  print(f"{Operater} is not a valid  operator")