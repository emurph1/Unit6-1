#Emily Murphy
#2017-12-07
#palindromes.py - prints out all palindromes in the dictionary

dictionary = open('palindromes.txt')
L = []
for word in dictionary:
    word = word.strip()
    if word != '':
        for ch in word:
            L.append(ch)
            if L == L.reverse():
                print(word)
