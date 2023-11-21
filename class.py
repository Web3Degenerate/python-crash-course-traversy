# Created at (1:15:50): https://youtu.be/JJmcL1N2KQs?si=xXEOEg2OfZ-Wo5R7&t=4550

# A class is like a blueprint for creating objects.  
# An object has properties and methods (functions) associated with it. 
# Almost everything in Python is an object. Str is an object, we can call methods on it. 

# Create a class
class User: 
    # Constructor (self is this)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Create a class method. Use self keyword to use properties in the class constructor
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    #Add another year to age
    def has_birthday(self):
        self.age += 1

# init user object
brad = User('Brad Smith', 'brad@gmail.com', 37)


# print(brad)
print(type(brad))

# Access properties
print(brad.name)

# Increment age using has_birthday()
brad.has_birthday()
# Call the class function greeting()
print(brad.greeting())