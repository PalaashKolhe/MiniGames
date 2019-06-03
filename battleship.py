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

## Creating array to check for user input
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
positions = []

for i in range(len(letters)):
    for j in range(len(numbers)):
        var = str(letters[i]) + str(numbers[j])
        positions.append(var)

### Inputs
carrier1 = input('Enter co-ordinates of where you want to place the aircraft carrier (AAAAA): ')
batship1 = input('Enter co-ordinates of where you want to place the battleship (BBBB): ')
cruiser1 = input('Enter co-ordinates of where you want to place the cruiser (CCC): ')
sub1 = input('Enter co-ordinates of where you want to place the submarine (DDD): ')
destroyer1 = input('Enter co-ordinates of where you want to place the destroyer (EE): ')

if carrier1 in positions:
    carrier1 = list(carrier1)
    for i in range(len(gridPlayer1)):
        if gridPlayer1[i][0] == carrier1[0]:
            if gridPlayer1[0][i] == carrier1[1]:
                pass


for i in range(len(gridPlayer1)):
    print('|'.join(gridPlayer1[i]))

for i in range(len(gridPlayer2)):
    print('|'.join(gridPlayer2[i]))