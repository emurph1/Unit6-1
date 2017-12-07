#Emily Murphy
#2017-12-06
#howManyWords.py - how many words there are for each number of letters

dictionary = open('engmix.txt')

L = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for word in dictionary:
    if len(word) == 1:
        