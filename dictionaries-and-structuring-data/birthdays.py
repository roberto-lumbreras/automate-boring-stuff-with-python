birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name (blank to quit)')
    name = input()
    if not name:
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('There is no birthday information for '+name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday data updated')