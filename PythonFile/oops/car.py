class Car:
    window = 0
    door = 0
    enginetype = ""

    def __init__(self,window,door,enginetype):
        self.window = window
        self.door = door
        self.enginetype = enginetype

    def self_driving(self):
        return "This is a {} car".format(self.enginetype)

    def changeValue(self):
        self.window = int(input("Enter the no of window::"))
        self.door = int(input("Enter the no of doors::"))
        self.enginetype = input("Enter the type of the engine::")

    def showValeu(self):
        print(f"Engine type:: {self.enginetype}\nWindow:: {self.window}\nDoor:: {self.door}")


a = Car(4,5,"Petrol")
a.changeValue()
a.showValeu()
print(a.self_driving())


