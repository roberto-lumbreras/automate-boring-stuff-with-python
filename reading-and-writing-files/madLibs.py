import sys
from pathlib import Path

#this version replaces all occurrences with the given input

path = Path(sys.argv[1])
file = open(file=path, mode='r')
text = file.read()
file.close()
wordsToSubstitute = ['ADJECTIVE','NOUN','VERB','ADVERB']
foundAnything = False
for i in range(len(wordsToSubstitute)):
    if text.find(wordsToSubstitute[i]) != -1:
        print(f'Enter a/an {wordsToSubstitute[i].lower()}:')
        text = text.replace(wordsToSubstitute[i], input())
        foundAnything = True
if not foundAnything:
    print('No keywords to substitute found')
if foundAnything:
    print('Type a name for the modified text file')
    name = input()
    newFile = open(path.parent / (name + '.txt'), 'w')
    newFile.write(text)
    newFile.close()
