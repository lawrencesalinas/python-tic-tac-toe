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
        marker = input('Player 1, choose X or O:')
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
    



