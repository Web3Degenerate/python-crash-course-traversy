# Created at (1:30:55): https://youtu.be/JJmcL1N2KQs?si=4lrSSxqAW0IqEo6Q&t=5455

# JSON is commonly used with data APIs.  Here is how we can parse JSON into a Python dictionary. 

# import the json module
import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict (just like json.stringify or parse in JS, we have such methods in python)
user = json.loads(userJSON)

print(user) #returns dictionary of user {'first_name': 'John', 'last_name': 'Doe', 'age': 30}'

#Access just the first_name
print(user['first_name']) #returns John


# Turn dict into JSON at (1:33:48): https://youtu.be/JJmcL1N2KQs?si=uyzxk_3tN_ZqjwZB&t=5628
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)
print(type(carJSON))