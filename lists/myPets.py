myPets = ['Misi','Fu','Gamusino']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named '+name)
else:
    print(name+' is my pet')