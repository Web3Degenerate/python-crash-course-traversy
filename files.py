# Created at (1:26:18): https://youtu.be/JJmcL1N2KQs?si=8skAcRHxewu9EcrN&t=5178

# Python has functions for creating, reading, updating and deleting files. 

# CREATE FILE
# Open a file (run `python files.py` and it creates 'myfile.txt')
# (file_name, mode (w for write))

myFile = open('myfile.txt', 'w')


# Get some info on newly created file 'myfile.txt'
print('Name: ', myFile.name)         # 'myfile.txt'
print('Is Closed: ', myFile.closed)  # 'False'
print('Opening Mode: ', myFile.mode) # 'w'


# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
# Then close
myFile.close()

# Append to file (after close above)
# Open it again, but THIS time use mode 'a' for append. If we used 'w' write again, we'd overwrite our file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP.')
myFile.close()


# READ from file (1:30:20)
# Use mode 'r+' to read
myFile = open('myfile.txt', 'r+')
# pass in the number of characters to read, here '100'
text = myFile.read(100)
print(text)

# Pick up with JSON at (1:30:55): https://youtu.be/JJmcL1N2KQs?si=4uBvIu87_ggFk32k&t=5455