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

