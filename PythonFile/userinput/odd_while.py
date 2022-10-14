msg = "Enter the number::"
i = 0
number = int(input(msg))
while i <= number:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

