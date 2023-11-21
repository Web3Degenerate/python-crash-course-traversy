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

# Extend class (1:22:07): https://youtu.be/JJmcL1N2KQs?si=VG3PIqN-08-e4_n2&t=4927
# Create class Customer, which extends User class above.
class Customer(User):
        # Constructor (self is this)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

# You can access parent methods since Customer inherits from User. 
# Or you can overwrite that greeting as shown here: (adding balance to the User greeting template)
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Initialize a customer object
janet = Customer('Janet Smith', 'janet@gmail.com', '42')

# Set a balance for customer object
janet.set_balance(500)

print(janet.greeting())