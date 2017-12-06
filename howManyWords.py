#Emily Murphy
#2017-12-06
#howManyWords.py - how many words there are for each number of letters

dictionary = open('engmix.txt')

L = []
for word in dictionary:
    if 'e' in word:
        L.append(word)

print(len(L))