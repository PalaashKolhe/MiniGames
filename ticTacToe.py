'''
Shaishav Shah & Palaash Kolhe
Tic-Tac-Toeeeeeee
2019-06-04
'''
### Variables ###

grid = ['0','1','2','3','4','5','6','7','8','9']
gridarray = [
    [grid[7], '|',grid[8], '|',grid[9]],
    ['----------'],
    [grid[4], '|',grid[5], '|',grid[6]],
    ['----------'],
    [grid[1], '|',grid[2], '|',grid[3]]
]
repeat = True
wins = ((7,4,1),(8,5,2),(9,6,3),(4,5,6),(7,8,9),(1,2,3),(7,5,3),(1,5,9))
win = 0
turn = 0

### Subroutines ###

def makemove(player,num):
    global grid, gridarray
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    #
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
                win = 0
                break
    return win

def start():
    print('''
Welcome to Tic-Tac-Toeeee !
We hope you know how to play!
''')

def main_make_move():
    global win, grid, gridarray, turn
    move = int(input('Your move player',str(turn),': '))
    makemove(turn, move)
    printgrid()
    win = checkwin(turn)

###########################
# ------ Main code ------ #
###########################
start()
while win == 0:
    if turn == 0:



