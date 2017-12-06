#Emily Murphy
#2017-12-06
#zzwords.py - prints words that contain 'zz'

dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    if 'zz' in word:
        print(word.strip()) #gets rid of weird spacing after each word
    wordCount += 1
    
