def add(*a):
    sum = 0
    for i in a:
        sum = sum + i

    return sum

a = [1,2,3]
print(add(*a))
