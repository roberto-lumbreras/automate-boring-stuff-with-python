import sys, re
from pathlib import Path

#this version replaces each occurrence with the given input

path = Path(sys.argv[1])
file = open(file=path, mode='r')
text = file.read()
file.close()
regex = re.compile('ADJECTIVE|NOUN|VERB|ADVERB')
foundAnything = False
match = regex.search(text)
while match is not None:
    foundAnything = True  
    print(f'Enter an {match.group().lower()}:')
    text = text.replace(match.group(),input(),1)
    match = regex.search(text)
if not foundAnything:
    print('No keywords to substitute found')
if foundAnything:
    print('Type a name for the modified text file')
    name = input()
    newFile = open(path.parent / (name + '.txt'), 'w')
    newFile.write(text)
    newFile.close()