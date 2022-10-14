class Dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} dog is sitting")

    def bark(self):
        print(f"{self.name} dog is barking for {self.age} year")


kisi = Dog("Kisi",1)
kisi.sit()
kisi.bark()