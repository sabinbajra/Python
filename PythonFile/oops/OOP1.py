class Dog:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def bark(self):
        print("The dog is barking")

    def roll(self):
        return "I am rolling ::"

    def intro(self):
        return [self.name, self.type]

    def getInfo(self):
        self.name = input("Enter the name of the dog::")
        self.type = input("Enter the type of the dog::")

    def updateName(self):
        self.name = input("Enter the new name of the dog::")


# kissing is object of class Dog
a = Dog("kissi", "cockerspaniel")
a.bark()
a.getInfo()
intro = a.intro()

for i in intro:
    print(i)

print(a.roll())
a.updateName()
