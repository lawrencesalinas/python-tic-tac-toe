import random

# print board
def display_board(board):
    # clear output and only show the new version of the board, print 100 new lines
    print('\n'*30)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    
# test_board = [' ']*10
# display_board(test_board)

# give each player a marker
def player_input():
    marker = ''
    # keep asking until x or O is chosen
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose a marker: X or O ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)
            

# assign marker to board
def place_marker(board, marker, position):
    board[position] = marker
    
# check if there is a winning combination on the board
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
  

# check if a space is freely available on the board
def space_check(board, position):
    return board[position] ==  ' '

# randomly check which player goes first
def choose_first():
    flip = 0 
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# check if the board is full
def check_fullboard(board):
    for i in range(1-10):
        # if space exists, board is not full
        if space_check(board, i):
            return False
    # board is full return true
    return True

# Ask for a player's next position
def player_choice(board):
    position = 'wrong'
    
    
    while (position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position)) and position.isdigit() == False:
        position = (input('Choose a position: (1-9) '))
        
    return int(position)


# ask player if they want to play again
def replay():
    choice = input('Play again? Enter Yes or No')
    return choice == 'Yes'
    

print('Welcome to Tic Tac Toe!')
while True: # Reset the board 
    theBoard = [' '] * 10 
    player1, player2 = player_input() 
    turn = choose_first() 
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No. ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1, position)

            if win_check(theBoard, player1):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if check_fullboard(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2, position)

            if win_check(theBoard, player2):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if check_fullboard(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

        if not replay():
            break







 


