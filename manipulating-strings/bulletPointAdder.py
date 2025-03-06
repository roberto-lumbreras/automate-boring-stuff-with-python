import pyperclip
stringToModify = pyperclip.paste()
lines = stringToModify.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
pyperclip.copy('\n'.join(lines))
print('text modified and copied to the clipboard')