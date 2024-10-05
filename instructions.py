import pygame
import game

WIDTH, HEIGHT = 400, 500  
TITLE_FONT_SIZE = 60
BUTTON_FONT_SIZE = 40
INSTRUCTION_FONT_SIZE = 24
BACKGROUND_COLOR = (187, 173, 160)
BUTTON_COLOR = (119, 136, 153)
BUTTON_TEXT_COLOR = (255, 255, 255)
TEXT_COLOR = (119, 110, 101)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYS2048")
title_font = pygame.font.Font(None, TITLE_FONT_SIZE)
button_font = pygame.font.Font(None, BUTTON_FONT_SIZE)
instruction_font = pygame.font.Font(None, INSTRUCTION_FONT_SIZE)

def draw_instruction_screen():
    screen.fill(BACKGROUND_COLOR)

    title_surface = title_font.render("How to Play", True, TEXT_COLOR)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 100))
    screen.blit(title_surface, title_rect)

    instructions = [
        "Use your arrow keys or WASD to move the tiles.",
        "When two tiles with the same number touch,",
        "they merge into one! When the timer hits 0,", 
        "a random tile is added! Try to reach 2048."
    ]
    
    for i, line in enumerate(instructions):
        instruction_surface = instruction_font.render(line, True, TEXT_COLOR)
        instruction_rect = instruction_surface.get_rect(center=(WIDTH // 2, 200 + i * 30))
        screen.blit(instruction_surface, instruction_rect)

    start_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT - 150, 150, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, start_button_rect)
    
    button_text_surface = button_font.render("Return", True, BUTTON_TEXT_COLOR)
    button_text_rect = button_text_surface.get_rect(center=start_button_rect.center)
    screen.blit(button_text_surface, button_text_rect)

    pygame.display.update()

    return start_button_rect

def instruction_screen():
    running = True
    while running:
        button_rect = draw_instruction_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False  

