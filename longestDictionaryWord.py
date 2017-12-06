#Emily Murphy
#2017-12-06
#longestDictionaryWord.py - find longest word in dictionary

dictionary = open('engmix.txt')

lettercount = 0
maxletters = 0
maxword = ''
for word in dictionary:
    if len(word) > lettercount:
        lettercount = len(word)
    if lettercount > maxletters:
        maxletters = lettercount
        maxword = w
        lettercount = 0
        
print(maxword)