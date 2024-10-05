import pygame
import random
import copy
import time

pygame.init()

WIDTH, HEIGHT = 400, 700  
GRID_SIZE = 4
CELL_SIZE = WIDTH // GRID_SIZE
FONT_SIZE = 40
TIMER_FONT_SIZE = 25
SCORE_FONT_SIZE = 30
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_CELL_COLOR = (205, 193, 180)
CELL_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
TEXT_COLOR = (119, 110, 101)
BUTTON_COLOR = (119, 136, 153)
BUTTON_TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYS2048")
font = pygame.font.Font(None, FONT_SIZE)
score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
timer_font = pygame.font.Font(None, TIMER_FONT_SIZE)

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
score = 0
high_score = 0
move_timer = None  
timer_speed = 3  
speed_levels = [1, 3 ,5, 10, 60]  
current_speed_index = 2  


def reset_game():
    global board, score, move_timer
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    score = 0
    spawnRandTile(force_two=True)
    spawnRandTile(force_two=True)
    move_timer = time.time() 

def spawnRandTile(force_two=False):
    emptySpots = [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE) if board[x][y] == 0]
    if emptySpots:
        xCord, yCord = random.choice(emptySpots)
        board[xCord][yCord] = 2 if force_two or random.random() >= 0.1 else 4

def shift(row):
    newRow = [num for num in row if num != 0]
    newRow += [0] * (GRID_SIZE - len(newRow))
    return newRow

def merge(row):
    global score
    for i in range(GRID_SIZE - 1):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            score += row[i]  
            row[i + 1] = 0
    return row

def moveLeft():
    for i in range(GRID_SIZE):
        board[i] = shift(board[i])
        board[i] = merge(board[i])
        board[i] = shift(board[i])

def moveRight():
    for i in range(GRID_SIZE):
        board[i] = shift(board[i][::-1])
        board[i] = merge(board[i])
        board[i] = shift(board[i])
        board[i] = board[i][::-1]

def moveUp():
    for j in range(GRID_SIZE):
        col = [board[i][j] for i in range(GRID_SIZE)]
        col = shift(col)
        col = merge(col)
        col = shift(col)
        for i in range(GRID_SIZE):
            board[i][j] = col[i]

def moveDown():
    for j in range(GRID_SIZE):
        col = [board[i][j] for i in range(GRID_SIZE)][::-1]
        col = shift(col)
        col = merge(col)
        col = shift(col)
        col = col[::-1]
        for i in range(GRID_SIZE):
            board[i][j] = col[i]

def draw_board():
    global high_score, timer_speed
    screen.fill(BACKGROUND_COLOR)

    score_surface = score_font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_surface, (10, 10))

    high_score_surface = score_font.render(f"High Score: {high_score}", True, TEXT_COLOR)
    screen.blit(high_score_surface, (10, 40))

    time_remaining = max(0, timer_speed - (time.time() - move_timer))  
    timer_surface = timer_font.render(f"Timer: {time_remaining:.1f}s", True, TEXT_COLOR)
    screen.blit(timer_surface, (10, 70)) 

    speed_button_rect = pygame.Rect(WIDTH - 150, 10, 110, 40)
    pygame.draw.rect(screen, BUTTON_COLOR, speed_button_rect)
    speed_button_text = font.render("Speed", True, BUTTON_TEXT_COLOR)
    screen.blit(speed_button_text, (WIDTH - 140, 15))

    speed_surface = timer_font.render(f"Speed: {timer_speed}s", True, TEXT_COLOR)
    screen.blit(speed_surface, (WIDTH - 135, 55))

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = board[i][j]
            cell_color = CELL_COLORS.get(value, EMPTY_CELL_COLOR)
            pygame.draw.rect(screen, cell_color, (j * CELL_SIZE, i * CELL_SIZE + 100, CELL_SIZE, CELL_SIZE)) 
            if value != 0:
                text_surface = font.render(str(value), True, TEXT_COLOR)
                text_rect = text_surface.get_rect(center=(j * CELL_SIZE + CELL_SIZE / 2, i * CELL_SIZE + 100 + CELL_SIZE / 2))
                screen.blit(text_surface, text_rect)

    pygame.display.update()

    return speed_button_rect

def draw_game_over():
    global high_score
    screen.fill(BACKGROUND_COLOR)

    offset = 200  

    game_over_surface = font.render("GAME OVER", True, TEXT_COLOR)
    game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - offset))
    screen.blit(game_over_surface, game_over_rect)

    high_score_surface = font.render(f"High Score: {high_score}", True, TEXT_COLOR)
    high_score_rect = high_score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - offset + 50))
    screen.blit(high_score_surface, high_score_rect)

    final_score_surface = font.render(f"Final Score: {score}", True, TEXT_COLOR)
    final_score_rect = final_score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - offset + 100))
    screen.blit(final_score_surface, final_score_rect)

    retry_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - offset + 160, 150, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, retry_button_rect)

    retry_button_text_surface = font.render("Retry", True, BUTTON_TEXT_COLOR)
    retry_button_text_rect = retry_button_text_surface.get_rect(center=retry_button_rect.center)
    screen.blit(retry_button_text_surface, retry_button_text_rect)

    title_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - offset + 220, 200, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, title_button_rect)

    title_button_text_surface = font.render("Return to Title", True, BUTTON_TEXT_COLOR)
    title_button_text_rect = title_button_text_surface.get_rect(center=title_button_rect.center)
    screen.blit(title_button_text_surface, title_button_text_rect)

    pygame.display.update()
    
    return retry_button_rect, title_button_rect


def boardChanged(old_board, new_board):
    return old_board != new_board

def checkWin():
    for row in board:
        if 2048 in row:
            return True
    return False

def checkLose():
    for row in board:
        if 0 in row:
            return False
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True

def game():
    global high_score, move_timer, timer_speed, current_speed_index
    running = True
    game_over = False
    reset_game()

    while running:
        if game_over:
            retry_button_rect, title_button_rect = draw_game_over()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_button_rect.collidepoint(event.pos):
                        reset_game()
                        game_over = False
                        return "game"
                    elif title_button_rect.collidepoint(event.pos):
                        return "title_screen"

        else:
            speed_button_rect = draw_board()

            if time.time() - move_timer >= timer_speed:
                if any(0 in row for row in board):
                    spawnRandTile()
                else:
                    if checkLose():
                        game_over = True
                move_timer = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    old_board = copy.deepcopy(board)
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        moveLeft()
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        moveRight()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        moveUp()
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        moveDown()
                    elif event.key == pygame.K_r:
                        game_over = True

                    if boardChanged(old_board, board):
                        if any(0 in row for row in board):
                            spawnRandTile()
                        else:
                            if checkLose():
                                game_over = True
                        move_timer = time.time()

                    if score > high_score:
                        high_score = score

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if speed_button_rect.collidepoint(event.pos):
                        current_speed_index = (current_speed_index + 1) % len(speed_levels)
                        timer_speed = speed_levels[current_speed_index]
                        move_timer = time.time()
