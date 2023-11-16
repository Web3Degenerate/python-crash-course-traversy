# Added (32:06): https://youtu.be/JJmcL1N2KQs?si=_AI4U0yjrofazXzs&t=1926

# A Dictionary is a collection which is unordered, changeable and indexed. 
# No duplicate members.

# similar to an object literal in javascript
# similar to a hash in ruby

# Similar to javascript objects and json

# Create dict

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person)) # {'first_name': 'John', 'last_name': 'Doe', 'age': 30} <class 'dict'>

# Use constructor (less common?)
# person2 = dict(first_name='Sara', last_name="Williams")
# print(person2, type(person2))

# Get a single value
# In JavaScript we'd use an object literal with dot notation 'person.name'
# Python use brackets: 
print(person['first_name'])


# Use get method (less common way)
print(person.get('last_name'))

# Add key/value
person['phone'] = '123-456-7890'

# Get all the keys
print(person.keys()) # returns > dict_keys(['first_name', 'last_name', 'age', 'phone'])

# Get all the items (key => value pairs)
print(person.items()) 

# Get all the values
print(person.values()) # returns all values


# Copy a dictionary with the .copy() method 
# SIMILAR to how JavaScript spread operator works
# Get all the values of an object and then add to it if desired
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)


# Remove item
del(person['age']) # removes age

# Remove item with pop
person.pop('phone') # removes phone

print(person)

# Clear a Dictionary
person.clear()

print(person) # returns {}


# Get dictionary length (number of key-value pairs)

print(len(person2)) #returns 5


# List of dictionaries (40:50)

people = [
    {'name':'Martha', 'age': 30},
    {'name':'Kevin', 'age': 25}
]

print(people)

# print Kevin's Age
print(people[1]['age'])