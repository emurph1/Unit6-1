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
    if side == 'before':
        print(guess + randL)
        data['cL'] += str(guess) + str(randL)
        challenge(1,2,3)
    elif side == 'after':
        print(randL + guess)
        data['cL'] += str(randL) + str(guess)
        challenge(1,2,3)
   
def challenge(cL,pN,oP):
    oP = str('Player 2')
    pN = str('Player 1')
    chall = input('Would ' + oP +' like to challenge '+ pN + '? ')
    if chall == 'yes' or 'Yes':
        print('Challenge')
    elif chall == 'no' or 'No' or 'NO':
        print('Player 2 turn')
        
#main code that generates the "board" and displays the letters (starting and input)
if __name__ == '__main__':
    data = {}
    data['pN'] = ''
    data['cL'] = ''
    data['oP'] = ''
    
    lettersL = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    randL = lettersL[randint(1,26)-1]
    print('Starting letter: ', randL)
    guess = input('Player 1 enter a letter: ')
    side = input('before or after? ')
    updateLetter(randL,guess,side)
    
    