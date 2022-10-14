"""

def add_numbers(x, y):
    return x + y


def greatest(x,y):
    if x > y:
        return x
    else:
        return y


def to_printf():
    print("Hello world from to_printf() function")


def print_name(fname):
    print('My name is ' + fname)


def print_fullname(fname, lname):
    print('My name is ' + fname + ' ' + lname)


to_printf()
print_name('sabin')
print_fullname('sangamita', 'shakya')

sum1 = add_numbers(2, 13)
print(sum1)
print('The greatest number is %d', greatest(33, 88))

"""

#program to display the use of the function and if else


def add(x, y):
    return x+y


def minimum_value(a,b):
    if a<b:
        return a
    else:
        return b


def draw_triangle(x):
    j = 0
    i = 0
    for i in range(x+1):
        j = 0
        for j in range(i):
            print('@', end='', flush=True)
            j = j + 1
            if (j == i): print("")
    j = 0
    i = 0
    for i in range(10):
        j = 0
        for j in range(i):
            print('@', end='', flush=True)
            j = j + 1
            if (j == i): print("")
    else:
        print("End of the draw")


a = 0
b = 0
print("Menu \n ++++++++++++++ \n 1. add \n 2. small one \n 3. draw")
print("Enter your choice::")
x = int(input())

if x == 1 or x == 2:
    print("Enter 1st no::")
    a = int(input())
    print("Enter 1st no::")
    a = int(input())
    if x == 1:
        sum = add(a, b)
        print("The added value is ", sum)
    else:
        min = minimum_value(a, b)
        print("The minimum value is ", min)
elif x == 3:
    size = int(input(print("Enter size of flag::")))
    draw_triangle(size)
else:
    print("Wrong entry")

