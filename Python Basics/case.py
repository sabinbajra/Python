#Function definition starts
import numpy as np
def check_X(x):
    y = 1
    if x < 0 or x > 4:
        y = 0
    return y

print("Calculator")
print("++++++++++++++")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

x = 0

x = int(input(print("Enter your choice::")))
if x == 1:
    print("You Press Add")
elif x == 2:
    print("You Press Subtract")
elif x == 3:
    print("You Press Multiply")
elif x == 4:
    print("You Press Divide")
else:
    print("Wrong Entry")



'''

x = int(input(print("Enter your choice::")))
val = check_X(x)
print(type(val))

match val:
    case 1:
        print("Adding")
    case 2:
        print("Subtracting")
    case 3:
        print("Multiplication")
    case 4:
        print("Division")
'''
'''
match x:
    case 1:
        print("")
    case 2:
        print("")
    case _:
        print("")

'''


