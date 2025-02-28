import random

playerInput = ''
print('ROCK, PAPER, SCISSORS')
wins = 0
ties = 0
losses = 0
computerMove = ''
while playerInput != 'q':
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
    playerInput = input()
    if playerInput == 'r':
        print('ROCK VERSUS...')
    elif playerInput == 'p':
        print('PAPER VERSUS...')
    elif playerInput == 's':
        print('SCISSORS VERSUS...')
    elif playerInput == 'q':
        break
    else:
        continue
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    if randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    if randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    if computerMove == playerInput:
        print('It is a tie!')
        ties = ties + 1
    elif computerMove == 'r' and playerInput == 's' or computerMove == 'p' and playerInput == 'r' or computerMove == 's' and playerInput == 'p':
        print('You lose!')
        losses = losses + 1
    else:
        print('You win!')
        wins = wins + 1
    
    
    
    