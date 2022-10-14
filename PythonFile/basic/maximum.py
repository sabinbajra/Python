max_no, num1, num2 = 0, 0, 0
num1 = int(input("Enter the 1 number::"))
num2 = int(input("Enter the 2 number::"))

if num1 > num2:
    max_no = num1
else:
    max_no = num2

print(f"The maximum number among {num1} and {num2} is {max_no}")