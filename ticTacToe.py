'''
title: Tic Tac Toe
author: Palaash Kolhe
date created: 2019-04-16
'''

print("Welcome to Tic Tac Toe")
## Subroutines
def printGrid(player, symbol):
    player -= 1
    if player > -1 and player < 3:
        grid[0].insert(index[player][1], symbol)
        grid[0].pop(index[player][1] + 1)
    elif player > 2 and player < 6:
        grid[2].insert(index[player][1], symbol)
        grid[2].pop(index[player][1] + 1)
    else:
        grid[4].insert(index[player][1], symbol)
        grid[4].pop(index[player][1] + 1)
    for i in range(5):
        newGrid = ' '.join(grid[i])
        print(newGrid)

def spotFull(playerInput):
    if playerInput in moves1 or playerInput in moves2:
        playerInput = int(input("This spot is full! Enter another number: "))
        return spotFull(playerInput)
    elif playerInput not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        playerInput = int(input("Please enter a number between 1-9: "))
        return spotFull(playerInput)
    else:
        return playerInput

def checkWinner(playerInput):
    for i in range(len(wins)):
        if playerInput == wins[i]:
            return 1
        elif len(moves1) == 5 and len(moves2) == 4 and playerInput != wins[i]:
            return 2


def winAdder(one, two, three):
    for j in range(9):
        j += 1

        wins.append([j, one, two, three])
        wins.append([one, j, two, three])
        wins.append([one, two, j, three])

## Arrays
index = [[0, 0], [0, 2], [0, 4], [2, 0], [2, 2], [2, 4], [3, 0], [3, 2], [3, 4]]
wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
moves1 = []
moves2 = []
grid = [[' ', '|', ' ', '|', ' '],
        ['----------'],
        [' ', '|', ' ', '|', ' '],
        ['----------'],
        [' ', '|', ' ', '|', ' ']]

## Main Code Starts Here
tryAgain = True

## Win Array Creator
for i in range(8):
    inOne = wins[i][0]
    inTwo = wins[i][1]
    inThree = wins[i][2]
    newList1 = [inOne, inTwo, inThree]
    winAdder(inOne, inTwo, inThree)

    newList2 = [inTwo, inThree, inOne]
    winAdder(inTwo, inThree, inOne)

    newList3 = [inThree, inOne, inTwo]
    winAdder(inThree, inOne, inTwo)

    newList4 = [inOne, inThree, inTwo]
    winAdder(inOne, inThree, inTwo)

    newList5 = [inTwo, inOne, inThree]
    winAdder(inTwo, inOne, inThree)

    newList6 = [inThree, inTwo, inOne]
    winAdder(inThree, inTwo, inOne)

    wins.append(newList1)
    wins.append(newList2)
    wins.append(newList3)
    wins.append(newList4)
    wins.append(newList5)
    wins.append(newList6)


while tryAgain:
    noWin2 = True

    for i in range(4):
        print('Player 1 - ( X )')
        play1 = int(input("Enter position 1-9: "))
        play1 = spotFull(play1)
        moves1.append(play1)
        printGrid(play1, 'X')
        win1 = checkWinner(moves1)

        if win1 == 1:
            print('''''')
            print("Player 1 Wins!")
            noWin2 = False
            break
        elif win1 == 2:
            print('''''')
            print("It's a Tie!")
            noWin2 = False
            break

        print('''''')

        print('Player 2 - ( O )')
        play2 = int(input("Enter position 1-9: "))
        play2 = spotFull(play2)
        moves2.append(play2)
        printGrid(play2, 'O')
        win2 = checkWinner(moves2)

        if win2 == 1:
            print('''''')
            print("Player 2 Wins!")
            noWin2 = False
            break
        elif win2 == 2:
            print('''''')
            print("It's a Tie!")
            noWin2 = False
            break
        print(len(moves1))
        print(len(moves2))

    while noWin2:
        print('Player 1 - ( X )')
        play1 = int(input("Enter position 1-9: "))
        play1 = spotFull(play1)
        moves1.append(play1)
        printGrid(play1, 'X')
        win1 = checkWinner(play1)

        if win1 == 1:
            print('''''')
            print("Player 1 Wins!")
            break
        elif win1 == 2:
            print('''''')
            print("It's a Tie!")
            break
        noWin2 = False

    ## Ask Try Again

    playAgain = input("Would you like to play again? Y/n: ")
    if playAgain in ['Y', 'y', '']:
        tryAgain = True
        moves1 = []
        moves2 = []
        grid = [[' ', '|', ' ', '|', ' '],
                ['----------'],
                [' ', '|', ' ', '|', ' '],
                ['----------'],
                [' ', '|', ' ', '|', ' ']]
    else:
        tryAgain = False









