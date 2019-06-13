import random
#######################

grid_1 = []
grid_2 = []
hit1 = 0
hit2 = 0

#######################
def creategrid(grid):
    for i in range(10):
        grid.append([])
        for k in range(10):
            grid[i].append(' ')

def printgrid(grid):
    print('  0   1   2   3   4   5   6   7   8   9')
    for i in range(len(grid)):
        print(chr(65 + i),' | '.join(grid[i]),'|')

def ai_move_1():
    global hit1
    aiX = random.randrange(10)
    aiY = random.randrange(10)
    if makemove(aiX, aiY,grid_1,2) == True:
        hit1 = 1
    else:
        pass
    return aiX, aiY

def makemove(X,Y,grid, player):
    if grid[Y][X] == ' ':
        grid[Y][X] == '-'
        return False
    else:
        grid[Y][X] == 'X'
        return True

def ai_move_2(oldX,oldY):
    #
    global hit2,d
    #
    d = random.randrange(4)
    if d == 0: # down
        if makemove(oldX,oldY+1,grid_1,2):
            hit2 = 1
        else:
            d1.append(d)
    elif d == 1: # Up
        if makemove(oldX, oldY - 1, grid_1, 2):
            hit2 = 1
        else:
            d1.append(d)
    elif d == 2: # Right
        if makemove(oldX+1, oldY, grid_1, 2):
            hit2 = 1
        else:
            d1.append(d)
    else: # Left
        if makemove(oldX-1, oldY, grid_1, 2):
            hit2 = 1
        else:
            d1.append(d)

def ai_move_2_part_2(orignalX, orignalY):
    global hit2,d, d1

    while d in d1:
         d = random.randrange(4)
    if d == 0: # down
        if makemove(orignalX,orignalY+1,grid_1,2):
            hit2 = 1
    elif d == 1: # Up
        if makemove(orignalX, orignalY - 1, grid_1, 2):
            hit2 = 1
    elif d == 2: # Right
        if makemove(orignalX+1, orignalY, grid_1, 2):
            hit2 = 1
    else: # Left
        if makemove(orignalX-1, orignalY, grid_1, 2):
            hit2 = 1

def ai_move_3(X,Y,ogX, ogY):
    pass
#######################

creategrid(grid_1)
creategrid(grid_2)
grid_1[5][7] = 'S'
grid_1[5][8] = 'S'
grid_1[5][9] = 'S'
ai_move_1()
printgrid(grid_1)