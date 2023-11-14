# Added 10:29 (https://youtu.be/JJmcL1N2KQs?si=3tAtAnsylE-W_hOF&t=629)

name = 'Brad'
age = 37

#Contatenate

print ('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by Position: {variables} are place holders
print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-strings available in 3.6 and later 
# similar to javascript `` but instead we use f string
print(f'Hello for third time, my name is {name} and I am {age}')


# String Methods

s = 'hello world'

# Capitalize first letter of string
print(s.capitalize())

# All uppercase
print(s.upper())

# All Lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get string length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count occurence of something
sub = 'h'
print(s.count(sub))

# Resume (15:25): https://youtu.be/JJmcL1N2KQs?si=aUPkVIf6_dvZeiHd&t=925

