from restaurant import Restaurant


class IceCreamStand(Restaurant):
    flavours = []

    def __init__(self, restaurant_name, cuisine_type, flavours=[]):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        for i in flavours:
            self.flavours.append(i)

    def display_flavours(self):
        for i in self.flavours:
            print(i)


flavours = ["vanilla", "strawberry", "chocolate"]
a = IceCreamStand("The ICECREAM STAND", "ice-cream", flavours)
a.describe_restaurant()
a.open_restaurant()
a.display_flavours()
