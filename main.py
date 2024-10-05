import pygame
from title import title_screen
from instructions import instruction_screen
import game

def main():
    pygame.init()
    running = True
    current_screen = "title_screen" 

    while running:
        if current_screen == "title_screen":
            next_screen = title_screen()

            if next_screen == "instructions":
                current_screen = "instructions"
            elif next_screen == "game":
                current_screen = "game"
            else:
                running = False 

        elif current_screen == "instructions":
            instruction_screen()
            current_screen = "title_screen" 

        elif current_screen == "game":
            next_screen = game.game()

            if next_screen == "title_screen":
                current_screen = "title_screen"
            elif next_screen == "game":
                current_screen = "game"
            else:
                running = False  

    pygame.quit()

if __name__ == "__main__":
    main()