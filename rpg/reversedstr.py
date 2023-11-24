# Subclassing Built-ins: https://teamtreehouse.com/library/objectoriented-python-2/subclassing-builtins
# If customizing MUTABLE objects (like list) use __init__
# If customizing IMMUTABLE objects use __new__

# no built-in for reverse string
class TestInheritance(str):
    pass

# IMMUTABLE so use __new__
class ReversedStr(str): #extends built-in str class
    # safer to use __new__ than super() here (3:15)
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


#Confirm inheritance from str working (won't reverse string)
rs = TestInheritance('hello world')
print(rs) #returns 'hello world'

#using self[::-1]
rs = ReversedStr('hello world')
print(rs) #returns 'dlrow olleh'


# MUTABLE so use __init__
import copy

class FilledList(list):
    #Ignore args and kwargs for now
    def __init__(self, count, value, *args, **kwargs):      
        super().__init__() #We want an EMPTY list and ignore everything that was passed in: 
        #brand new empty list instance:
        for _ in range(count):  # the underscore '_' ignore the number that would come out of range
            #Use copy.copy b/c if they send in something mutable, like another list, each member in that filled list that was a copy of that list would be the same member. If you changed one you'd change all of them.
            #With copy.copy we are getting brand new versions of that list ((6:30))
            self.append(copy.copy(value)) #append a copy of whatever they gave us


#Send in 9 copies of the number '2'
# fl = filledlist.FilledList(9, 2)
fl1 = FilledList(9, 2)
print(f'The f1 list has length of: {len(fl1)}')
print(f"The f1 list's contains: {fl1}")

# Test the copy.copy part is working (7:10): https://teamtreehouse.com/library/objectoriented-python-2/subclassing-builtins
#fl2 will have two copies of list 1, 2, 3
fl2 = FilledList(2, [1, 2, 3])
print(f'The fl2 list has length of: {len(fl2)}')
print(f"The fl2 list's contains: {fl2}")

#Change fl2's first item's, 2nd item to be 5, so => [[1, 5, 3], [1, 2, 3]]
fl2[0][1] = 5
print(f"The fl2 list's first item's second item is now changed: {fl2}")