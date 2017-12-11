#Emily Murphy  
#12/11/17
#warmUp16.py 

dictionary = open('engmix.txt')

for line in dictionary:
    if line != '':
        if line[0] == 'e' and line[-1] == 'm': 
            print(line.strip())