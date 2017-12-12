#Emily Murphy
#2017-12-07
#palindromes.py - prints out all palindromes in the dictionary

dictionary = open('palindromes.txt')


for word in dictionary:
    word = word.strip()
    L = []
    L.append(word)
    L.reverse()
    wordReverse = ''
    for ch in L:
        wordReverse = (wordReverse+ch)
    if word == wordReverse:
        print(word)