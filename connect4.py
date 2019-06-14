
#### - Subroutines - ####
def createborder(c_length,c_border):
    i = 0
    while i != c_length:
        c_border.append('-----')
        i += 1
    c_border[0] = ''.join(c_border)

def creategrid(c_length, c_height, c_grid,c_gridarray):
    #
    for i in range(c_length * c_height):
        c_grid.append(0)
    #
    for i in range(c_height):
        c_gridarray.append([])
        for k in range(c_length):
            c_gridarray[i].append(' ')

def printgrid(c_length, c_grid, c_gridarray,c_border):
    ind = []
    print('\n')
    for i in range(c_length):
        ind.append(str(i+1))
    ind = ' || '.join(ind)
    print(c_border[0])
    print('|',ind,'|')
    for i in range(len(c_gridarray)):
        print('|',' || '.join(c_gridarray[i]),'|')
    print(c_border[0])

def makemove(player, column,c_gridarray, c_length, c_height):
    if c_gridarray[0][column-1] == ' ':
        done = 0
        while done == 0:
            for i in range(c_height - 1, -1, -1):
                if c_gridarray[i][column - 1] == ' ':
                    if player == 1:
                        c_gridarray[i][column - 1] = 'X'
                    else:
                        c_gridarray[i][column - 1] = 'O'
                    done = 1

                    return column - 1, i  # to check if c_win
                    break
        return moveX, moveY
    else:
        usr = int(input('That column is full, so choose another move: '))
        return makemove(player, usr, c_gridarray, c_length, c_height)

def chkconnect4(usr,c_length):
    if usr <= c_length and usr > 0:
        return usr
    else:
        usr_1 = int(input('Valid column: '))
        return chkconnect4(usr_1, c_length)

def checkwin(player, Y, X, c_win, c_height, c_length, c_gridarray):
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    # Horizontal
    if c_win == 0:
        for k in range(c_height):
            for i in range(3, c_length):
                if c_gridarray[k][i] == c_gridarray[k][i - 1] == c_gridarray[k][i - 2] == c_gridarray[k][i - 3]==mark:
                    c_win = 1
                    break
        for k in range(c_height):
            for g in range(0,c_length - 3):
                if c_gridarray[k][g] == c_gridarray[k][g + 1] == c_gridarray[k][g + 2] == c_gridarray[k][g + 3]==mark:
                    c_win = 1
                    break
    # Vertical
    if c_win == 0:
        if Y <= (6-4):
            if c_gridarray[Y][X]==c_gridarray[Y+1][X]==c_gridarray[Y+2][X]==c_gridarray[Y+3][X] == mark:
                c_win = 1
    # / direction
    if c_win == 0:
        for j in range(c_height - 3):
            for i in range(3, c_length):
                if c_gridarray[j][i] == c_gridarray[j+1][i-1] == c_gridarray[j+2][i-2]==c_gridarray[j+3][i-3] == mark:
                    c_win = 1
                    break
    # \ direction
    if c_win == 0:
        for j in range(c_height-3):
            for i in range(c_length-3):
                if c_gridarray[j][i] == c_gridarray[j+1][i+1] == c_gridarray[j+2][i+2]==c_gridarray[j+3][i+3] == mark:
                    c_win = 1
                    break
    return c_win

def main_makemove(player,c_gridarray, c_length, c_height, c_win, c_turn, c_grid, c_border):
    print('Player',str(player),"'s c_turn")
    col = chkconnect4(int(input('Which column would you like to place the chip player: ')), c_length)
    X, Y = makemove(player,col,c_gridarray, c_length, c_height)
    printgrid(c_length, c_grid, c_gridarray,c_border)
    c_win = checkwin(player,Y, X, c_win, c_height, c_length, c_gridarray)
    if c_win == 1:
        c_win = player
    else:
        c_turn += 1
        c_turn = c_turn%2 # this way I can have 1 function to get both the players moves
    return X, Y, c_turn, c_win
