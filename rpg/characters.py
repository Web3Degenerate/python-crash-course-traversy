# https://teamtreehouse.com/library/objectoriented-python-2/multiple-superclasses

class Character:
    def __init__(self, name="", **kwargs):
        #Check that name is defined
        if not name:
            raise ValueError("'name' is required.")
                
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    