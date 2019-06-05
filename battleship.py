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
def turnToList(ship):
    ship = list(ship)
    ship = ''.join(ship)
    ship = ship.split('-')
    return ship

def shipPlacement(shipArray, length, letter, grid):
    for i in range(len(grid)):
        if grid[i][0] == shipArray[0][0]:
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

def chkSpot(ship, length, turn):
    if turn == 'human':
        ship = turnToList(ship)
        for i in range(len(gridPlayer1)):
            if gridPlayer1[i][0] == ship[0][0] and gridPlayer1[i][0] == ship[1][0]:
                for j in range(length):
                    if gridPlayer1[i][int(ship[0][1]) + j] in ('A', 'B', 'C', 'D', 'E'):
                        ship = input("These co-ordinates are filled! Enter different co-ordinates: ")
                        return chkSpot(ship, length, turn)
                    else:
                        pass
            elif gridPlayer1[i][0] == ship[0][0] and gridPlayer1[i + length - 1][0] == ship[1][0]:
                for j in range(length):
                    if gridPlayer1[i + j][int(ship[0][1])] in ('A', 'B', 'C', 'D', 'E'):
                        ship = input("These co-ordinates are filled! Enter different co-ordinates: ")
                        return chkSpot(ship, length, turn)
                    else:
                        pass
        return ship
    else:
        ship = turnToList(ship)
        for i in range(len(gridPlayer2)):
            if gridPlayer2[i][0] == ship[0][0] and gridPlayer2[i][0] == ship[1]:
                for j in range(length):
                    if gridPlayer2[i][int(ship[0][1]) + j] in ('A', 'B', 'C', 'D', 'E'):
                        ship = [random.choice(positions), '-', random.choice(letters)]
                        return chkSpot(ship, length, turn)
                    else:
                        pass
            elif gridPlayer2[i][0] == ship[0][0]:
                for j in range(length):
                    if gridPlayer2[i + j][int(ship[0][1])] in ('A', 'B', 'C', 'D', 'E'):
                        ship = [random.choice(positions), '-', random.choice(letters)]
                        return chkSpot(ship, length, turn)
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

def chkSpaces(ship, length, turn):
    if turn == 'human':
        if ship[0][0] == ship[1][0]:
            if int(ship[0][1]) > (11 - length):
                ship = chkSpot(input("There are not enough spots available to fit the ship! Enter different co-ordinates: "))
                return chkSpaces(ship, length, 'human')
        else:
            for i in range(len(letters)):
                if ship[0][0] == letters[i]:
                    try:
                        letters[i + length - 1]
                    except IndexError:
                        ship = chkSpot(input("There are not enough spots available to fit the ship! Enter different co-ordinates: "))
                        return chkSpaces(ship, length, 'human')
        return ship
    else:
        if ship[0][0] == ship[1][0]:
            if int(ship[0][1]) > (11 - length):
                ship[0] = random.choice(positions)
                return chkSpaces(chkSpot(ship, length, 'ai'), length, turn)
        else:
            for i in range(len(letters)):
                if ship[0][0] == letters[i]:
                    try:
                        letters[i + length - 1]
                    except IndexError:
                        ship[0] = random.choice(positions)
                        return chkSpaces(chkSpot(ship, length, 'ai'), length, turn)
        return ship

def chkPositions(attack):
    if attack not in positions:
        attack = input("This is not a valid co-ordinate! Enter different co-ordinate: ")
        return chkPositions(attack)
    else:
        return attack
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
'''
carrier1 = input('Enter co-ordinates from start to finish (Eg. A1-A5) of where you want to place the aircraft carrier (AAAAA): ')
carrier1 = turnToList(carrier1)
shipPlacement(carrier1, 5, 'A', 'human')

batship1 = chkSpot(input('Enter co-ordinates from start to finish (Eg. A1-D1) of where you want to place the battleship (BBBB): '), 4, 'human')
shipPlacement(batship1, 4, 'B', 'human')

cruiser1 = chkSpot(input('Enter co-ordinates from start to finish (Eg. A1-A3) of where you want to place the cruiser (CCC): '), 3, 'human')
shipPlacement(cruiser1, 3, 'C', 'human')

sub1 = chkSpot(input('Enter co-ordinates from start to finish (Eg. D3-F3) of where you want to place the submarine (DDD): '), 3, 'human')
shipPlacement(sub1, 3, 'D', 'human')

destroyer1 = chkSpot(input('Enter co-ordinates from start to finish (Eg. A1-A2) of where you want to place the destroyer (EE): '), 2, 'human')
shipPlacement(destroyer1, 2, 'E', 'human')
displayGrid()
'''
### Processing
## AI - Computer choosing its positions

carrier2 = chkSpot((chkSpaces([random.choice(positions),'-', random.choice(letters)], 5, 'ai')), 5, 'ai')
shipPlacement(carrier2, 5, 'A', gridPlayer2)
displayGrid()

batship2 = chkSpot((chkSpaces([random.choice(positions),'-', random.choice(letters)], 4, 'ai')), 4, 'ai')
shipPlacement(batship2, 4, 'B', gridPlayer2)
displayGrid()

batship3 = chkSpot((chkSpaces((carrier2[0], '-', carrier2[1]), 3, 'ai')), 3, 'ai')
print(batship3)

cruiser2 = chkSpot((chkSpaces([random.choice(positions),'-', random.choice(letters)], 3, 'ai')), 3, 'ai')
shipPlacement(cruiser2, 3, 'C', gridPlayer2)
displayGrid()

sub2 = chkSpot((chkSpaces([random.choice(positions),'-', random.choice(letters)], 3, 'ai')), 3, 'ai')
shipPlacement(sub2, 3, 'D', gridPlayer2)
displayGrid()

destroyer2 = chkSpot((chkSpaces([random.choice(positions),'-', random.choice(letters)], 2, 'ai')), 2, 'ai')
shipPlacement(destroyer2, 2, 'E', gridPlayer2)
displayGrid()

## GAME STARTS HERE
attack = chkPositions(input("Enter co-ordinates to deploy attack: "))



### Outputs
displayGrid()