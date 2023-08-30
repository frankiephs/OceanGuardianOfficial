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





class Game():
    def __init__(self):

        """
        # bg menu
        self.bg_menu_image

        # bg game
        self.bg_game_image
        """



        # character
        self.character_image = ""
        self.character_color = (255,0,0)
        self.character_x = SCREEN_WIDTH // 2
        self.character_y = SCREEN_HEIGHT // 2
        self.character_width = 50
        self.character_height = 50
        self.character_rect = pygame.Rect(self.character_x, self.character_y, self.character_width, self.character_height)

        
    # archive
    """
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

        
        # time
        self.time = 3000 # ms 


        # high score
        self.scores = []
    """
    def draw(self):
        pygame.draw.rect(screen, self.character_color, self.character_rect)
        pygame.display.flip()


        


game = Game()






        
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)


    game.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
