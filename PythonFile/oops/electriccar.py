class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def getvalue(self):
        self.make = input("Enter make of the car::")
        self.model = input("Enter model of the car::")
        self.year = int(input("Enter year of the car::"))
        self.odometer = int(input("Enter odometer reading the car::"))

    def return_name(self):
        print(f"Car Name:: {self.make}\nModel:: {self.model}\nYear made:: {self.year}")
        return f"{self.make} {self.model}"

    def read_odometer(self):
        print("Enter the odometer reading::")
        self.odometer = int(input())

    def update_odometer(self):
        mileage = int(input("Enter the new odometer reading::"))
        if mileage < self.odometer:
            print("You can not roll back your odometer.")
        else:
            self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles

    def display(self):
        print(f"Car Name:: {self.make}\nModel:: {self.model}\nYear made:: {self.year}")

    def fill_fuel(self):
        print("Car is filling the fuel::")


class Battery:
    def __init__(self,size):
        self.battery_size = size

    def describe(self):
        print(f"The size of battery is :: {self.battery_size}")

    def update_battery(self):
        self.battery_size += 10
        print()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(15)

    def fill_fuel(self):
        # Car.fill_fuel(self)
        print("Electric car do not need fuel")


a = ElectricCar("BMW", "E series", 1990)
a.display()
a.getvalue()
a.display()
a.battery.describe()
a.fill_fuel()
a.battery.update_battery()
a.battery.describe()
