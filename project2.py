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
    nL = input( p + 'enter a letter: ')
    s = input('before or after? ')
    if side == 'before':
        print(guess + randL)
        data['cL'] += str(guess) + str(randL)
        data['cL'] = cL
        challenge(1,2,3)
    elif side == 'after':
        print(randL + guess)
        data['cL'] += str(randL) + str(guess)
        data['cL'] = cL
        challenge(1,2,3)
    data['p'] = 'Player 2'
   
def challenge(cL,pN,oP):
    oP = str('Player 2')
    pN = str('Player 1')
    chall = input('Would ' + oP +' like to challenge '+ pN + '? ')
    if chall == 'yes' or 'Yes':
        ans = input('Player 1 enter reserve word or add another letter: ')
        if ans not in DList:
            print('Word not in dictionary' + oP + 'wins')
        return True
    elif chall == 'no' or 'No' or 'NO':
        return False
        
#main code that generates the "board" and displays the letters (starting and input)
if __name__ == '__main__':
    data = {}
    data['pN'] = ''
    data['cL'] = ''
    data['oP'] = ''
    data['p'] = 'Player 1'
    lettersL = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    randL = lettersL[randint(1,26)-1]
    print('Starting letter: ', randL)
    updateLetter(randL,guess,side)
    
    