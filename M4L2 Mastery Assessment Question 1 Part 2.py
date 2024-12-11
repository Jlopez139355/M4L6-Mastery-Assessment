class Restaurant:
    #A class representing a restaurant

    def __init__(self, name, cuisine_type):
       #Initialize the restaurant
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        #Display a summary of the restaurant
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        #Display a message that the restaurant is open
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

Joels_FastFood = Restaurant('Joels FastFood', 'fries')
Joels_FastFood.describe_restaurant()

Johnnys_Shop = Restaurant("Johnnys Shop", 'bacon')
Johnnys_Shop.describe_restaurant()

Nates_Club = Restaurant('Nates Club', 'Ramen')
Nates_Club.describe_restaurant()
