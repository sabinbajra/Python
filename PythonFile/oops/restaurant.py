class Restaurant:

    def __init__(self, restaurant_name="", cuisine_type=""):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        print("Restaurant class object instantiated.")

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} and it serve {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is now opening")




