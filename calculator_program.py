# basic calculator program
first_operand = int(input("Enter the first number:"))
second_operand = int(input("Enter the second number:"))
operation= input("Enter the operation to be performed:")
if operation == "+":
    result = first_operand + second_operand
elif operation == "-":
    result = first_operand - second_operand
elif operation == "/":
    result = first_operand / second_operand
elif operation == "*":
    result = first_operand * second_operand
else :
    print("Invalid operator! please enter a valid operation")
print(result)