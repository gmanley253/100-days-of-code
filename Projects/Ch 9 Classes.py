class Restaurant:
    """This is ex. 9 from the book Python Crash Course"""
    def __init__(self, name, cuisine, number_served):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
        
    def describe_restaurant(self):
        """Function to return the restaurant description."""
        return ('The name of the restaurant is: ' + self.name)
        return ('The cuisine type is: ' + self.cuisine)
        
    def open_restaurant(self):
        """Function to determine if the restaurant is open"""
        return ("Restaurant is open")
        
    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, customers):
        self.number_served += customers

class User:
    """Class to define a set of users. Ex 9.3 from the book Python Crash Course"""
    def __init__(self, fname, lname, login_attempts):
        self.fname = fname
        self.lname = lname
        self.login_attempts = 0
        
    def describe_user(self):
        """Function to return a users fname and lname"""
        return ("User:" + self.fname + " " + self.lname)
        
    def greet_user(self):
        """Function to greet a user"""
        return ("Welcome " + self.fname + " " + self.lname)
        
    def increment_login_attempts(self, attempts):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        self.name = name
        self.cuisine = cuisine
        self.flavors = flavors
        
    def flavors(self, flavors):
        return flavors
    
class Admin(User):
    def __init__(self, fname, lname, privileges):
        self.fname = fname
        self.lname = lname
        self.privileges = privileges
        
    def show_privilges(self, privileges):
        return ("can add post", "can delete post", "can ban user")
        
#Restaurant class check on learning     
french_restaurant = Restaurant("Le Pigeon", "French", 0)
fastfood_restaurant = Restaurant("McDonalds", "Fast Food", 0)
italian_restaurant = Restaurant("Olive Garden", "Italian", 0)

print(french_restaurant.describe_restaurant())

french_restaurant.set_number_served(1000)

french_restaurant.increment_number_served(25)

print(french_restaurant.number_served)

#User class check on 
user1 = User("Bob", "Nordstrom", 0)
user2 = User("Julie", "Macy", 0)
user3 = User("Sears", "Roebuck", 0)

print(User.describe_user(user1))
print(User.greet_user(user1))

user1.increment_login_attempts(1)
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)

#Ice Cream stand check on learning
frozen_treats = IceCreamStand("frozen treats", "ice cream", ["Vanilla", "Chocolate"])

print(frozen_treats.name + ' ' + ' '.join(frozen_treats.flavors))