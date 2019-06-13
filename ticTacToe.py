'''
Shaishav Shah
Tic-Tac-Toe
2019-06-04
'''
def makemove(player,num,grid,gridarray):
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    #
    if grid[num] in ['X','O']:
        usr = int(input('Space not avaliable, choose something else: '))
        return makemove(player, usr, grid, gridarray)
    grid[num] = mark
    #

def printgrid(gridarray, grid):
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

def checkwin(player, win, grid, gridarray, wins):
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
Welcome to Tic-Tac-Toe !
We hope you know how to play!
''')

def chktic(move,grid):
    if move in [1,2,3,4,5,6,7,8,9]:
        return move
    else:
        usr = int(input('Valid spot: '))
        return chktic(usr, grid)

def main_make_move(win, grid, gridarray, turn, wins):
    #
    if turn == 0:
        print("Player 2's turn")
    else:
        print('Player',str(turn),"'s turn")
    #
    move = int(input('Your move: '))
    makemove(turn, chktic(move,grid),grid,gridarray)
    printgrid(gridarray,grid)
    win_1 = checkwin(turn, win, grid, gridarray, wins)
    if win_1 == 0:
        turn += 1
        turn = turn % 2
    else:
        pass
    return win_1, turn

def check_if_spot_open(num): # Doesnt work idk why

    global grid
    if grid[num] == ' ' :
        return num
    else:
        usr = int(input('Someone is already there, choose something else: '))
        return check_if_spot_open(usr)

##########################################################################################