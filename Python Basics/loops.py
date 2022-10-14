'''
print("This gives the examples of the loop")

for i in range(10):
    print(i)
    i = i + 1
n = int(input(print("Enter the no of terms less than 10")))

#n terms even number
terms = 1
for i in range(n):
    print(2*terms)
    i = i + 1
    terms = terms + 1

print("+++++++++++++++++++++++++")
#n terms even number
i=1
x = 1
for i in range(10):
    print(x)
    x = x + 2
    i = i + 1
    if i == n:
        break
else:
    print("This is else inside the for loop")
'''
j = 0
i = 0
for i in range(7):
    j = 0
    for j in range(i):
        print('@', end='', flush=True)
        j = j + 1
        if(j == i): print("")
j = 0
i = 0
for i in range(10):
    j = 0
    for j in range(i):
        print('@', end='', flush=True)
        j = j + 1
        if(j == i): print("")
else:
    print("End of the draw")