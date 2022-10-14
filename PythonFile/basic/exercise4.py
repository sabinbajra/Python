# use a loop for print numbers from 1 to 20
for i in range(1, 21):
    print(i)

# list of numbers from 1 to 999 and print it
numbers = [i for i in range(1, 1000)]
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# odd numbers from 1 to 20
odd_numbers = list(range(1, 20, 2))
for i in odd_numbers:
    print(i)

# multiple of 2
numbers = [i * 2 for i in range(1, 11)]
j = 1
for i in numbers:
    # print(i)
    print(f"2 X {j} = {i}")
    j += 1

#cubes
j=1
cubes = [i**3 for i in range(1,11)]
for i in cubes:
    print(f"The cube of {j} is {i}")
    j += 1

#squares
squares = []
for i in range(1,11):
    squares.append(i**2)

print(squares)
