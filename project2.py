#Emily Murphy
#2017-12-14
#project2.py - Lexicant (word game)

from random import randint

#loads all words from dictionary (D) to a list (DList)
def loadD():
    D = open('engmix.txt')
    DList = []
    for word in D:
        DList.append(word.strip())
        return DList
        
#when the user adds a new letter
def updateLetter(cL,nL,s):
    if s == 'before':
        cL = nL + cL
    elif s == 'after':
        cL = cL + nL
    return cL
 
#defines what a challenge is and does it 
def challenge(cL,p,oP):
        chall = input('Would ' + oP +' like to challenge '+ p + '? ')
        if chall == 'yes':
            return True
        elif chall == 'no':
            return False
        
#main code that generates the "board" and displays the letters (starting and input)
if __name__ == '__main__':
    lettersL = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cL = lettersL[randint(1,26)-1]
    print('Starting letter: ', cL)
    while True:
        for i in range(0,1):
            p = "Player 1"
            oP = "Player 2"
            nL = input( p + ' enter a letter: ')
            s = input('before or after? ')
            cL = updateLetter(cL,nL,s)
            print(cL)
        for i in range(0,1):
            p = "Player 2"
            oP = "Player 1"
            nL = input( p + ' enter a letter: ')
            s = input('before or after? ')
            cL = updateLetter(cL,nL,s)
            print(cL)
        if len(cL) == 3:
            challenge(cL,p,oP)
            if True:
                answ = input(p + ' ,What word from the dictionary were you thinking of?')
                DList = loadD()
                for word in DList:
                    if answ == word:
                        print(oP + 'Loses and ' + p + 'wins!')
        challenge(cL,p,oP)
                
                
    
    