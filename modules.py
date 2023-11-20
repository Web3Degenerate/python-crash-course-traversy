# Created At: (1:05:06): https://youtu.be/JJmcL1N2KQs?si=GEkvWEYSzA_2VbqQ&t=3906

# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager
# (including Django) as well as custom modules. 

# (1:05:46) Import the dateTime module: 
# Here the date object is IN datetime:

# import datetime
# today = datetime.date.today() # See docs for all the properties available.
# print(today)

# (1:06:44) import JUST date from datetime, instead of importing all of datetime
# Core modules (datetime and time)
import datetime
from datetime import date
today = date.today() 
print(today)


# Import Time
# import time
# timestamp = time.time()

import time
from time import time
timestamp = time()
print(timestamp)


# At (1:09:00) Covers Python package manager 'pip': https://youtu.be/JJmcL1N2KQs?si=HyOOaLhCfsHJx34W&t=4140
# install 'camelcase' from pip with
# 'pip install camelcase' - (he used 'pip3 install camelcase')

# Pip module (camelcase)
# import camelcase

from camelcase import CamelCase

c = CamelCase()

print(c.hump('hello there world'))


# At (1:13:05) Example of Custom Module to be imported: https://youtu.be/JJmcL1N2KQs?si=C32j1fOkWALZYydn&t=4385
# Create email validator function in 'validator.py'

from validator import validate_email

# email = 'test@test.com'
email = 'test#test.com'

if validate_email(email):
    print('Email is valid')
else: 
    print('Email is invalid')      