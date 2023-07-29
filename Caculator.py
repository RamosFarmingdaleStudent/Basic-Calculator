import math

print("Choose two numbers: ")

num1 = int(input())
num2 = int(input())

operation = int(input("Choose one of the four operations:\n 1.add\n 2.subtract\n 3.divide\n 4.multiple\n"))

if operation == 1:
    print(num1 + num2)
elif operation == 2:
    print(num1 - num2)
elif operation == 3:
    print(num1 / num2)
else:
    print(num1 * num2)