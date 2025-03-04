board = {'topLeft': ' ', 'topMid': ' ', 'topRight': ' ', 
         'midLeft': ' ', 'midMid': ' ', 'midRight': ' ', 
         'lowLeft': ' ', 'lowMid': ' ', 'lowRight': ' '}
def printBoard(board):
    print(board['topLeft'] + '|' + board['topMid'] + '|' + board['topRight'])
    print('-+-+-')
    print(board['midLeft'] + '|' + board['midMid'] + '|' + board['midRight'])
    print('-+-+-')
    print(board['lowLeft'] + '|' + board['lowMid'] + '|' + board['lowRight'])
printBoard(board)
turn = 'X'
for i in range(9):
    print('Turn for ' + turn + '. Move on which space?')
    board[input()] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    printBoard(board)