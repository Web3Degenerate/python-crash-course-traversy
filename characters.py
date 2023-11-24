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
  
    def pickpocket(self):
       return self.sneaky and bool(random.randint(0, 1))
 
    def hide(self, light_level):
      return self.sneaky and light_level < 10