#Emily Murphy
#2017-12-14
#project2.py - Lexicant (word guessing game)

from random import randint

#loads all words from dictionary (D) to a list (DList)
def loadD():
    D = open('engmix.txt')
    DList = []
    for word in D:
        DList.append(word.strip())
    return DList
    
def updateLetter(cL,nL,s):
    if side == 'front':
        print(guess + randL)
    elif side == 'back':
        print(randL + guess)
   
#def challenge(cL,pN,oP)
    
#main code that generates the "board" and displays the letters (starting and input)
if __name__ == '__main__': 
    lettersL = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    randL = lettersL[randint(1,26)-1]
    print('Starting letter: ', randL)
    guess = input('Player 1 enter a letter: ')
    side = input('Front or back? ')
    updateLetter()
    
    