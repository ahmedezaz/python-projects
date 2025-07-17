#Simple calculator using two input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator: ")
total = 0

if op == "+":
    total = a+b
    print("total is:", total)
elif op == "-":
    total = a -+ b
    print("total is:", total)
elif op == "*":
    total = a * b
    print("total is:", total)
elif op == "/":
    total = a / b
    print("total is:", total)
else:
    print("Wrong operator")
