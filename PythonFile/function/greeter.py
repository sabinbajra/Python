def greet_user():
    print("Hello welcome to the python programming")


def maximum(a=0, b=0):
    if a <= b:
        print(f"B {b} is maximum")
    else:
        print(f"A {a} is maximum")


greet_user()
maximum(15, 11)
maximum(b=12,a=10)
