#Emily Murphy
#2017-12-07
#palindromes.py - prints out all palindromes in the dictionary

dictionary = open('palindromes.txt')
L = []
for word in dictionary:
    L.append(word.strip())
    backwards = L.reverse()
    if backwards == word:
        print(word)
