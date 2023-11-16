# Added at (24:26): https://youtu.be/JJmcL1N2KQs?si=HytKgSEPvewbuute&t=1466

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members

print('**** TUPLE SECTION ****')

# Create tuple 
fruits = ('Apples', 'Oranges', "Grapes")

# (Uncommon) - Create tuple with constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
# print(fruits, fruits2)

# Get tuple value
print(fruits[1])

# Can't change the value of a tuple
# fruits[0] = 'Pears' # >TypeError: 'tuple' object does not support item assignment



# SINGLE VALUE needs trailing comma
# if you only have one value, leave a trailing comma. 
# fruits2 = ('Apples')

# without trailing comma interprets as string
# print(fruits2, type(fruits2)) # >Apples <class 'str'>

fruits3 = ('Apples',)
# print(fruits3, type(fruits3)) # >Apples <class 'tuple'>

# DELETE a Tuple item (here using the del method)
# del fruits3
# print(fruits3) # returns undefined since deleted.


# Get length of tuple
print(len(fruits))


# (28:58) A Set is a collection which is unordered and unindexed. No duplicate members.

print('**** SET SECTION ****')

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Remove item from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set) # returns empty set => set()

# Delete set
# del fruits_set
# print(fruits_set) # returns error. Deleting it is the same as never defining it. 


# NO DUPLICATES ALLOWED IN A SET
grocery_list = {'eggs', 'milk', 'bacon'}
print(grocery_list)

grocery_list.add('eggs') #No error, just doesn't add it twice!
print(grocery_list)