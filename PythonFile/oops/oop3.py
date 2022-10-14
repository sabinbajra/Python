pi = 3.145


class Circle:
    def __init__(self, radius=0, area=0.0):
        self.radius = radius
        self.area = area

    def set_Data(self):
        self.radius = int(input("Enter the radius of a circle::"))

    def calc_Area(self):
        global pi
        print("Calculating the area of the circle::")
        self.area = pi * (self.radius ** 2)

    def display(self):
        print(f"Radius of cirle:: {self.radius}\nArea:: {self.area}")


c = Circle()
c.set_Data()
c.calc_Area()
c.display()