class BasicClass:
    theVariable = 1


class ExampleClass:
    age = 24
    name = "Sabin"
    location = "Amsterdam"


class BirthdayBoy:
    name = ""
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        print("Happy Birhtday")
        self.age += 1

    def display(self):
        print(f"Name :: {self.name}")
        print(f"Age :: {self.age}")


# ============================
a = ExampleClass()
print(f"{a.name}  {a.age}  {a.location}")

# ============================
b = BirthdayBoy("Sabin Bajracharya", 36)
b.birthday()
b.display()

