# Created at (49:46): https://youtu.be/JJmcL1N2KQs?si=YRFzqb5ZQv8daT4w&t=2986

x = 10
y = 50  

# Comparison Operators (==, !=, >, <, >=, <=)

if x > y:
    print(f'{x} is greater than {y}')
else: 
    print(f'{y} is greater than {x}')


x = 10
y = 10 

# else if with 'elif'

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else: 
    print(f'{y} is greater than {x}')


# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Better to do nested if above with Logical Operators

# Logical Operators (and, or, not) - used to combine conditional statements
# AND
if x > 2 and x <= 10:
    print(f'AND Logical Operator: {x} is greater than 2 and less than or equal to 10')

# OR (just one has to be true)
if x > 2 or x <= 10:
    print(f'OR Logical Operator: {x} is greater than 2 and less than or equal to 10')

x = 38
y = 83

# NOT 
if not(x == y): 
    print(f'NOT Logical Operator: {x} is not equal to {y}')



# Membership Operators (not, not in) - (56:10)
# Membership operators are used to test if a sequence is presented in an object. 
# Test to see if something is in a list

# x = 3
numbers = [1,2,3,4,5]

# if 3 in numbers:
#     print(3 in numbers) # return bool
x = 3
if x in numbers:
    print(x in numbers) # return bool True

x = 38
if x not in numbers:
    print(x not in numbers) #return bool True


# Identity Operators (is, is not) - (57:45)
# Compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location: 

# (not common) - is

x = 20
y = 20
if x is y: 
    print(x is y)

x = 20
y = 21
if x is not y:
    print(x is not y)