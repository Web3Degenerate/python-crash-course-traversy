#Created (3:45): https://teamtreehouse.com/library/objectoriented-python-2/controlling-conversion

class NumString:
    def __init__(self, value):
        self.value = str(value)
        
    def __str__(self):
        return self.value
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)

#Math: https://teamtreehouse.com/library/objectoriented-python-2/math 

# Concatenates numbers (5 + 4 = 54)
    # def __add__(self, other):
    #     return self.value + str(other)
    
    def add_as_string(self, other):
        return self.value + str(other)

# Adds the numbers as expected
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

# Add if NumString(5) is on the right:    
# radd is reflective addition (either side)
    def __radd__(self, other):
        return self + other    

# __iadd__ In place addition so we can say age=25, age + 1
    def __iadd__(self, other): 
        self.value = self + other
        return self.value

# __mul__ for multiply
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other
    
    def __rmul__(self, other):
        self.value = self * other
        return self.value

    def __imul__(self, other):
        self.value = self * other
        return self.value

#When using built in __add__
# five = NumString(5)
# print(five + 4) #returns 54  

five = NumString(5)
print(five.add_as_string(4)) #returns 54

print(five + 4) #using __add__ now returns 9

five_point_five = NumString(5.5) #using __add__ now returns 9.5
print(five_point_five + 4)

print(4 + five_point_five) #works with __radd__

age = NumString(25)
print(age + 5) # __add__ is working (30)
print(5 + age) # __radd__ is working (30)
age += 1
print(age) # __iadd__ is working (26)

# MULTIPLY
five_mul = NumString(5)
print(five_mul * 3) # __mul__ returns 15
print(3 * five_mul) # __rmul__ returns 15
# five_mul *= 3     # __imul__ worked in TTH. Not here.
# print(five_mul)