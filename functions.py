# Added at (42:24): https://youtu.be/JJmcL1N2KQs?si=Fj7Rta18ciMQOdsn&t=2544

# A function is a block of code which only runs when it is called. 
# In Python, we do not use curly brackets, 
# we use INDENTATION with tabs or spaces


# Create funciton, returns hello
# Instead of using brackets, use ':' colon and indentation
def sayHello(name ='Sam'):
    print(f'Hello {name}')

sayHello('John Doe')

# Default parameters
sayHello()


# Function to Return Values
def getSum(num1, num2): 
    total = num1 + num2
    return total

# getSum(30,8)
# print(getSum(30,8))
num = getSum(30,8)
print(num)




# A lambda function is a small anonymous function. 

# A lambda function can take any number of arguments, 
# but can only have ONE expression. 
# Very similar to a JS arrow function. 

#like const getSum in JS
                #params      values
getSummer = lambda num1, num2 : num1 + num2 #implicity return whatever expression equals

print(getSummer(10,3))