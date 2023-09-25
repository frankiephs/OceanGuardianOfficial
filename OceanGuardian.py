import pygame
import random
import sys
import time

# variables



#print("Hell0")

# Initialize Pygame
pygame.init()

# Constants

# Where the player moves around
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 830

# starting from the very top
TOP_SCREEN = 300


# The screen size
WINDOW_SCREEN_WIDTH = 1280
WINDOW_SCREEN_HEIGHT = 830

# Required score
SCORE = 15




PLAYER_SIZE = 60

ENEMY_SIZE = 30
ENEMY_SPEED = 20
PLAYER_ACCELERATION = 30
TIME_LIMIT = 60  # Time limit in seconds
MESSAGE_DELAY = 7800  # Delay in milliseconds (2 seconds)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0,255,0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_SCREEN_WIDTH, WINDOW_SCREEN_HEIGHT))
pygame.display.set_caption("OceanGuaridan")

# Load font
font = pygame.font.Font(None, 36)
fact_font = pygame.font.Font(None, 15)


# created the player class only its pos
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = pygame.Vector2(0, 0)

    
    # updates and intializes the player attributes
    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.x = max(0, min(self.x, SCREEN_WIDTH - PLAYER_SIZE))
        self.y = max(TOP_SCREEN, min(self.y, SCREEN_HEIGHT - PLAYER_SIZE))
        

    
    
    # draws the player
    def draw(self):
        player = pygame.image.load("fish.png")
        player = pygame.transform.scale(player, (PLAYER_SIZE, PLAYER_SIZE))
        screen.blit(player, (self.x, self.y))



# enemy class
class Enemy:
    
    
    # enemy attributes
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)

        self.direction = direction
    
    
    # decision where the enemy goes or the rubbish
    def move(self):
        if self.direction == 'left':
            self.rect.x += ENEMY_SPEED
        else:
            self.rect.x -= ENEMY_SPEED



    # binder
class Game:
    def __init__(self):
        
        # created a player instance and initialized all the sizes and pos
        self.player = Player(SCREEN_WIDTH // 2 - PLAYER_SIZE // 2, SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2)
        self.enemies = []
        self.enemy_spawn_timer = 0
        self.score = 0
        self.start_time = pygame.time.get_ticks()  # Start time in milliseconds
        
        
        # initialize the starting page
        self.state = "home"
        self.message_timer = 0  # Timer for win/lose message display
        
        self.new_user = True
        
# Add variables to track movement keys
        self.is_w_pressed = False
        self.is_a_pressed = False
        self.is_s_pressed = False
        self.is_d_pressed = False
        
        
        
        
# List of plastic pollution facts
        self.plastic_facts = [
            "Plastic pollution harms marine life and ecosystems worldwide.",
            "Plastic waste in the ocean can take hundreds of years to decompose.",
            "Over 8 million tons of plastic enter the ocean each year.",
            "Plastic pollution affects not only oceans but also rivers and lakes.",
            "Microplastics, tiny plastic particles, are found throughout the marine food web.",
            "Many seabirds and marine animals ingest plastic, mistaking it for food.",
            "Plastic pollution can transport invasive species to new regions.",
            "Efforts to reduce single-use plastics are essential to combat plastic pollution.",
            "Plastic pollution is a major contributor to coral reef degradation.",
            "Plastic waste in the ocean can disrupt the balance of marine ecosystems.",
            "Plastic pollution poses a threat to human health through contaminated seafood.",
            "Plastic debris can entangle and harm marine animals, including turtles and seals."
        ]

        self.displayed_fact = None  # Initialize the displayed_fact attribute
        
        
        
        
        # event runner
        
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                
                # detects for button click
                if self.state == "home" and self.play_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "intro"
                    
                    
                
                    
                elif self.state == "game":
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for enemy in self.enemies:
                        if enemy.rect.collidepoint(mouse_x, mouse_y):
                            target_vector = pygame.Vector2(enemy.rect.centerx - self.player.x, enemy.rect.centery - self.player.y)
                            target_vector.normalize_ip()
                            self.player.velocity = target_vector * PLAYER_ACCELERATION
                            
                else:
                    # change the state to game as default
                    self.state == "game"
                    
                            
            # Detect key presses and releases for movement keys
            
            
            
            
            
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.is_w_pressed = True
                elif event.key == pygame.K_a:
                    self.is_a_pressed = True
                elif event.key == pygame.K_s:
                    self.is_s_pressed = True
                elif event.key == pygame.K_d:
                    self.is_d_pressed = True
            
            
            
            # this returns when it is not clicked to the defaults.
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.is_w_pressed = False
                elif event.key == pygame.K_a:
                    self.is_a_pressed = False
                elif event.key == pygame.K_s:
                    self.is_s_pressed = False
                elif event.key == pygame.K_d:
                    self.is_d_pressed = False
                    
    def update(self):
        if self.state == "game":
            print(self.new_user)
            # Adjust the player's velocity based on key presses
            player_velocity = pygame.Vector2(0, 0)
            if self.is_w_pressed:
                player_velocity.y -= PLAYER_ACCELERATION
            if self.is_a_pressed:
                player_velocity.x -= PLAYER_ACCELERATION
            if self.is_s_pressed:
                player_velocity.y += PLAYER_ACCELERATION
            if self.is_d_pressed:
                player_velocity.x += PLAYER_ACCELERATION
            
            self.player.velocity = player_velocity
            
            self.player.update()
            current_time = pygame.time.get_ticks()
            time_elapsed = (current_time - self.start_time) / 1000  # Convert to seconds
            
        
            if time_elapsed >= TIME_LIMIT or self.score >= SCORE:
                if self.score >= SCORE:
                    self.state = "win"
                    self.new_user = False
                else:
                    self.state = "lose"
                self.player = Player(SCREEN_WIDTH // 2 - PLAYER_SIZE // 2, SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2)
                self.enemies.clear()
                self.message_timer = pygame.time.get_ticks()
                self.new_user = False

            self.enemy_spawn_timer += 1
            if self.enemy_spawn_timer >= 60:
                side = random.choice(['left', 'right'])
                if side == 'left':
                    enemy_x = 0 - ENEMY_SIZE
                    enemy_y = random.randint(TOP_SCREEN, SCREEN_HEIGHT - ENEMY_SIZE)
                else:
                    enemy_x = SCREEN_WIDTH
                    enemy_y = random.randint(TOP_SCREEN, SCREEN_HEIGHT - ENEMY_SIZE)
                new_enemy = Enemy(enemy_x, enemy_y, side)
                self.enemies.append(new_enemy)
                self.enemy_spawn_timer = 0

            for enemy in self.enemies:
                enemy.move()

            for enemy in self.enemies:
                if enemy.rect.colliderect(pygame.Rect(self.player.x, self.player.y, PLAYER_SIZE, PLAYER_SIZE)):
                    self.enemies.remove(enemy)
                    self.score += 1
                    self.player.velocity = pygame.Vector2(0, 0)

    def draw(self):
        
        
        bg_img = pygame.image.load("bg.png")
        bg = pygame.transform.scale(bg_img, (WINDOW_SCREEN_WIDTH, WINDOW_SCREEN_HEIGHT))
        # The all screen fill
        screen.blit(bg, (0,0))
        
        
        
        # home
        if self.state == "home":
            self.play_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 25, 150, 50)
            pygame.draw.rect(screen, RED, self.play_button)
            play_text = font.render("Play", True, WHITE)
            screen.blit(play_text, (self.play_button.centerx - 30, self.play_button.centery - 15))
            
            
            # draws the intro screen
        elif self.state == "intro" and self.new_user == True:
                screen.fill(BLACK)
                
                
                # Top
                obj = font.render("The objective of the game is to collect rubbish in", True, WHITE)
                obj2 = font.render("a specified time, You need to get 15 rubbish to win.", True, WHITE)
                obj3 = font.render("if you lose, the game ends.", True, WHITE)
                Instructions = font.render("Controls: Use the WASD.", True, WHITE)
                
                # Credits
                credits = font.render("Credits:", True, WHITE)
                credits1 = font.render("Frankie: Project manager and Main Programmer", True, WHITE)
                credits2 = font.render("Chien: Debugger and programmer", True, WHITE)
                credits3 = font.render("Manling: Main designer", True, WHITE)
                
                
                # blit
                # Objective
                screen.blit(obj, ((WINDOW_SCREEN_WIDTH // 2) - 250, 200))
                screen.blit(obj2, ((WINDOW_SCREEN_WIDTH // 2) - 250, 230))
                screen.blit(obj3, ((WINDOW_SCREEN_WIDTH // 2) - 250, 260))
                
                screen.blit(Instructions, ((WINDOW_SCREEN_WIDTH // 2) - 100, 320))
                
                # credits
                screen.blit(credits, (10, WINDOW_SCREEN_WIDTH - 620))
                screen.blit(credits1, (10, WINDOW_SCREEN_WIDTH - 590))
                screen.blit(credits2, (10, WINDOW_SCREEN_WIDTH - 560))
                screen.blit(credits3, (10, WINDOW_SCREEN_WIDTH - 530))
                
                pygame.display.flip()
                time.sleep(5)
                self.state = "game"
        
            

            
            
            
        elif self.state == "game":
            self.player.draw()
            for enemy in self.enemies:
       
                
                enemyimg = pygame.image.load("bottle.png")
                enemyimg = pygame.transform.scale(enemyimg,(ENEMY_SIZE,ENEMY_SIZE))
                
                screen.blit(enemyimg,enemy.rect )
                


            score_text = font.render("Score: {}".format(self.score), True, RED)
            screen.blit(score_text, (10, 10))
            time_text = font.render("Time: {:.1f}".format(max(0, TIME_LIMIT - (pygame.time.get_ticks() - self.start_time) / 1000)), True, RED)
            screen.blit(time_text, (10, 50))
        elif self.state == "win":
            win_text = font.render("Congratulations! You won!", True, RED)
            if self.displayed_fact is None:
                self.displayed_fact = random.choice(self.plastic_facts)
                time.sleep(3.5)


            
            fact_text = font.render(self.displayed_fact, True, RED)

            screen.blit(fact_text, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 + 20))
            screen.blit(win_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20))
            if pygame.time.get_ticks() - self.message_timer >= MESSAGE_DELAY:
                self.displayed_fact = None
                self.reset_game()
        elif self.state == "lose":
            lose_text = font.render("Game over! Try again.", True, RED)
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT // 2 - 20))
            if pygame.time.get_ticks() - self.message_timer >= MESSAGE_DELAY:
                self.displayed_fact = None
                self.reset_game()
        else:
            self.state = "game"

        pygame.display.flip()

    def reset_game(self):
        self.state = "home"
        self.score = 0
        self.start_time = pygame.time.get_ticks()

# Initialize the game
game = Game()

# Game loop
while True:
    game.handle_events()
    game.update()
    game.draw()

    pygame.time.Clock().tick(100)

    
    
    
    
    
    """
    The draw is where all the display happens and the screen
    while the updates, updates all the variables, and attributes

    """

