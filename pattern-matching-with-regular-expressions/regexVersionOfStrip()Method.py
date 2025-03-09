# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re,pyperclip

def regexStrip(string, charactersToRemove):
    if charactersToRemove is None or charactersToRemove == '':
        string = re.sub(r'^\s*|\s*$','',string)
    else:
        for char in charactersToRemove:
            string = re.sub(char,'',string)
    return string

text = pyperclip.paste()
print('Type the characters you want to remove from the content of the clipboard')
print('If nothing is typed spaces from the beggining and the end of the content will be removed')
charactersToRemove = input()
pyperclip.copy(regexStrip(text,charactersToRemove))
print('Copied to the clipboard')
