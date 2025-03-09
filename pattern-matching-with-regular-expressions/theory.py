# Regular expressions, called regexes for short, are descriptions for a pattern of text.
# For example, a \d in a regex stands for a digit character—that is, any single numeral from 0 to 9.
# The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python
# to match the same text pattern the previous isPhoneNumber() function did:
# a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers.
# Any other string would not match the \d\d\d-\d\d\d-\d\d\d\d regex.
# But regular expressions can be much more sophisticated.
# For example, adding a 3 in braces ({3}) after a pattern is like saying,
# “Match this pattern three times.” 
# So the slightly shorter regex \d{3}-\d{3}-\d{4} also matches the correct phone number format.

import re
phoneNumber = '333-333-3333'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# same as
phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}$')
print(phoneNumber + ' is a phone number?' + str(phoneNumberRegex.search(phoneNumber) is not None))
print(phoneNumber + '3' + ' is a phone number?' + str(phoneNumberRegex.search(phoneNumber+'3') is not None))

# A Regex object’s search() method searches the string it is passed for any matches to the regex.
# The search() method will return None if the regex pattern is not found in the string.
# If the pattern is found, the search() method returns a Match object,
# which have a group() method that will return the actual matched text from the searched string.

phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
matchObject = phoneNumberRegex.search('anyString'+phoneNumber+'anyString')
print('Phone number found: ' + matchObject.group())

# Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).
# Then you can use the group() match object method to grab the matching text from just one group.
# By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text.
# Passing 0 or nothing to the group() method will return the entire matched text.

phoneNumber = '111-222-3333'
phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
print('Area code of phone number '+phoneNumber+': '+phoneNumberRegex.search(phoneNumber).group(1))

# If you would like to retrieve all the groups at once, use the groups() method
# Since .groups() returns a tuple of multiple values,
# you can use the multiple-assignment trick to assign each value to a separate variable

firstGroup, secondGroup = phoneNumberRegex.search(phoneNumber).groups()
print('First group: '+firstGroup+'\nSecond group: '+secondGroup)

# Backslash can be used as an escape character in regex

phoneNumber = '(111) 222-3333'
phoneNumberRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
print(f'{phoneNumber} is a valid phone number? {phoneNumberRegex.search(phoneNumber) is not None}')
firstGroup, secondGroup = phoneNumberRegex.search(phoneNumber).groups()
print('First group: '+firstGroup+'\nSecond group: '+secondGroup)

# The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.
# In regular expressions, the following characters have special meanings:
# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
# ----> Backslash can be used as an escape character in regex <-----


# The | character is called a pipe. You can use it anywhere you want to match one of many expressions.

regex = re.compile(r'batman|spiderman')
print(f'batman matches? {regex.search('batman') is not None}')
print(f'spiderman matches? {regex.search('spiderman') is not None}')

# When both expressions exist in the searched string, the first occurrence of matching text will be returned

print(f'This should print spiderman {regex.search('spiderman and batman').group()}\nAnd this should print batman {regex.search('batman and spiderman').group()}')

# You can also use the pipe to match one of several patterns as part of your regex.
# This can be done with parentheses.

regex = re.compile(r'bat(man|girl)')
print(f'batman matches? {regex.search('batman') is not None}')
print(f'batgirl matches? {regex.search('batgirl') is not None}')

# Sometimes there is a pattern that you want to match only optionally.
# That is, the regex should find a match regardless of whether that bit of text is there.
# The ? character flags the group that precedes it as an optional part of the pattern.

regex = re.compile(r'bat(wo)?man')
print(f'batman matches? {regex.search('batman') is not None}')
print(f'batwoman matches? {regex.search('batwoman') is not None}')

# You can think of the ? as saying,
# “Match zero or one of the group preceding this question mark.”

# The * (called the star or asterisk) means “match zero or more”.
# The group that precedes the star can occur any number of times in the text.
# It can be completely absent or repeated over and over again.

regex = re.compile(r'bat(wo)*man')
print(f'batman matches? {regex.search('batman') is not None}')
print(f'batwoman matches? {regex.search('batwoman') is not None}')
print(f'batwowoman matches? {regex.search('batwowoman') is not None}')

# While * means “match zero or more,” the + (or plus) means “match one or more.”
# Unlike the star, which does not require its group to appear in the matched string,
# the group preceding a plus must appear at least once. It is not optional.

regex = re.compile(r'Bat(wo)+man')
text = 'The adventures of Batman'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')
text = 'The adventures of Batwoman'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')
text = 'The adventures of Batwowoman'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')

# If you have a group that you want to repeat a specific number of times,
# follow the group in your regex with a number in braces.
# For example, the regex (Ha){3} will match the string 'HaHaHa'

regex = re.compile(r'(Ha){3}')
text = 'HaHaHa'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')
text = 'HaHa'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')

# Instead of one number, you can specify a range by writing a minimum,
# a comma, and a maximum in between the braces. 
# For example, the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.

regex = re.compile(r'(Ha){3,5}')
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')
text = 'HaHaHa'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')
text = 'HaHaHaHaHa'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')


# You can also leave out the first or second number in the braces to leave the minimum or maximum unbounded.

regex = re.compile(r'(Ha){1,}')
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')
text = 'Ha'
print(f'There is a match in \'{text}\'? {regex.search(text) is not None}')

# Since (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa',
# you may wonder why the Match object’s call to group() in the previous brace example returns 'HaHaHaHaHa'
# instead of the shorter possibilities.
# After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression (Ha){3,5}.
# Python’s regular expressions are greedy by default,
# which means that in ambiguous situations they will match the longest string possible.
# The non-greedy (also called lazy) version of the braces,
# which matches the shortest string possible,
# has the closing brace followed by a question mark.

text = 'Ha' * 5
regex = re.compile(r'(Ha){3,5}?')
print(f'The match in this case should be \'HaHaHa\' -> {regex.search(text).group()}')

# Note that the question mark can have two meanings in regular expressions:
# declaring a non-greedy match or flagging an optional group.
# These meanings are entirely unrelated.

# findall() will not return a Match object but a list of strings—as long as there are no groups in the regular expression.
# Each string in the list is a piece of the searched text that matched the regular expression.

regex = re.compile(r'\d{3}-\d{3}-\d{4}')
text = 'Cell: 415-555-9999 Work: 212-555-0000'
print(f'List of phone numbers found in \'{text}\' -> {regex.findall(text)}')

# If there are groups in the regular expression, then findall() will return a list of tuples.
# Each tuple represents a found match, and its items are the matched strings for each group in the regex.

regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
print(f'List of phone numbers found in \'{text}\' with regex groups displayed as a tuple -> {regex.findall(text)}')

# you learned that \d could stand for any numeric digit.
# That is, \d is shorthand for the regular expression (0|1|2|3|4|5|6|7|8|9). 
# There are many such shorthand character classes
# \d -> Any numeric digit from 0 to 9.
# \D -> Any character that is not a numeric digit from 0 to 9.
# \w -> Any letter, numeric digit, or the underscore character.
# \W -> Any character that is not a letter, numeric digit, or the underscore character.
# \s -> Any space, tab, or newline character.
# \S -> Any character that is not a space, tab, or newline character.

regex = re.compile(r'\d+\s\w+')
text = 'I found 3 apples, 4 ladies and 2 gentlemen'
print(f'Matches for \'{text}\' {regex.findall(text)}')

# There are times when you want to match a set of characters
# but the shorthand character classes (\d, \w, \s, and so on) are too broad.
# You can define your own character class using square brackets.
# For example, the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase.

regex = re.compile(r'[aeiouAEIOU]')
text = 'Loreem ipsum'
print(f'vowels found in \'{text}\' -> {regex.findall(text)}')

# You can also include ranges of letters or numbers by using a hyphen.
# For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.
# Note that inside the square brackets, the normal regular expression symbols are not interpreted as such.
# This means you do not need to escape the ., *, ?, or () characters with a preceding backslash.
# For example, the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.].
# By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class.
# A negative character class will match all the characters that are not in the character class.

regex = re.compile(r'[^aeiouAEIOU]')
print(f'characters that are not vowels found in \'{text}\' -> {regex.findall(text)}')

# You can also use the caret symbol (^) at the start of a regex
# to indicate that a match must occur at the beginning of the searched text.
# Likewise, you can put a dollar sign ($) at the end of the regex
# to indicate the string must end with this regex pattern.
# And you can use the ^ and $ together
# to indicate that the entire string must match the regex—that is,
# it’s not enough for a match to be made on some subset of the string.

text = 'Hello, world!'
regex = re.compile(r'^Hello')
print(f'Match found for regex \'^Hello\' in \'{text}\' -> {regex.search(text).group()}')
text = 'World, hello!'
regex = re.compile(r'^hello')
print(f'Match found for regex \'^hello\' in \'{text}\' -> {regex.search(text)}')
text = 'miauhello'
regex = re.compile(r'hello$')
print(f'Match found for regex \'hello$\' in \'{text}\' -> {regex.search(text).group()}')
text = 'miauhello!'
print(f'Match found for regex \'hello$\' in \'{text}\' -> {regex.search(text)}')
text = '4.3'
regex = re.compile(r'^\d+$')
print(f'Match found for regex \'^\d+$\' in {text} -> {regex.search(text)}')
text = '43'
print(f'Match found for regex \'^\d+$\' in {text} -> {regex.search(text).group()}')

# The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

regex = re.compile(r'.at')
wordsEndingInAt = ['cat','rat','flat','at']
matches = regex.findall(str(wordsEndingInAt))
print(f'Matches for regex \'.at\' in \'{wordsEndingInAt}\' -> {matches}')

#  You can use the dot-star (.*) to stand in for that “anything.”
# Remember that the dot character means “any single character except the newline,”
# and the star character means “zero or more of the preceding character.”

regex = re.compile(r'First name: (.*) Last name: (.*)')
text = 'First name: Roberto Last name: Lumbreras'
matchObject = regex.search(text)
firstName = matchObject.group(1)
lastName = matchObject.group(2)
print(f'First name -> {firstName}')
print(f'Last name -> {lastName}')

# The dot-star uses greedy mode: It will always try to match as much text as possible.
# To match any and all text in a non-greedy fashion, use the dot, star, and question mark (.*?).
# Like with braces, the question mark tells Python to match in a non-greedy way.

text = '<To serve man> for dinner.>'
regex = re.compile(r'<.*>')
print(f'For regex \'<.*>\' match found in {text} -> {regex.search(text).group()}')
regex = re.compile(r'<.*?>')
print(f'For regex \'<.*?>\' match found in {text} -> {regex.search(text).group()}')

# Both regexes roughly translate to “Match an opening angle bracket, followed by anything, followed by a closing angle bracket.”
# But the string '<To serve man> for dinner.>' has two possible matches for the closing angle bracket.
# In the non-greedy version of the regex, Python matches the shortest possible string: '<To serve man>'.
# In the greedy version, Python matches the longest possible string: '<To serve man> for dinner.>'.

#The dot-star will match everything except a newline.
# By passing re.DOTALL as the second argument to re.compile(),
# you can make the dot character match all characters, including the newline character.

text = 'Serve the public trust.\nProtect the innocent'
regex = re.compile(r'.*')
print(f'Match for text regex \'.*\' in \'{text}\' -> {regex.search(text).group()}')
regex = re.compile(r'.*', re.DOTALL)
print(f'Match for text regex \'.*\' in \'{text}\' using the re.DOTALL argument -> {regex.search(text).group()}')

# This chapter covered a lot of notation, so here’s a quick review of what you learned about basic regular expression syntax:
# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a non-greedy match of the preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
# [abc] matches any character between the brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the brackets.

# Normally, regular expressions match text with the exact casing you specify.
# But sometimes you care only about matching the letters without worrying whether they’re uppercase or lowercase.
# To make your regex case-insensitive, you can pass re.IGNORECASE as a second argument to re.compile().

regex = re.compile('man', re.IGNORECASE)
text = 'Who\'s the MAN? I am.'
print(f'Match found for regex \'man\' in \'{text}\' -> {regex.search(text) is not None}')
text = 'Man that looks delicious.'
print(f'Match found for regex \'man\' in \'{text}\' -> {regex.search(text) is not None}')

# Regular expressions can not only find text patterns but can also substitute new text in place of those patterns.
# The sub() method for Regex objects is passed two arguments.
# The first argument is a string to replace any matches.
# The second is the string for the regular expression.
# The sub() method returns a string with the substitutions applied.

text = 'Your password is BIGfluffyKITTIES'
regex = re.compile(r'(password)(\s)*(is)?(\s)*(.+)')
print(regex.sub('*******',text)) 

# Sometimes you may need to use the matched text itself as part of the substitution.
# In the first argument to sub(), you can type \1, \2, \3, and so on, to mean
# “Enter the text of group 1, 2, 3, and so on, in the substitution.”

print(regex.sub(r'\1\2\3\4*******',text)) 

# egular expressions are fine if the text pattern you need to match is simple.
# But matching complicated text patterns might require long, convoluted regular expressions.
# You can mitigate this by telling the re.compile() function to ignore whitespace and comments
# inside the regular expression string.
# This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# You can spread the regular expression over multiple lines with comments like this:

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Note how the previous example uses the triple-quote syntax (''')
# to create a multiline string so that you can spread the regular expression definition over many lines,
# making it much more legible.

# The comment rules inside the regular expression string are the same as regular Python code:
# the # symbol and everything after it to the end of the line are ignored.
# Also, the extra spaces inside the multiline string for the regular expression
# are not considered part of the text pattern to be matched.
# This lets you organize the regular expression so it’s easier to read.




















