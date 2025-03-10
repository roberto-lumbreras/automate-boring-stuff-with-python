# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
# Note that if the day or month is a single digit, it’ll have a leading zero.

#The regular expression doesn’t have to detect correct days for each month or for leap years;
# it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
# Then store these strings into variables named month, day, and year,
# and write additional code that can detect if it is a valid date.
# April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days.
# February has 29 days in leap years.
# Leap years are every year evenly divisible by 4,
# except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
# Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

import re, pyperclip

def isValidDate(match):
    day,month,year = match
    day = int(day)
    month = int(month)
    year = int(year)
    if year < 3000 and year > 999 and month > 0 and month < 13 and day > 0 and day < 32:
        if month in [2,4,6,9,11]:
            if month != 2:
                return day < 31
            else:
                if isLeapYear(year):
                    return day < 30
                return day < 29
        else:
            return True
    else:
        return False
    
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

regex = re.compile(r'''
                    ([0-3]   # first digit for days
                    [0-9])   # second digit for days
                    /       # first separator
                    ([01]    # first digit for months
                    [0-9])   # second digit for months
                    /       # second separator
                    ([12]    # first digit for years
                    \d{3})   # last 3 digits for years 
                   ''', re.VERBOSE)

copiedText = pyperclip.paste()
listOfMatches = regex.findall(copiedText)
if len(listOfMatches)>0:
    listOfValidDates = []
    for match in listOfMatches:
        if isValidDate(match):
            listOfValidDates.append('/'.join(match))
    pyperclip.copy('\n'.join(listOfValidDates))
    print('Copied to clipboard')
else:
    print('No valid dates in format [DD/MM/YYYY] found')
    
