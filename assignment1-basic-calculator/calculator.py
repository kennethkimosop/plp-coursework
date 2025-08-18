# Basic Calculator Program

# Step 1 inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Step 2 operations
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed .")

else:
    print("Invalid operation! Please enter +, -, *, or /")



# values = []
# for i in values:


#   "+" = num1 + num2
#   "/" = num1/num2
#   "-" = num1 - num2
#   "*" = num1 * num2

#   if "+" == num1 + num2:
#     print("The sum is", num1 + num2)
#     elif "/" == num1/num2:
#       print("")