from thieves import Thief

from characters import Character

#Loosely coupled code, easier mix & match (8:30): https://teamtreehouse.com/library/objectoriented-python-2/multiple-superclasses. (Not tightly coupled code).

#in Character class' init (name="",) and check that name is set.
kenneth = Thief(name="Kenneth", sneaky=False) #matches the *args param in attributes? 
print(kenneth.sneaky)
print(kenneth.agile)
print(kenneth.hide(8)) #hide when light level is 8 

#isinstance()
is_instance = isinstance('a', str)
print(f'string example is {is_instance}') #True

is_instance = isinstance(5.2, (int, float))
print(f'5.2 int & float is {is_instance}') #True (both int and float)

is_instance = isinstance(5.2, (str, bool, dict))
print(f'5.2 is string, bool or dict is {is_instance}') #False

is_instance = isinstance(True, int)
print(f'True is int (because 0 false, 1 true?) is {is_instance}') #True

#issubclass
is_subclass = issubclass(Thief, Character)
print(f'is Thief a subclass of Character is {is_subclass}')

#type
check_type = type(kenneth)
print(f'type check of kenneth is {check_type}')

# dunder is double underscores, kenneth dunder class is 
kenneth_dunder = kenneth.__class__
print(f'kenneth dunder is {kenneth_dunder}')

# kenneth dunder class dunder name is 'Thief'
kenneth_dunder = kenneth.__class__.__name__
print(f'kenneth dunder class dunder name is {kenneth_dunder}')