#Emily Murphy
#2017-12-07
#palindromes.py - prints out all palindromes in the dictionary

dictionary = open('palindromes.txt')

for word in dictionary:
    word = word.strip()
    if word != '':
        L = []
        for ch in word:
            L.append(ch)
            

