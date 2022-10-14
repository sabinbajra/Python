#print 1 to 9
for i in range(1,10):
    print(i)

#print from 0 to 9
for i in range(10):
    print(i)

#using range to create a list
numbers = list(range(1,11))
for i in numbers:
    print(i)

print("A program to print first 10 even numbers")
even = list(range(2,21,2))
for i in even:
    print(i)

print(even)

print("Program to find out the square of the first 10 numbers")
squares = []
for i in range (1,11):
    #square = i ** 2
    squares.append(i**2)

print(squares)

print("The minimum value of the list is :: ")
print(min(squares))
print("The maximum value of the list is :: ")
print(max(squares))
print("The sum value of the list is :: ")
print(sum(squares))
print("The length value of the list is :: ")
print(len(squares))

#List  comprehension
squares = [i**2 for i in range(1,5)]
print(squares)