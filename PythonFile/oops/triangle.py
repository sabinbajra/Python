class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = 0.5 * self.base * self.height

    def getdata(self):
        self.base = float(input("Enter the base of the triangle::"))
        self.height = float(input("Enter the height of the triangle::"))

    def calculatearea(self):
        print("Calculating area of the triangle")
        self.area = 0.5 * self.base * self.height
        print("Area successfully calculated")

    def display(self):
        print(f"Base:: {self.base} Height:: {self.height} and area:: {self.area}")

    def update(self):
        self.base = float(input("Enter new value for the base::"))
        self.height = float(input("Enter new value for the height::"))


a = Triangle(0, 0)
a.getdata()
a.calculatearea()
a.display()
a.update()
a.calculatearea()
a.display()
