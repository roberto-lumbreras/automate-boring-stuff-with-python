import pyinputplus as pyinput

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyinput.inputYesNo(prompt)
    if response == 'no':
        break
print('Thank you. Have a nice day')

# spansish version

while True:
    prompt = '¿Quieres saber como mantener ocupado a un idiota durante horas?\n'
    response = pyinput.inputYesNo(prompt, 'sí')
    if response == 'no':
        break
print('Gracias. Que tengas un buen día')
