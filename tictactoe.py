import random
# display board
def display_board(b):
    print(b[6]+'|'+b[7]+'|'+b[8])
    print(b[3]+'|'+b[4]+'|'+b[5])
    print(b[0]+'|'+b[1]+'|'+b[2])

#empty the board
def reset_board(b):
    for i in range(len(b)):
        b[i] = ''
    display_board(b)
    
def board_not_full(b):
    for item in b:
        if not item:
            return True
    return False

def check_emptiness(b, cell):
    if b[cell] == '':
        print("Empti cell")
        return True
    elif b[cell] == 'X' or b[cell] == 'O':
        return False

def display_result(b):
    if b[0] == 'X' and b[1] == 'X' and b[2] == 'X':
        print('player1 with value X won')
    elif b[0] == 'O' and b[1] == 'O' and b[2] == 'O':
        print('player2 with value O won')
    elif b[3] == 'X' and b[4] == 'X' and b[5] == 'X':
        print('player1 with value X won')
    elif b[3] == 'O' and b[4] == 'O' and b[5] == 'O':
        print('player2 with value O won')
    elif b[6] == 'X' and b[7] == 'X' and b[8] == 'X':
        print('player1 with value X won')
    elif b[6] == 'O' and b[7] == 'O' and b[8] == 'O':
        print('player2 with value O won')
    elif b[0] == 'X' and b[3] == 'X' and b[6] == 'X':
        print('player1 with value X won')
    elif b[0] == 'O' and b[3] == 'O' and b[6] == 'O':
        print('player2 with value O won')
    elif b[1] == 'X' and b[4] == 'X' and b[7] == 'X':
        print('player1 with value X won')
    elif b[1] == 'O' and b[4] == 'O' and b[7] == 'O':
        print('player2 with value O won')
    elif b[2] == 'X' and b[5] == 'X' and b[8] == 'X':
        print('player1 with value X won')
    elif b[2] == 'O' and b[5] == 'O' and b[8] == 'O':
        print('player2 with value O won')
    elif b[0] == 'X' and b[4] == 'X' and b[8] == 'X':
        print('player1 with value X won')
    elif b[0] == 'O' and b[4] == 'O' and b[8] == 'O':
        print('player2 with value O won')
    elif b[6] == 'X' and b[4] == 'X' and b[2] == 'X':
        print('player1 with value X won')
    elif b[6] == 'O' and b[4] == 'O' and b[2] == 'O':
        print('player2 with value O won')
    else:
        print('Game is a Draw')

def player_choose_cell(b, var):

    cell = int(input( " Enter the cell you would like to choose (0 to 8): "))
    while cell not in range(0, 9):
        print("Please enter a number between 0 and 8")
        cell = int(input(" Enter the cell you would like to choose (0 to 8): "))
    empti = check_emptiness(b, cell)
    if empti:
        b[cell] = var
        display_board(b)
    else:
        cell = int(input("Selected cell is already occupied, please try again."))
        b[cell] = var
        display_board(b)

#choose player
def choose_player(b):
    rint1 = random.randint(1,2)
    if rint1 == 1:
        players = (1,2)
    else:
        players = (2,1)
    print("Players are ",players,"in that order")

    if players[0] == 2:
        player_choose_cell(test_board, 'O')
        player_choose_cell(test_board,'X')
    else:
        player_choose_cell(test_board, 'X')
        player_choose_cell(test_board, 'O')

    return players

def continue_play(b):
    reset_board(b)
    #Choose player and start game
    players = choose_player(b)
    while board_not_full(b):
        if players[0] == 2:
            while board_not_full(b):
                player_choose_cell(test_board, 'O')
                break
            while board_not_full(b):
                player_choose_cell(test_board, 'X')
                break

        elif players[0] == 1:
            while board_not_full(b):
                player_choose_cell(test_board, 'X')
                break
            while board_not_full(b):
                player_choose_cell(test_board, 'O')
                break
    display_board(test_board)
    display_result(test_board)

def restart_game(b):
    restart = input("Game over, do you want to restart the game?Y/N")
    if restart.lower() == 'y':
        reset_board(b)
        continue_play(b)
    else:
        display_result(test_board)
        exit(0)

#function calls
test_board = ['X','O','X','O','X','O','X','O','X']
display_board(test_board)
continue_play(test_board)
restart_game(test_board)









