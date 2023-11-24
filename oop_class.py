
# https://teamtreehouse.com/library/objectoriented-python-2/instant-objects/method-interactivity



# Call class method within the class with the 'self' keyword

# PART 1
# Make a new method named feedback. It should take self and an argument named grade. 
# Methods take arguments just like functions do.
# Inside the feedback method, if grade is above 50, return the result of the praise method. If it's 50 or below, return the reassurance method's result.

# PART 2
# I'd like to be able to set the name attribute at the same time that I create an instance. Add the code for doing that?
# Override the __init__ method by adding your own __init__ method to the Student class. 
# Add self and name as arguments to the __init__ method. 
# Inside of __init__, set self.name to the argument name.

# PART 3 - ADD **kwargs to the init
# Sometimes I have other attributes I need to store on a Student instance. 
# Add **kwargs as an argument to the __init__ method. 
# Then use setattr inside the __init__ method to add attributes for any other key/value pairs I want to send to the instance when I create it.

class Student:
    # name = "Your Name"
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            # setattr lets us set values for key-value pairs we don't know exist yet  
            setattr(self, key, value)

    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()



# RACECAR CLASS
# First, create a class named RaceCar. 
# # In the __init__ for the class, take arguments for color and fuel_remaining. 
# # Set these as attributes on the instance.
# Also, add the **kwargs argument and use setattr to take any other keyword arguments that come in.

# Part 2: 
#Now let's handle the racecar running laps. Add a laps attribute to the RaceCar class and set it to 0. 
# Add a method named run_lap. It'll take a length argument. 
# It should reduce the fuel_remaining attribute by the length argument multiplied by 0.125 (length * 0.125). 
# Also, increment the laps attribute by 1 each time the run_lap method is called.

# Part 3: 
# In Python, attributes defined on the class, but not an instance, are universal. 
# So if you change the value of the RaceCar's laps attribute, any instance of RaceCar that doesn't have laps set explicitly will have its value changed, too!
# For example, right now, if we made a RaceCar instance named red_car, then set RaceCar.laps = 10, red_car.laps would then be set to 10 too!
# To prevent this, be sure to set the laps attribute inside the __init__ method (it doesn't have to be a keyword argument, though). If you already did it, you're good to go!

class RaceCar:
    def __init__(self, color, fuel_remaining, laps=0, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining = self.fuel_remaining - (length * 0.125)
        self.laps += 1


## INHERITANCE 
# Create a new class, SortedInventory that should be a subclass of Inventory (it inherits from Inventory).

# Now, let's override the add_item method. 
# First, add an add_item method to your new SortedInventory class. 
# It should also take an item argument. 
# Inside your new add_item method, use super() to call add_item() and pass it item to make sure the item 
# still gets added to the slots list.

#Sorted inventories should be just that: sorted. Right now, we just add an item onto the slots list whenever our add_item method is called. 
# In the SortedInventory's add_item method, use the list.sort() method to make sure the slots list gets sorted 
# after an item is added.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
        
class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        #self.slots.append(item)
        self.slots.sort()



    