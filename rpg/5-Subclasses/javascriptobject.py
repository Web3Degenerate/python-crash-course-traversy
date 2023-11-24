#Create dict to act like JS object (8:00): https://teamtreehouse.com/library/objectoriented-python-2/subclassing-builtins

#This will have the ability to look up keys with a dot '.'

class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try: 
            return self[item]
        except KeyError:
            return super().__getattribute__(item) #defaults to getattribute's attempt to find any match?
        

jso = JavaScriptObject({'name': 'Kenneth'})
jso.language = 'Python'
print(jso.name) #returns 'Kenneth'
print(jso.language) #returns 'Python'
# print(jso.errorz) #returns TWO errors:
# (#1) KeyError: 'errorz' 
# (#2) AttributeError: 'JavaScriptObject' object has no attribute 'errorz'



# SUBCLASS int
# Make class named Double that extends int. 
class Double(int):
# Override __new__. 
# Create a new int instance from whatever is passed in as arguments and keyword arguments. Return that instance.
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        #return self
# Double (multiply by two) the int that you created in __new__.  
# Return the new, doubled value. 
# For example Double(5) would return 10
        return int(self) * 2
        #return self * 2 #guess this works as well? 
    
double = Double(5)
print(f'Subclass of int class Double returned: {double}')


# CHALLENGE: https://teamtreehouse.com/library/objectoriented-python-2/advanced-objects/frustration
# Now I want you to make a subclass of list. Name it Liar.
# Override the __len__ method so that it always returns the wrong number of items in the list. 
# For example, if a list has 5 members, the Liar class might say it has 8 or 2.
# You'll probably need super() for this.

class Liar(list):
    def __init__(self, *args, **kwargs):      
        super().__init__(*args, **kwargs) 
        #self.slotz = []
        #self.append() #append a copy of whatever they gave us
        self.slotz = []
    
    def add(self, item):
        self.slotz.append(item)
            
    def __len__(self):
        find_len = len(self.slotz)
        return find_len + 2