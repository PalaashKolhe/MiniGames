'''
title: Battleship
author: Palaash Kolhe
date created: 2019-06-03
'''

import random

gridPlayer1 = [
    [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['J', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

gridPlayer2 = [
    [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['J', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

## Subroutines
def chkCoord(shipArray, length):
    if shipArray[0][0] == shipArray[1][0]:
        if len(shipArray[1]) == 2:
            if int(shipArray[1][1]) - int(shipArray[0][1]) + 1 != length:
                ship = turnToList(input("The ship isn't this long! Enter different co-ordinates: "))
                return chkCoord(ship, length)
            else:
                return shipArray
        else:
            if 10 - int(shipArray[0][1]) + 1 != length:
                ship = turnToList(input("The ship isn't this long! Enter different co-ordinates: "))
                return chkCoord(ship, length)
            else:
                return shipArray
    else:
        if len(shipArray[0]) == 3 or len(shipArray[1]) == 2:
            if shipArray[0][1:3] == shipArray[1][1:3]:
                for i in range(len(letters)):
                    if shipArray[0][0] == letters[i]:
                        num1 = i
                    if shipArray[1][0] == letters[i]:
                        num2 = i
                if num2 - num1 + 1 != length:
                    ship = turnToList(input("This ship isn't this long! Enter different co-ordinates: "))
                    return chkCoord(ship, length)
                else:
                    return shipArray
            else:
                ship = turnToList(input("This ship isn't this long! Enter different co-ordinates: "))
                return chkCoord(ship, length)
        elif shipArray[0][1] == shipArray[1][1]:
            for i in range(len(letters)):
                if shipArray[0][0] == letters[i]:
                    num1 = i
                if shipArray[1][0] == letters[i]:
                    num2 = i
            if num2 - num1 + 1 != length:
                ship = turnToList(input("This ship isn't this long! Enter different co-ordinates: "))
                return chkCoord(ship, length)
            else:
                return shipArray
        else:
            ship = turnToList(input("The ship isn't this long! Enter different co-ordinates: "))
            return chkCoord(ship, length)


def turnToList(ship):
    ship = list(ship)
    ship = ''.join(ship)
    ship = ship.split('-')

    if len(ship[1]) != 1:
        if ship[0] not in positions or ship[1] not in positions:
            ship = input("Please enter valid co-ordinates: ")
            return turnToList(ship)
    return ship

def shipPlacement(shipArray, length, letter, grid):
    for i in range(len(grid)):
        if grid[i][0] == shipArray[0][0]:
            if len(shipArray[-1]) == 1:
                if shipArray[0][0] == shipArray[-1]:
                    for j in range(length):
                        grid[i][int(shipArray[0][1]) + j] = letter
                else:
                    if len(shipArray[0]) == 2:
                        for j in range(length):
                            grid[i+j][int(shipArray[0][1])] = letter
                    else:
                        for j in range(length):
                            grid[i+j][10] = letter
            else:
                if shipArray[0][0] == shipArray[1][0]:
                    for j in range(length):
                        grid[i][int(shipArray[0][1]) + j] = letter
                else:
                    if len(shipArray[0]) == 2:
                        for j in range(length):
                            grid[i+j][int(shipArray[0][1])] = letter
                        else:
                            for j in range(length):
                                grid[i+j][10] = letter

def chkSpot(ship, length, turn): ## check to see if spot is filled with A,B,C,D,E
    if turn == 'human':
        for i in range(len(gridPlayer1)):
            if gridPlayer1[i][0] == ship[0][0] and gridPlayer1[i][0] == ship[1][0]:
                for j in range(length):
                    if len(ship[0]) == 2:
                        if gridPlayer1[i][int(ship[0][1]) + j] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                    else:
                        if gridPlayer1[i][10 + j] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                return ship

            elif gridPlayer1[i][0] == ship[0][0] and gridPlayer1[i + length - 1][0] == ship[1][0]:
                for j in range(length):
                    if len(ship[0]) == 2:
                        if gridPlayer1[i + j][int(ship[0][1])] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                    else:
                        if gridPlayer1[i + j][10] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                return ship
    else:
        ship = turnToList(ship)
        for i in range(len(gridPlayer2)):
            if gridPlayer2[i][0] == ship[0][0] and gridPlayer2[i][0] == ship[1]:
                for j in range(length):
                    if len(ship[0]) == 2:
                        if gridPlayer2[i][int(ship[0][1]) + j] in ('A', 'B', 'C', 'D', 'E'):
                            ship = [random.choice(positions), '-', random.choice(letters)]
                            return chkSpot(chkSpaces(ship, length, turn), length, turn)
                        else:
                            pass
                    else:
                        if gridPlayer2[i][10] in ('A', 'B', 'C', 'D', 'E'):
                            ship = [random.choice(positions), '-', random.choice(letters)]
                            return chkSpot(chkSpaces(ship, length, turn), length, turn)
                        else:
                            pass
                return ship
            elif gridPlayer2[i][0] == ship[0][0]:
                for j in range(length):
                    if len(ship[0]) == 2:
                        if gridPlayer2[i + j][int(ship[0][1])] in ('A', 'B', 'C', 'D', 'E'):
                            ship = [random.choice(positions), '-', random.choice(letters)]
                            return chkSpot(chkSpaces(ship, length, turn), length, turn)
                        else:
                            pass
                    else:
                        if gridPlayer2[i + j][10] in ('A', 'B', 'C', 'D', 'E'):
                            ship = [random.choice(positions), '-', random.choice(letters)]
                            return chkSpot(chkSpaces(ship, length, turn), length, turn)
                        else:
                            pass
                return ship

def displayGrid():
    print('''''')
    for i in range(len(gridPlayer1)):
        print(' | '.join(gridPlayer1[i]))

    print('''''')
    for i in range(len(gridPlayer2)):
        print(' | '.join(gridPlayer2[i]))

def chkSpaces(ship, length, turn): ## number of blank places
    if turn == 'human':
        if ship[0][0] == ship[1][0]:
            if int(ship[0][1]) > (11 - length):
                ship = chkCoord(turnToList(input("There are not enough spots available to fit the ship! Enter different co-ordinates: ")), length)
                return chkSpaces(ship, length, 'human')
        else:
            for i in range(len(letters)):
                if ship[0][0] == letters[i]:
                    try:
                        letters[i + length - 1]
                        return ship
                    except IndexError:
                        ship = chkCoord(turnToList(input("There are not enough spots available to fit the ship! Enter different co-ordinates: ")), length)
                        return chkSpaces(ship, length, 'human')
        return ship
    else:
        if ship[0][0] == ship[-1]:
            if int(ship[0][1]) > (11 - length):
                ship[0] = random.choice(positions)
                return chkSpaces(ship, length, 'ai')
        else:
            for i in range(len(letters)):
                if ship[0][0] == letters[i]:
                    try:
                        letters[i + length - 1]
                        return ship
                    except IndexError:
                        ship[0] = random.choice(positions)
                        return chkSpaces(ship, length, 'ai')
        return ship
## Creating array to check for user input
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
positions = []

for i in range(len(letters)):
    for j in range(len(numbers)):
        var = str(letters[i]) + str(numbers[j])
        positions.append(var)

### MAIN CODE STARTS HERE ###
### Inputs
carrier1 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-A5) of where you want to place the aircraft carrier (AAAAA): ')), 5), 5, 'human'), 5, 'human')
shipPlacement(carrier1, 5, 'A', gridPlayer1)

batship1 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-D1) of where you want to place the battleship (BBBB): ')), 4), 4, 'human'), 4, 'human')
shipPlacement(batship1, 4, 'B', gridPlayer1)

cruiser1 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-A3) of where you want to place the cruiser (CCC): ')), 3), 3, 'human'), 3, 'human')
shipPlacement(cruiser1, 3, 'C', gridPlayer1)

sub1 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. D3-F3) of where you want to place the submarine (DDD): ')), 3), 3, 'human'), 3, 'human')
shipPlacement(sub1, 3, 'D', gridPlayer1)

destroyer1 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-A2) of where you want to place the destroyer (EE): ')), 2), 2, 'human'), 2, 'human')
shipPlacement(destroyer1, 2, 'E', gridPlayer1)

### Processing
## AI - Computer choosing its positions
carrier2 = chkSpaces([random.choice(positions), '-',  random.choice(letters)], 5, 'ai')
shipPlacement(carrier2, 5, 'A', gridPlayer2)

batship2 = chkSpot(chkSpaces([random.choice(positions), '-',  random.choice(letters)], 4, 'ai'), 4, 'ai')
shipPlacement(batship2, 4, 'B', gridPlayer2)

cruiser2 = chkSpot(chkSpaces([random.choice(positions), '-',  random.choice(letters)], 3, 'ai'), 3, 'ai')
shipPlacement(cruiser2, 3, 'C', gridPlayer2)

sub2 = chkSpot(chkSpaces([random.choice(positions), '-',  random.choice(letters)], 3, 'ai'), 3, 'ai')
shipPlacement(sub2, 3, 'D', gridPlayer2)

destroyer2 = chkSpot(chkSpaces([random.choice(positions), '-',  random.choice(letters)], 2, 'ai'), 2, 'ai')
shipPlacement(destroyer2, 2, 'E', gridPlayer2)

### Outputs
displayGrid()