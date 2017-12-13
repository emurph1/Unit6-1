#Emily Murphy
#12/13/17
#quiz6.py

D = open('engmix.txt')

'''for word in D:
    if word.count('c') == 3:
        print(word.strip())
    elif word.count('p') == 2:
        print(word.strip())'''
        
for line in D:
    line = line.strip()
    if line != '':
        if line[0] == 'r':
            print(line)
        
