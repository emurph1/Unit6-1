#Emily Murphy
#2017-12-06
#reverseFile.py - input file name and prints lines in file in reverse order
file = open(input('Enter file name: '))
L = []
for line in file:
    L.append(line.strip())

print(L.reverse())
    
