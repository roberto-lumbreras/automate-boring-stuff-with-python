while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')
while True:
    print('Select a password (numbers and letters only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have numbers and letters')
    