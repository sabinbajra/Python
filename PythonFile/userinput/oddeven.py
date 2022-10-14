number = 0

msg = "Enter number to check if the number is even or odd"
number = input(msg)
number = int(number)

if number % 2 == 1:
    print(f"The enter number {number} is odd")
else:
    print(f"The enter number {number} is even")
