"""
msg = "Enter the number till you want to print::"
i = 1
number = int(input(msg))
while i <= number:
    print(i)
    i += 1
"""

msg = "Do you want to quit"
display = "Menu:\n1.Add\n2.Sub\n3.Quit\nEnter your choice::"
choice = 0

while choice != 3:
    choice = int(input(display))
    if choice == 1:
        print("Adding")
    elif choice == 2:
        print("Subtracting")
    else:
        print("Please enter correctly")


print("Thank you!!!")
