class Room:
    def __init__(self, length, breadth,area=0):
        self.length = length
        self.breadth = breadth
        self.area = area

    def getValue(self):
        self.length = int(input("Enter the Length of the room::"))
        self.breadth = int(input("Enter the Breadht of the room::"))

    def display(self):
        print(f"Length :: {self.length} \nBreadth :: {self.breadth} \nArea :: {self.area}")

    def calculateArea(self):
        self.area = self.length * self.breadth


room1 = Room(2,3)
room1.getValue()
room1.calculateArea()
room1.display()



