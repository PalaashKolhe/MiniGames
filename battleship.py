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

gridPlayer1Attack = [
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

gridPlayer2Attack = [
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
        for i in range(len(gridPlayer2)):
            if gridPlayer2[i][0] == ship[0][0] and gridPlayer2[i][0] == ship[1][0]:
                for j in range(length):
                    if len(ship[0]) == 2:
                        if gridPlayer2[i][int(ship[0][1]) + j] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                    else:
                        if gridPlayer2[i][10 + j] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                return ship

            elif gridPlayer2[i][0] == ship[0][0] and gridPlayer2[i + length - 1][0] == ship[1][0]:
                for j in range(length):
                    if len(ship[0]) == 2:
                        if gridPlayer2[i + j][int(ship[0][1])] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                    else:
                        if gridPlayer2[i + j][10] in ('A', 'B', 'C', 'D', 'E'):
                            ship = chkCoord(turnToList(input("These co-ordinates are filled! Enter different co-ordinates: ")), length)
                            return chkSpot(ship, length, turn)
                        else:
                            pass
                return ship

def displayGrid1():
    print('''Player 1 -''')
    for i in range(len(gridPlayer1)):
        print(' | '.join(gridPlayer1[i]))

    print('''Attack Grid -''')
    for i in range(len(gridPlayer1Attack)):
        print(' | '.join(gridPlayer1Attack[i]))

def displayGrid2():
    print('''Player 2 -''')
    for i in range(len(gridPlayer2)):
        print(' | '.join(gridPlayer2[i]))

    print('''Attack Grid -''')
    for i in range(len(gridPlayer1Attack)):
        print(' | '.join(gridPlayer2Attack[i]))

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
        pass

def chkPosition(usr):
    if usr not in positions:
        usr = input("Please enter valid co-ordinates: ")
        return chkPosition(usr)
    else:
        return usr

def chk10(coord):
    try:
        coord[2]
        if coord[1] == '1' and coord[2] == '0':
            coord[1] = '10'
            coord.pop(2)
            return coord
    except IndexError:
        return coord

def chkGameplay(coord, turn):
    if turn == 'Player1':
        if ''.join(coord) in usr1Array:
            coord = input("You have already enter this co-ordinate! Enter a different co-ordinate: ")
            return chkGameplay(coord, turn)
        else:
            return coord
    else:
        if ''.join(coord) in usr2Array:
            coord = input("You have already enter this co-ordinate! Enter a different co-ordinate: ")
            return chkGameplay(coord, turn)
        else:
            return coord

def startMenu():
    print('''
Welcome to Battleship, a game of strategy and luck. Both of the players will create a password to prevent the other player from peeking at their ship placement.
You will see two grids per player. The first grid is where you see your ship placement and where the other player will shoot at.
The second grid is where you will see what co-ordinates you have attacked.  
''')

def rules():
    print('''
1. The players choose where to place their ships based on prompts from the program from the grid.
2. The players then call out positions / co-ordinates on the grid in hopes of hitting the other players ships.
3. The first player to sink all of the other player's ships wins!
''')

def chkRules(usr):
    if usr in ('Y', 'y', ''):
        rules()
    elif usr in ('N', 'n'):
        pass
    else:
        usr = input("Enter Y or N: ")
        return chkRules(usr)

## Creating array to check for user input
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
positions = []

for i in range(len(letters)):
    for j in range(len(numbers)):
        var = str(letters[i]) + str(numbers[j])
        positions.append(var)

### MAIN CODE STARTS HERE ###
startMenu()

### Inputs
chkRules(input("Would you like to read the rules? Y/n: "))

print('''''')
displayGrid1()
print('''
You will choose your positions / co-ordinates from the grid above. 
''')

print('''Player 2 turn around now!
''')
usr1Password = input("(Player 1) Enter your password: ")

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

print('''
Here are where you have placed your ships - 
''')
displayGrid1()

printLines = input("Press any key when you are done looking at your ship placement: ")

for i in range(100):
    print('''
    ''')

## USER 2
print('''''')
displayGrid2()
print('''
You will choose your positions / co-ordinates from the grid above. 
''')

print('''Player 1 turn around now!
      ''')
usr2Password = input("(Player 2) Enter your password: ")

carrier2 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-A5) of where you want to place the aircraft carrier (AAAAA): ')), 5), 5, 'human'), 5, 'player2')
shipPlacement(carrier1, 5, 'A', gridPlayer2)

batship2 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-D1) of where you want to place the battleship (BBBB): ')), 4), 4, 'human'), 4, 'player2')
shipPlacement(batship1, 4, 'B', gridPlayer2)

cruiser2 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-A3) of where you want to place the cruiser (CCC): ')), 3), 3, 'human'), 3, 'player2')
shipPlacement(cruiser1, 3, 'C', gridPlayer2)

sub2 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. D3-F3) of where you want to place the submarine (DDD): ')), 3), 3, 'human'), 3, 'player2')
shipPlacement(sub1, 3, 'D', gridPlayer2)

destroyer2 = chkSpot(chkSpaces(chkCoord(turnToList(input('Enter co-ordinates from start to finish (Eg. A1-A2) of where you want to place the destroyer (EE): ')), 2), 2, 'human'), 2, 'player2')
shipPlacement(destroyer1, 2, 'E', gridPlayer2)

print('''Here are where you have placed your ships - ''')
displayGrid2()

rulesChoose = input("Press any key when you are done looking at your ship placement: ")

for i in range(100):
    print('''
    ''')

#### GAMEPLAY STARTS HERE ####
usr1Array = []
usr2Array = []

usr1Points = 0
usr2Points = 0

def passwordCheck(password, player):
    if player == 1:
        if password != usr1Password:
            password = ('Wrong Password! Try Again: ')
            return passwordCheck(password, player)
        else:
            return password
    else:
        if password != usr2Password:
            password = ('Wrong Password! Try Again: ')
            return passwordCheck(password, player)
        else:
            return password

while usr1Points < 16 or usr2Points < 16:
    passwordCheck1 = passwordCheck(input("Enter your password player 1: "), 1)

    usr1Move = chkGameplay(chk10(list(chkPosition(input("Attack co-ordinates (Eg. A1): ")))), 'Player1')
    usr1Array.append(''.join(usr1Move))

    for i in range(len(gridPlayer2)): ## Player 1
        if usr1Move[0] == gridPlayer2[i][0]:
            for j in range(len(gridPlayer2[i])):
                if int(usr1Move[1]) == j:
                    if gridPlayer2[i][j] in ('A', 'B', 'C', 'D', 'E'):
                        print('''
                        HITTTTTTTTT
                        ''')
                        usr1Points += 1
                    else:
                        print('''
                        MISS
                        ''')
                    gridPlayer1Attack[i][j] = 'X' ### 'X' for usr attack
                    if gridPlayer2[i][j] in ('A', 'B', 'C', 'D', 'E'):
                        gridPlayer2[i][j] = 'S'
                    else:
                        gridPlayer2[i][j] = 'O' ### 'O' for computers grid being attacked
                    displayGrid1()

    choose = input("Press any key when you are done looking at your ship placement: ")

    for i in range(100):
        print('''
        ''')

    passwordCheck2 = passwordCheck(input("Enter your password player 2: "), 2)

    usr2Move = chkGameplay(chk10(list(chkPosition(input("Attack co-ordinates (Eg. A1): ")))), 'Player2')
    usr2Array.append(''.join(usr2Move))

    for i in range(len(gridPlayer1)): ## Player 2
        if usr2Move[0] == gridPlayer1[i][0]:
            for j in range(len(gridPlayer1[i])):
                if int(usr2Move[1]) == j:
                    if gridPlayer1[i][j] in ('A', 'B', 'C', 'D', 'E'):
                        print('''
                        HITTTTTTTTT
                        ''')
                        usr2Points += 1
                    else:
                        print('''
                        MISS
                        ''')
                    gridPlayer2Attack[i][j] = 'X'
                    if gridPlayer1[i][j] in ('A', 'B', 'C', 'D', 'E'):
                        gridPlayer1[i][j] = 'S'
                    else:
                        gridPlayer1[i][j] = 'O'
                    displayGrid2()

    choose = input("Press any key when you are done looking at your ship placement: ")

    for i in range(100):
        print('''
            ''')

### Outputs

if usr1Points > 16:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")
