def to_printf():
    print("Hello world from to_printf() function")

def check_Greater(**x):
    if x[0] <= x[1]:
        print(x[1] + " is greater")
    else:
        print(x[0] + " is greater")


to_printf()
check_Greater(4,7)

