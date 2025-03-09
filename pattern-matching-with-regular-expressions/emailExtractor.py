# finds email adresses on the clipboard

import pyperclip, re

regex = re.compile(r'''
                   [a-zA-Z0-9._%+-]+    # username
                   @                    # @ symbol
                   [a-zA-Z0-9.-]+       # domain name
                   \.[a-zA-Z]{2,4}      # dot-something
                   ''', re.VERBOSE)

text = str(pyperclip.paste())
emailList = regex.findall(text)
if len(emailList)>0:
    listAsString = '\n'.join(emailList)
    pyperclip.copy(listAsString)
    print('Copied to clipboard')
else:
    print('No email adresses found')