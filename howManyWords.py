#Emily Murphy
#2017-12-06
#howManyWords.py - how many words there are for each number of letters

dictionary = open('engmix.txt')

L = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for word in dictionary:
    L[len(word.strip())-1] += 1
 
i = 0   
while i < len(L):
    print('There are', L[i], 'words with', i+1, 'letters')
    i += 1 