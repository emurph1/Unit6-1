#Emily Murphy
#2017-12-06
#reverseFile.py - input file name and prints lines in file in reverse order

fileName = input('Enter file name: ')
file = open(fileName)
L = []
for word in fileName:
    L.append(word)
    L.reverse()
    
print(L)
    
