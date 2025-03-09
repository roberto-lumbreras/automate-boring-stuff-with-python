#Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters,
# and has at least one digit.
# You may need to test the string against multiple regex patterns
# to validate its strength.

import re

print('Introduce a password to check if it is strong enough')
password = input()
try:
    regex = re.compile(r'.{8,}') # Is it 8 characters long or more?
    match = regex.search(password).group()
    regex = re.compile(r'(.*[a-z]+.*[A-Z]+.*)|(.*[A-Z]+.*[a-z]+.*)') # contains both uppercase and lowercase characters?
    match = regex.search(match).group()
    regex = re.compile(r'.*\d.*') # has at least one digit?
    match = regex.search(match).group()
    print('Your password is strong')
except AttributeError:
    print('Your password is weak')

 