class Restaurant():
    #A class representing a restaurant

    def __init__(self, name, cuisine_type):
        #Initialize the restaurant
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        #Display a summary of the restaurant
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        #Display a message that the restaurant is open
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        #Allow user to set the number of customers that have been served
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        #Allow user to increment the number of customers served.
        self.number_served += additional_served


restaurant = Restaurant('Joels FastFood', 'fries')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 115
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1375)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(300)
print("Number served: " + str(restaurant.number_served))
