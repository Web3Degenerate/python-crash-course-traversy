import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
            
# Signal inheritance by passing the parent class as a param to the child class
class Thief(Character):
    sneaky = True

# **kwargs is a catchall dictionary full of key value pairs you assign when instantiating the class
    #def __init__(self, name, sneaky=True, **kwargs):
      #self.name = name
      #self.sneaky = sneaky
        
# setattr lets us set values for key-value pairs we don't know exist yet      
      #for key, value in kwargs.items():
        #setattr(self, key, value)

    def __init__(self, name, sneaky=True, **kwargs):
        #Call super() first to prevent conflict if someone passed in sneaky=True as kwargs argument
        #When we use super() we have to include the method name and the required arguments.
        #As if we were creating an instance of the parent class ('Character')
        super().__init__(name, **kwargs)
        # self.sneaky = True #wouldn't allow subsequent change ('kenneth.sneaky = False')
        self.sneaky = sneaky
  
    def pickpocket(self):
       return self.sneaky and bool(random.randint(0, 1))
 
    def hide(self, light_level):
      return self.sneaky and light_level < 10
    
# kenneth = Thief('Kenneth', sneaky=False, clever=True)
# kenneth.sneaky (False) 
# kenneth.clever (True)
