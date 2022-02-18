import random

# create a display board for the game
def display_board(board):
    # clear output and only show the new version of the board, print 100 new lines
    print('\n'*100)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    
    
test_board = [' ']*10
# display_board(test_board)

def player_input():
    marker = ''
    # keep asking player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O:').upper()
    # Assign player 2 the opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)
player1_marker, player2_marker = player_input()
print('Player 1 marker:',player1_marker)
print('Player 2 marker:',player2_marker)
 
def place_marker(board, marker, position):
    board[position] = marker
    
place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board, mark):
    # Win TIC TAC TOE
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
display_board(test_board)
win_check(test_board,'X')

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

    


