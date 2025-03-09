#Say you want to find an American phone number in a string. 
# You know the pattern if you’re American: 
# three numbers, a hyphen, 
# three numbers, a hyphen,
# and four numbers.
# Here’s an example: 415-555-4242

def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
number = '334-332-1212'
print(f'Is {number} a phone number?')
print(isPhoneNumber(number))
number = 'moshi moshi'
print(f'Is {number} a phone number?')
print(isPhoneNumber(number))
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    if isPhoneNumber(message[i:i+12]):
        print('Phone number found '+message[i:i+12])