# https://teamtreehouse.com/library/objectoriented-python-2/multiple-superclasses

class Character:
    def __init__(self, name="", **kwargs):
        #Check that name is defined
        if not name:
            raise ValueError("'name' is required.")
                
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    #Returns a string that we use to identify our object whenever it is turned into a string
    def __str__(self):
        #tell if archer, thief or barbarian etc.
        return "{}: {}".format(self.__class__.__name__, self.name)