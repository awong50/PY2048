import random
import copy

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

def spawnRandTwo():
    emptySpots = [(x, y) for x in range(4) for y in range(4) if board[x][y] == 0]
    if emptySpots:
        xCord, yCord = random.choice(emptySpots)
        board[xCord][yCord] = 2

def shift(row):
    newRow = [num for num in row if num != 0]
    newRow += [0] * (4 - len(newRow))
    return newRow

def merge(row):
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row

def moveLeft():
    for i in range(4):
        board[i] = shift(board[i])
        board[i] = merge(board[i])
        board[i] = shift(board[i])

def moveRight():
    for i in range(4):
        board[i] = shift(board[i][::-1])
        board[i] = merge(board[i])
        board[i] = shift(board[i])
        board[i] = board[i][::-1]

def moveUp():
    for j in range(4):
        col = [board[i][j] for i in range(3)]
        col = shift(col)
        col = merge(col)
        col = shift(col)
        for i in range(4):
            board[i][j] = col[i]

def moveDown():
    for j in range(4):
        col = [board[i][j] for i in range(3)][::-1]
        col = shift(col)
        col = merge(col)
        col = shift(col)
        col = col[::-1]
        for i in range(4):
            board[i][j] = col[i]

def printBoard():
    for row in board:
        print(row)
    print()

def checkWin():
    for row in board:
        if 2048 in row:
            return True
    return False

def checkLose():
    for row in board:
        if 0 in row:
            return False

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1]:
                return False

    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j]:
                return False

    return True


def get_move():
    move = input("Enter your move (up, down, left, right, exit): ").strip().lower()
    while move not in ['up', 'down', 'left', 'right', 'exit']:
        move = input("Invalid move. Please enter 'up', 'down', 'left', or 'right': ").strip().lower()
    return move

def boardChanged(old_board, new_board):
    return old_board != new_board

def game():
    spawnRandTwo()  
    spawnRandTwo()
    printBoard()

    while True:
        if checkWin():
            print("You win! You've reached 2048!")
            break
        
        if checkLose():
            print("Game over! No more valid moves.")
            break

        move = get_move()
        
        old_board = copy.deepcopy(board)
        
        if move == 'left':
            moveLeft()
        elif move == 'right':
            moveRight()
        elif move == 'up':
            moveUp()
        elif move == 'down':
            moveDown()
        elif move == 'exit':
            break
        else:
            print("Invalid move. Try again.")
            continue
        
        if boardChanged(old_board, board):
            spawnRandTwo()  
        
        print("Board after move:")
        printBoard()

game()