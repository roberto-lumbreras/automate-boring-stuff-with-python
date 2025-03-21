# Write a program that opens all .txt files in a folder
# and searches for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

import sys, re
from pathlib import Path

# here we get the path of the directory where we want to perform the search
# as an argument or current working directory
if len(sys.argv)<2:
    path = Path.cwd()
else:
    path = Path(sys.argv[1])
    
# now we are looking only for text files
matchingPaths = path.glob(pattern='*.txt')
# we ask te user for a regular expression
userInput = input('Enter a regular expression to look for in the text files\n')
# now we iterate over each line of each text file and if theres a match
# we print the whole line where the match was found
for matchingPath in matchingPaths:
    file = open(file=matchingPath,mode='r')
    for line in file.readlines():
        match = re.search(pattern=userInput, string=line)
        if match is not None:
            print(line)
