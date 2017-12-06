#Emily Murphy  
#2017-12-06
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    if 'murph' in word:
        print(word)
    wordCount += 1
    
print('There are', wordCount, 'words in the dictionary')