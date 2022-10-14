class Car:
    def show_carinfo(self):
        print("Inside the car::")


class ElectricCar(Car):
    def show_electriccarinfo(self):
        super().show_carinfo()
        print("Inside Electric car::")


class Analog(Car):
    def show_analog(self):
        print("Inside Analog")


class HybridCar(Analog, ElectricCar):
    def show_hybridinfo(self):
        print("Inside HYBRID ZOOM::")
        super().show_electriccarinfo()


emx = HybridCar()
# emx.show_carinfo()
emx.show_analog()
emx.show_electriccarinfo()
emx.show_hybridinfo()
