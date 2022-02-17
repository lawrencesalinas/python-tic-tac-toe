# create a display board for the game
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[0] + '|' + board[1] + '|' + board[2] )
    
    
test_board = ['#','X','O','X','X','O','X','X','O','X']
display_board(test_board)
