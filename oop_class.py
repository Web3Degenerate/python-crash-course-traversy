
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


