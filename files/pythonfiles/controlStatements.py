# This is control statement program
"""
choice = 0
num1 = num2 = result = 0
print("Welcome to calculator")

print("Calculator Menu")
print("\t1. Add \n\t2. Subtract\n\t3.Multiply\n\t4.Division\n")

print("Enter your choice")
choice = int(input())

if choice > 0:
    print("Enter number 1:")
    num1 = int(input())
    print("Enter number 2:")
    num2 = int(input())
    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        result = num1 / num2
    else:
        print("!!!!Wrong Choice!!!!")
    print("The result is ", result)
else:
    print("Please Enter a valid choice")
"""

"""
x = 0
for x in range(10):
    print(x*2)
"""

x = 0
print("Enter the number of terms::")
x = int(input())

for i in range (0,x):
    print(i*2)
    i = i + 1

