class Circle:
    radius = 0
    area = 0.0

    def __init__(self):
        print("Inside constructor")
        self.radius = 0

    def get_data(self):
        self.radius = int(input("enter the radius of the circle"))

    def calc_area(self):
        self.area = 2 * 3.14 * self.radius
        print("Calculating area of the circle")

    def display(self):
        print(f"The radius is {self.radius} and area is {self.area}")


b = Circle()
b.get_data()
b.calc_area()
b.display()

a = Circle()
a.get_data()
a.calc_area()
a.display()


