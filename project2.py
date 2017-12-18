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
    nL = input( data['p'] + ' enter a letter: ')
    s = input('before or after? ')
    if s == 'before':
        print(nL + randL)
        data['cL'] += str(nL) + str(randL)
        data['cL'] = cL
        if len(data['cL']) == 3:
            challenge(1,2,3)
    elif s == 'after':
        print(randL + nL)
        data['cL'] += str(randL) + str(nL)
        data['cL'] = cL
        if len(data['cL']) == 3:
            challenge(1,2,3)
    data['p'] = 'Player 2'
   
def challenge(cL,pN,oP):
    oP = str('Player 2')
    pN = str('Player 1')
    chall = input('Would ' + oP +' like to challenge '+ pN + '? ')
    if chall == 'yes':
        ans = input('Player 1 enter reserve word or add another letter: ')
        for word in DList:
            if ans not in DList:
                print('Word not in dictionary' + oP + 'wins')
        return True
    elif chall == 'no':
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
    updateLetter(1,2,3)
    
    