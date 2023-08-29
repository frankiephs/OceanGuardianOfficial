import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame")





class game():
    def __init__(self):
        # bg menu
        self.bg_menu_image

        # bg game
        self.bg_game_image

        # character
        self.character_image
        self.character_x
        self.character_y
        self.character_rect

        # button
        self.button_color
        self.button_image

        # rubbish 

        self.rubbish_character
        self.rubbish_x
        self.rubbish_y
        self.rubbish_rect

        # usernames
        self.username

        



        # high score
        self.scores = []




        






        
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update game logic here

    # Draw game elements here

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
