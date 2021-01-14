def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation")
print("1:Add")
print("2:Subtract")
print("3:Multiply")
print("4:Divide")
choice = input("Make a choice of operation(1, 2, 3, 4): ")


if choice == '1':
    print("The sum of", num1, "and", num2, "is", add(num1, num2))
elif choice == '2':
    print("The difference between", num1, "and", num2, "is", subtract(num1, num2))
elif choice == '3':
    print("The multiplication of", num1, "and", num2, "is", multiply(num1, num2))
elif choice == '4':
    print("The division of", num1, "and", num2, "is", divide(num1, num2))
else:
    print("Invalid choice")
