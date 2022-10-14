class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} and it serve {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is now opening")


a = Restaurant("The Lebanese Sajeria", "Lebanese")
print(f"Name:: {a.restaurant_name}\nCuisine:: {a.cuisine_type}")
a.describe_restaurant()
a.open_restaurant()

b= Restaurant("Maismas", "Mexican")
b.open_restaurant()
b.describe_restaurant()