#English to Pig Latin
#If a word begins with a vowel, the word yay is added to the end of it
#If a word begins with a consonant or consonant cluster (like ch or gr),
#that consonant or cluster is moved to the end of the word followed by ay.

def pigLatinfy(word):
    VOWELS = ('a','e','i','o','u','y')
    prefixNonLetters = ''
    suffixNonLetters = ''
    while not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
        if not len(word)>0:
            break
    if len(word)>0:
        while not word[-1].isalpha():
            suffixNonLetters += word[-1]
            word = word[:len(word)-1]
            if not len(word)>0:
                break
        if str(word).lower().startswith(VOWELS):
            word += 'yay'
        else:
            vowelFound = False
            consonantCluster = ''
            for letter in word:
                for vowel in VOWELS:
                    if letter.lower() == vowel:
                        vowelFound = True
                        break
                if not vowelFound:
                    consonantCluster += letter
                else:
                    break
            word = word[len(consonantCluster):] + consonantCluster.lower() + 'ay'    
    return prefixNonLetters+word+suffixNonLetters
        
                    

print('Enter the English message you want to translate to Pig Latin')
message = input()
words = message.split()
for i in range(len(words)):
    words[i] = pigLatinfy(words[i])
message = ' '.join(words)
print(message)
