import random

board = [[0, 0, 0]
         [0, 0, 0]
         [0, 0, 0]]

def spawnRandTwo():
    xCord = random.randint(0, 2)
    yCord = random.randint(0, 2)

    while board[xCord][yCord] != 0:
        xCord = random.randint(0, 2)
        yCord = random.randint(0, 2)
    
    board[xCord][yCord] = 2

