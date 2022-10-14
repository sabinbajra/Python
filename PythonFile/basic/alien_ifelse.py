color = ""
point = 0
alien_colors = ['red', 'green', 'yellow', 'blue', 'white']

print("Enter the color of alien you shoot::")
color = input()

if color in alien_colors:
    if color.lower() == 'red':
        point = 5
    elif color.lower() == 'green':
        point = 10
    elif color.lower() == 'yellow':
        point = 15
    elif color.lower() == 'blue':
        point = 20
    elif color.lower() == 'white':
        point = 30
    print(f"You earned {point} by killing {color} alien.")
else:
    print("Please enter correctly")

