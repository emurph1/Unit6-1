#Emily Murphy
#12/13/17
#quiz6.py

D = open('engmix.txt')

'''for word in D:
    if word.count('c') == 3:
        print(word.strip())
    elif word.count('p') == 2:
        print(word.strip())'''
        
'''for line in D:
    line = line.strip()
    if line != '':
        if line[0] == 'r':
            print(line)'''

'''num = int(input('Enter number:'))
for word in D:
    word = word.strip()
    length = len(word)
    answer = ''
    if length == num:
        answer = word
        break
print(answer)'''

'''letter = input('Enter letter: ')
for word in D:
    word = word.strip()
    if letter not in word:
        print(word)'''

L = []
for word in D:
    word = word.strip()
    L.append(word)
    if len(word)%2 == 0:
        print(word[len(word)//2-1:len(word)//2+1])
    else:
        print(word[len(word)//2])
    
    
    
    
    
    