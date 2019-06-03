#### - Variables - ####
gridarray = []
grid = []
length = 8
height = 5
#### - Subroutines - ####

def creategrid(length, height):
    global gridarray, grid
    #
    for i in range(length * height):
        grid.append(0)
    #
    for i in range(height):
        gridarray.append([])
        for k in range(length):
            gridarray[i].append(' ')

def printgrid():
    global length, grid, gridarray
    ind = []
    print('\n')
    for i in range(length):
        ind.append(str(i+1))
    ind = ' || '.join(ind)
    print('----------------------------------------')
    print('|',ind,'|')
    for i in range(len(gridarray)):
        print(gridarray[i])
    print('----------------------------------------')

def makemove(player, column):
    global gridarray, length, height, moveX, moveY
    done = 0
    while done == 0:
        for i in range(height-1,-1,-1):
            if gridarray[i][column-1] == ' ':
                if player == 1:
                    gridarray[i][column-1] = 'X'
                else:
                    gridarray[i][column-1] = 'O'
                done = 1

                return i, column -1 # to check if win
                break

def checkwin(player, Y, X):
    global win
    win = 0
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    # Horizontal
    if win == 0:
        for k in range(height):
            for i in range(3, length):
                if gridarray[k][i] == gridarray[k][i - 1] == gridarray[k][i - 2] == gridarray[k][i - 3]==mark:
                    win = 2
                    break
        for k in range(height):
            for g in range(0,length - 3):
                if gridarray[k][g] == gridarray[k][g + 1] == gridarray[k][g + 2] == gridarray[k][g + 3]==mark:
                    win = 2
                    break
    # Vertical
    if win == 0:
        if gridarray[Y][X]==gridarray[Y+1][X]==gridarray[Y+2][X]==gridarray[Y+3][X] == mark:
            win = 1
    # / direction
    if win == 0:
        for j in range(height - 3):
            for i in range(3, length + 1):
                if gridarray[j][i] == gridarray[j+1][i-1] == gridarray[j+2][i-2]==gridarray[j+3][i-3] == mark:
                    win = 3
                    break
    # \ direction
    if win == 0:
        for j in range:
            pass




##### - Main Code - #####

creategrid(length,height)
printgrid()
Y, X = makemove(1,5)
Y, X = makemove(1,6)
Y, X = makemove(1,7)
Y, X = makemove(1,8)

printgrid()
checkwin(1,Y,X)

print(win)