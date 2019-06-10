'''
MiniGames
Shaishav Shah & Palaash Kolhe
2019-06-06
'''
import connect4, ticTacToe

###########################
# ------ Variables ------ #
###########################

game = 0
main_game = 0

    # Battle ship stuff


###########################
# ----- Subroutines ----- #
###########################


def intro():
    print('''
Welcome to MiniGame! 
    ''')
def main_menu():
    print('''
Which game would you like to play?

1) Connect-4
2) Tic-Tac-Toe
3) Coming soon
    ''')
    m_game = int(input('>>> '))
    return m_game
def again_for_every_game():
    global game
    usr = input('''
1. Play this game again
2. Switch to another game
3. Exit
>>>''')
    if usr == '1':
        pass
    elif usr == '2':
        game = 0
    elif usr == '3':
        game == 999
###########################
# ------ Main code ------ #
###########################
while main_game == 0: #### DOESN'T WORK

    game = main_menu()

    while game == 1: # CONNECT-4


        # Variables

        c_gridarray = []
        c_grid = []
        c_border = []
        c_turn = 0
        c_win = 0

         # Setup the Connect 4 grid

        c_length = int(input('Length of Connect-4 grid: '))
        c_height = int(input('Height of Connect-4 grid: '))
        connect4.creategrid(c_length, c_height,c_grid,c_gridarray)
        if len(c_border) == 0:
            connect4.createborder(c_length,c_border)
        connect4.printgrid(c_length, c_grid, c_gridarray,c_border)

        # Gameplay

        while c_win == 0:

            if c_turn == 0:
                X, Y, c_turn, c_win = connect4.main_makemove(1,c_gridarray, c_length, c_height,c_win,c_turn, c_grid, c_border)
            else:
                X, Y, c_turn, c_win = connect4.main_makemove(2, c_gridarray, c_length, c_height, c_win, c_turn, c_grid, c_border)

        # Output

        if c_win != 0:
            if c_win == 1:
                print('Player 1 wins! ')
            else:
                print('Player 2 wins! ')

        again_for_every_game()

    while game == 2: # TIC-TAC-TOE

        # Variables

        t_grid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        t_gridarray = [
            [t_grid[7], '|', t_grid[8], '|', t_grid[9]],
            ['----------'],
            [t_grid[4], '|', t_grid[5], '|', t_grid[6]],
            ['----------'],
            [t_grid[1], '|', t_grid[2], '|', t_grid[3]]
        ]
        t_wins = ((7, 4, 1), (8, 5, 2), (9, 6, 3), (4, 5, 6), (7, 8, 9), (1, 2, 3), (7, 5, 3), (1, 5, 9))
        t_win = 0
        t_turn = 1

        #

        ticTacToe.start()
        ticTacToe.printgrid(t_gridarray, t_grid)
        #
        while t_win == 0:
            if t_turn == 1:
                t_win, t_turn = ticTacToe.main_make_move(t_win, t_grid, t_gridarray, t_turn, t_wins)
            else:
                t_win, t_turn = ticTacToe.main_make_move(t_win, t_grid, t_gridarray, t_turn, t_wins)
        # Output
        if t_win == 1:
            if t_turn == 1:
                print('Player 1 wins!')
            else:
                print('Player 2 won!')

        again_for_every_game()

    while game == 3:
        pass
        break


