'''
MiniGames
Shaishav Shah & Palaash Kolhe
2019-06-06
'''
import connect4
## Variables
game = 1
    # Connect 4 variables
c_gridarray = []
c_grid = []
c_border = []
c_turn = 0
c_win = 0

## Subroutines
def intro():
    print('''
Welcome to MiniGame! 
    ''')
def main_menu():
    print('''Which game would you like to play?
1) Connect-4
2) Tic-Tac-Toe
3) Coming soon
    ''')
    m_game = int(input('>>> '))
    return m_game

#### Main Code ####

m_game = main_menu()
if m_game == 1:
    # Setup the Connect 4 grid
    c_length = int(input('Length of Connect-4 grid: '))
    c_height = int(input('Height of Connect-4 grid: '))
    connect4.creategrid(c_length, c_height)
    if len(c_border) == 0:
        connect4.createborder(c_length)
    connect4.printgrid()
    # Gameplay


if m_game == 2:
    pass
if m_game == 3:
    pass

