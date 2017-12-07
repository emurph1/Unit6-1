#Emily Murphy
#2017-12-06
#howManyWords.py - how many words there are for each number of letters

dictionary = open('engmix.txt')

L = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for word in dictionary:
    L[(len(word))-1] += 1
 
i = 0   
for i in range(len(word)):
    i += 1
    print('There are', L[i], 'words with', i, 'letters')
        