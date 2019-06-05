'''
Shaishav Shah & Palaash Kolhe
Tic-Tac-Toeeeeeee
2019-06-04
'''
### Variables ###

repeat = True
wins = ((7,4,1),(8,5,2),(9,6,3),(4,5,6),(7,8,9),(1,2,3),(7,5,3),(1,5,9))

### Subroutines ###

def makemove(player,num):
    global grid, gridarray
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    #
    if grid[num] in ['X','O']:
        usr = int(input('Space not available, choose something else: '))
        return makemove(player, usr)
    else:
        grid[num] = mark
    #

def printgrid():
    global gridarray, grid
    gridarray = [
        [grid[7], '|', grid[8], '|', grid[9]],
        ['----------'],
        [grid[4], '|', grid[5], '|', grid[6]],
        ['----------'],
        [grid[1], '|', grid[2], '|', grid[3]]
    ]
    print('\n')
    for i in range(len(gridarray)):
        print(' '.join(gridarray[i]))
    print('\n')

def checkwin(player):
    global win, grid, gridarray
    win = 0
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    # win check
    if win == 0:
        for i in range(len(wins)):
            if grid[wins[i][0]] == grid[wins[i][1]] == grid[wins[i][2]] == mark:
                win = 1
                break
    return win

def start():
    print('''
Welcome to Tic-Tac-Toeeee !
We hope you know how to play!
''')


def main_make_move():
    global win, grid, gridarray, turn
    #
    if turn == 0:
        print("Player 2's turn")
    else:
        print('Player',str(turn),"'s turn")
    #
    move = int(input('Your move: '))
    makemove(turn, move)
    printgrid()
    win = checkwin(turn)
    if win == 0:
        turn += 1
        turn = turn % 2
    else:
        pass

def again(usr):
    global repeat
    usr1 = usr.lower()
    if usr1 in ['y','yes','']:\
        pass
    else:
        repeat = False
###########################
# ------ Main code ------ #
###########################
start()

while repeat:
    grid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    gridarray = [
        [grid[7], '|', grid[8], '|', grid[9]],
        ['----------'],
        [grid[4], '|', grid[5], '|', grid[6]],
        ['----------'],
        [grid[1], '|', grid[2], '|', grid[3]]
    ]
    win = 0
    turn = 1
    printgrid()
    # Input + Processing
    while win == 0:

        if turn == 0:
            main_make_move()
        else:
            main_make_move()

    # Output
    if win == 1:
        if turn == 1:
            print('Player 1 won! ')
        else:
            print('Player 2 won! ')
    again(input('Again? '))

############################

