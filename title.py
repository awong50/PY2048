import pygame
import game

WIDTH, HEIGHT = 400, 500  
TITLE_FONT_SIZE = 60
BUTTON_FONT_SIZE = 40
BACKGROUND_COLOR = (187, 173, 160)
BUTTON_COLOR = (119, 136, 153)
BUTTON_TEXT_COLOR = (255, 255, 255)
TEXT_COLOR = (119, 110, 101)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PY2048")
title_font = pygame.font.Font(None, TITLE_FONT_SIZE)
button_font = pygame.font.Font(None, BUTTON_FONT_SIZE)

def draw_title_screen():
    screen.fill(BACKGROUND_COLOR)

    title_surface = title_font.render("PY2048", True, TEXT_COLOR)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(title_surface, title_rect)

    instructions_surface = button_font.render("Press Start to Play", True, TEXT_COLOR)
    instructions_rect = instructions_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(instructions_surface, instructions_rect)

    start_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, start_button_rect)
    start_button_surface = button_font.render("Start", True, BUTTON_TEXT_COLOR)
    start_button_text_rect = start_button_surface.get_rect(center=start_button_rect.center)
    screen.blit(start_button_surface, start_button_text_rect)

    instructions_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, instructions_button_rect)
    instructions_button_surface = button_font.render("How to Play", True, BUTTON_TEXT_COLOR)
    instructions_button_text_rect = instructions_button_surface.get_rect(center=instructions_button_rect.center)
    screen.blit(instructions_button_surface, instructions_button_text_rect)

    pygame.display.update()

    return start_button_rect, instructions_button_rect

def title_screen():
    running = True
    while running:
        start_button_rect, instructions_button_rect = draw_title_screen()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    running = False 
                    return  "game"
                elif instructions_button_rect.collidepoint(event.pos):
                    running = False
                    return "instructions" 

