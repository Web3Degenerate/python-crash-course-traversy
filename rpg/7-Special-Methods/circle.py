# https://teamtreehouse.com/library/objectoriented-python-2/special-methods

class Circle:
  def __init__(self, diameter):
    self.diameter = diameter


# GETTER METHOD (effectively)
  # use property anywhere we have circle instance
  @property
  def radius(self):
    return self.diameter / 2

# SETTER METHOD  
  # Add setter method: ("Decorating" with '@')
  @radius.setter
  def radius(self, radius):
    self.diameter = radius * 2
  

small = Circle(10)
print(small.diameter) # returns 10
print(small.radius)   # returns 5.0

# Can't SET the radius WITHOUT the @radius.setter
set_radius = small.radius = 10
print(f'Set small.radius to 10, returns: {set_radius}') # (10) returns 'AttributeError: can't set attribute' w/o @radius.setter
print(f'small.diameter is now: {set_radius}') # (20) returns 'AttributeError: can't set attribute'


