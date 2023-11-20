# Set up around (1:13:05): https://youtu.be/JJmcL1N2KQs?si=C32j1fOkWALZYydn&t=4385
# import regular expression module: 
import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))