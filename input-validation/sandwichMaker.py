import pyinputplus as pyinput

bread = pyinput.inputMenu(['wheat','white','sourdough'], 'Choose your favourite bread\n', numbered=True)
protein = pyinput.inputMenu(['chicken','turkey','ham','tofu'], 'Choose your favourite protein\n', numbered=True)
cheese = pyinput.inputYesNo('Do you want cheese?\n')
if cheese == 'yes':
    cheese = pyinput.inputMenu(['cheddar','swiss','mozarella'], 'Choose your favourite cheese\n', numbered=True)
extras = {'mayo': None,'mustard': None,'lettuce':None,'tomato': None}
for k in extras:
    extras[k] = pyinput.inputYesNo(f'Do you want {k}?\n')
numberOfSandwiches = pyinput.inputInt('How many of them?\n', min=1,max=10)
prices = {'wheat': 1,
          'white': 0.9,
          'sourdough': 1.2,
          'chicken': 2.5,
          'turkey': 2.8,
          'ham': 2.3,
          'tofu': 2,
          'cheddar': 1,
          'swiss': 1.2,
          'mozarella': 1.1,
          'mayo': 0.3,
          'mustard': 0.25,
          'lettuce': 0.4,
          'tomato': 0.5
          }
total = prices[bread] + prices[protein]
if cheese != 'no':
    total += prices[cheese]
for k in extras:
    if extras[k] == 'yes':
        total += prices[k]
total *= numberOfSandwiches
print(f'Your sandwich will be {total}€')