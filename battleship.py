'''
title: Battleship
author: Palaash Kolhe
date created: 2019-06-03
'''

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

def shipPlacement(shipArray, length, letter):
    for i in range(len(gridPlayer1)):
        if gridPlayer1[i][0] == shipArray[0][0]:
            if shipArray[0][0] == shipArray[1][0]:
                for j in range(length):
                    gridPlayer1[i][int(shipArray[0][1]) + j] = letter
            else:
                for j in range(length):
                    gridPlayer1[j+1][int(shipArray[0][1])] = letter

## Creating array to check for user input
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
positions = []

for i in range(len(letters)):
    for j in range(len(numbers)):
        var = str(letters[i]) + str(numbers[j])
        positions.append(var)

### Inputs
carrier1 = input('Enter co-ordinates from start to finish (Eg. A1-A5) of where you want to place the aircraft carrier (AAAAA): ')
batship1 = input('Enter co-ordinates from start to finish (Eg. A1-D1) of where you want to place the battleship (BBBB): ')
cruiser1 = input('Enter co-ordinates from start to finish (Eg. A1-A3) of where you want to place the cruiser (CCC): ')
sub1 = input('Enter co-ordinates from start to finish (Eg. D3-F3) of where you want to place the submarine (DDD): ')
destroyer1 = input('Enter co-ordinates from start to finish (Eg. A1-A2) of where you want to place the destroyer (EE): ')

carrier1 = turnToList(carrier1)
batship1 = turnToList(batship1)
cruiser1 = turnToList(cruiser1)
sub1 = turnToList(sub1)
destroyer1 = turnToList(destroyer1)

shipPlacement(carrier1, 5, 'A')
shipPlacement(batship1, 4, 'B')
shipPlacement(cruiser1, 3, 'C')
shipPlacement(sub1, 3, 'D')
shipPlacement(destroyer1, 2, 'E')

print('''''')
for i in range(len(gridPlayer1)):
    print(' | '.join(gridPlayer1[i]))

print('''''')
for i in range(len(gridPlayer2)):
    print(' | '.join(gridPlayer2[i]))