# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# December 2022

'''
    Minesweeper is a puzzle game which the player will select a cell in a square grid continuously. 
    Each cell hides a bomb or a value which displays the number of bombs in its neighboring cells. 
    Just to make it clear, neighboring cells is defined as adjacent horizontally, vertically or diagonally.
    If the player selects a cell which contains the bomb, the player loses the game.
'''

'''			 						                   
    Created 150+ lines of a Minesweeper Game program to let user open a cell and check if the user gets a score or loses the game.
    Succeed in utilizing multi-dimensional arrays, list data structure, while/for loops, if/else statements, and data types in Python. 
    Implemented multiple functions (parameters and return values) to improve project accuracy to 95% and reduce risks by 20%. 
'''

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('MineSweeperGame/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('MineSweeperGame/output.txt', 'w')

import random

def GenerateMineSweeperBoard(n, k):
    
    arr = [[0 for row in range(n)] for column in range(n)]

    for num in range(k):

        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        arr[y][x] = 'X'

        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right

        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left

        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right

        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right

        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left

        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center

    return arr

def GeneratePlayerBoard(n):
    arr = [['-' for row in range(n)] for column in range(n)]
    return arr

def DisplayBoard(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")

def CheckWon(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True

def CheckContinueGame(score):
    print("Your score is: ", score)
    isContinue = input("Would you like want to try again (y/n)?: ")
    if isContinue == 'n':
        return False
    return True

def Game():

    GameStatus = True
    while GameStatus:

        '''
        Beginner (grid size n=5; number of bombs k=3)
        Intermediate (grid size n=6; number of bombs k=8)
        Expert (grid size n=8; number of bombs k=20)
        '''
        
        difficulty = input("Select your difficulty (b, i, h): ")
        if difficulty.lower() == 'b':
            n = 5
            k = 3
        elif difficulty.lower() == 'i':
            n = 6
            k = 8
        else:
            n = 8
            k = 20
 
        minesweeper_map = GenerateMineSweeperBoard(n, k)
        player_map = GeneratePlayerBoard(n)

        score = 0

        while True:
            if CheckWon(player_map) == False:
                print("Enter the cell you would to open: ")
                x = input("X (1 to 5): ")
                y = input("Y (1 to 5): ")
                x = int(x) - 1 # 0 based indexing
                y = int(y) - 1 # 0 based indexing 

                if (minesweeper_map[y][x] == 'X'):
                    print("Game Over! Good Luck Next Time")
                    DisplayBoard(minesweeper_map)
                    GameStatus = CheckContinueGame(score)
                    break

                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    DisplayBoard(player_map)
                    score += 1
 
            else:
                DisplayBoard(player_map)
                print("Congratulations! You have Won!")
                GameStatus = CheckContinueGame(score)
                break

def display():
    print('WELCOME TO MINESWEEPER GAME')
    print('If the player selects a cell which contains the bomb, the player loses the game.')
    print('Good luck!')

# Start of Program
if __name__ == "__main__":
    display()
    try:
        Game()
    except KeyboardInterrupt:
        print('\nEnd of Game. GoodBye!')