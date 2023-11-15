# Started at (18:31): https://youtu.be/JJmcL1N2KQs?si=VvRdba_WT67gFoBp&t=1111

# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor to create a duplicate list
# numbers2 = list((1,2,3,4,5))    #like new array() in javascript. Not commonly used.
# print(numbers, numbers2)

# Get a value from our list (like array)
print(fruits[1])

# Get length of list
print(len(fruits))

# Append item to end of list
fruits.append('Mangos')

# Remove item from list
fruits.remove('Grapes')

# Insert into certain position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries' #(replaced Apple which was position 0)

# Remove from certain position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list (alphabetical order)
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

