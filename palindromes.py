#Emily Murphy
#2017-12-07
#palindromes.py - prints out all palindromes in the dictionary

dictionary = open('palindromes.txt')

for word in dictionary:
    backwards = word.reverse()
    if backwards == word:
        print(word)
