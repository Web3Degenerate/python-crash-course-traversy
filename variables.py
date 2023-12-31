# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1           # int
# y = 2.5         # float
# name = 'John'   # str
# is_cool = True  # bool


# Multiple Assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic Math
a = x + y

# Casting
x = str(x)

# Type
print(type(x))

y = int(y) # was 2.5, int turns to whole number
z = float(y) # turn int 2 back to float, goes to 2.0

print(type(y), y)
print(type(z), z)

# Use parenthesis when printing: 
print('Hello', name)
print(name)
print(x, y, name, is_cool, a)





