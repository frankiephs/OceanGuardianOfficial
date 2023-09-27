import pygame
import random
import sys
import time


# Initialize Pygame
pygame.init()

# sound

collision_sound = pygame.mixer.Sound("sounds/comiendose-el-control-1-81452.mp3")
button_click = pygame.mixer.Sound("sounds/shooting-sound-fx-159024.mp3")
win_sound = pygame.mixer.Sound("sounds/success-fanfare-trumpets-6185.mp3")
lose_sound = pygame.mixer.Sound("sounds/wah-wah-sad-trombone-6347.mp3")

# Ai speeches
objective = pygame.mixer.Sound("sounds/The Objective.mp3")
tomove = pygame.mixer.Sound("sounds/To move.mp3")
doomed = pygame.mixer.Sound("sounds/We're doomed.mp3")
horay = pygame.mixer.Sound("sounds/Horay.mp3")



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

ENEMY_SIZE = 40
ENEMY_SPEED = 30
PLAYER_ACCELERATION = 30
TIME_LIMIT = 70  # Time limit in seconds
MESSAGE_DELAY = 7800  # Delay in milliseconds (2 seconds) * 2
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
    def update(self,right):
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.x = max(0, min(self.x, SCREEN_WIDTH - PLAYER_SIZE))
        self.y = max(TOP_SCREEN, min(self.y, SCREEN_HEIGHT - PLAYER_SIZE))
        self.playerimg = pygame.image.load("images/fish.png")
        self.playerimg2 = pygame.transform.scale(self.playerimg, (PLAYER_SIZE, PLAYER_SIZE))
        self.player = pygame.transform.flip(self.playerimg2, right, False)
    
    
    # draws the player
    def draw(self):
        screen.blit(self.player, (self.x, self.y))



# enemy class
class Enemy:
    
    
    # enemy attributes
    def __init__(self, x, y, direction, enemyimage):
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.direction = direction
        
        
        self.enemyimage = enemyimage
        self.enemyimg = pygame.transform.scale(self.enemyimage,(ENEMY_SIZE,ENEMY_SIZE))
        
        
        
        
        
    
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
        self.right = False
        self.player = Player(SCREEN_WIDTH // 2 - PLAYER_SIZE // 2, SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2)
        self.enemies = []
        
        self.enemy_spawn_timer = 0
        self.score = 0
        self.start_time = pygame.time.get_ticks()  # Start time in milliseconds
        
        
        # initialize the starting page
        self.state = "home"
        self.message_timer = 0  # Timer for win/lose message display
        
        self.new_user = True
        
        
        # music variable
        self.currentmusic = None
        
        
# Add variables to track movement keys
        self.is_w_pressed = False
        self.is_a_pressed = False
        self.is_s_pressed = False
        self.is_d_pressed = False
        
# sound
        self.sound_played = False
        
        
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
                    button_click.play()
                    self.state = "intro"
                
                else:
                    # change the state to game as default
                    self.state == "game"
                    
                            
            # Detect key presses and releases for movement keys
            
            
            
            
                
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.is_w_pressed = True
                elif event.key == pygame.K_a:
                    self.is_a_pressed = True
                    self.right = False
                    
                    
                elif event.key == pygame.K_s:
                    self.is_s_pressed = True
                elif event.key == pygame.K_d:
                    self.is_d_pressed = True
                    self.right = True
                    
                    
                    
            
            
            
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
            
            # turns off the music if it is not a new user anymore
            if pygame.mixer.music.get_busy() == True and self.new_user == False and self.currentmusic == "first":
                pygame.mixer.music.fadeout(500)
                pygame.mixer.music.unload()
            
            if pygame.mixer.music.get_busy() == False:
                # bg music
                pygame.mixer.music.load("sounds/OceanGuardian_Game_now.mp3")
                pygame.mixer.music.play()
                self.currentmusic = "second"
            
            # Adjust the player's velocity based on key presses
            player_velocity = pygame.Vector2(0, 0)
            if self.is_w_pressed:
                player_velocity.y -= PLAYER_ACCELERATION
            if self.is_a_pressed:
                player_velocity.x -= PLAYER_ACCELERATION
                self.right = False
                
                
            if self.is_s_pressed:
                player_velocity.y += PLAYER_ACCELERATION
            if self.is_d_pressed:
                player_velocity.x += PLAYER_ACCELERATION
                self.right = True
                
                
            
            self.player.velocity = player_velocity
            
            self.player.update(self.right)
            current_time = pygame.time.get_ticks()
            time_elapsed = (current_time - self.start_time) / 1000  # Convert to seconds
            
        
            if time_elapsed >= TIME_LIMIT or self.score >= SCORE:
                if self.score >= SCORE:
                    win_sound.play()
                    self.state = "win"
                    self.new_user = False
                else:
                    lose_sound.play()
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
                    
                    
                    
                    # new enemy
                enemy_image_list = ["can.png","bottle.png","bag.png"]
                randomimage = random.choice(enemy_image_list)
                self.new_enemy = Enemy(enemy_x, enemy_y, side,pygame.image.load(f"images/{randomimage}") )
                self.enemies.clear()
                self.enemies.append(self.new_enemy)
                
                
                
                self.enemy_spawn_timer = 0

            for enemy in self.enemies:
                enemy.move()

            for enemy in self.enemies:
                if enemy.rect.colliderect(pygame.Rect(self.player.x, self.player.y, PLAYER_SIZE, PLAYER_SIZE)):
                    self.enemies.remove(enemy)
                    collision_sound.play()
                    self.score += 1
                    
                    self.player.velocity = pygame.Vector2(0, 0)

    def draw(self):
        
        
        bg_img = pygame.image.load("images/bg.png")
        bg = pygame.transform.scale(bg_img, (WINDOW_SCREEN_WIDTH, WINDOW_SCREEN_HEIGHT))
        screen.blit(bg, (0,0))
        
        
        
        # home
        if self.state == "home":
            
            # bg music
            if pygame.mixer.music.get_busy() == False:
                
                pygame.mixer.music.load("sounds/OceanGuardian_TheOcean.mp3")
                pygame.mixer.music.play()
                self.currentmusic = "first"
            
            bg_start_img = pygame.image.load("images/startscreen.png")
            bg_start = pygame.transform.scale(bg_start_img, (WINDOW_SCREEN_WIDTH, WINDOW_SCREEN_HEIGHT))
            screen.blit(bg_start, (0,0))
            
            
            
            
            self.play_button = pygame.Rect(180, 300, 190, 100)
            
            
            
            
            
            # draws the intro screen
        elif self.state == "intro" and self.new_user == True:
            
            # music off

            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.fadeout(500)
                pygame.mixer.music.unload()
            
            screen.fill(BLACK)
            
            bg_load_img = pygame.image.load("images/loadingscreen.png")
            bg_load = pygame.transform.scale(bg_load_img, (WINDOW_SCREEN_WIDTH, WINDOW_SCREEN_HEIGHT))
            screen.blit(bg_load, (0,0))
            
            pygame.display.flip()
            time.sleep(1)
            
            objective.play()
            
            time.sleep(10)
            
            
            tomove.play()
            
            time.sleep(5)
            self.state = "game"
        
            

            
            
            
        elif self.state == "game":
            
            self.player.draw()
            
            
            
            
            
            for enemy in self.enemies:
                
                
                
                
                screen.blit(self.new_enemy.enemyimg,enemy.rect )
                pygame.display.flip()
                

            # score and time text
            
            # score
            font = pygame.font.Font(None, 30)  
            score_text = font.render("Score: {}".format(self.score), True, BLACK)
            screen.blit(score_text, ((WINDOW_SCREEN_WIDTH // 2) + 130, 30))
            
            
            
            # time
            time_text = font.render("Time: {:.1f}".format(max(0, TIME_LIMIT - (pygame.time.get_ticks() - self.start_time) / 1000)), True, BLACK)
            
            screen.blit(time_text, ((WINDOW_SCREEN_WIDTH // 2) + 130, 50))
        
        
        
        
        
        
        elif self.state == "win":
            # bg
            bg_win_img = pygame.image.load("images/winscreen.png")
            bg_win = pygame.transform.scale(bg_win_img, (WINDOW_SCREEN_WIDTH, WINDOW_SCREEN_HEIGHT))
            screen.blit(bg_win, (0,0))
            
            img = pygame.image.load("images/WinNews.png")
            img = pygame.transform.scale(img, ((img.get_width() // 2) - 50 , (img.get_height() // 2)-50))
            screen.blit(img, ((WINDOW_SCREEN_WIDTH // 2) , (WINDOW_SCREEN_HEIGHT // 2) - 200))
            pygame.display.flip()
            
            
            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.fadeout(500)
                pygame.mixer.music.unload()
                self.currentmusic = None
            
            
            
            
            if self.displayed_fact is None:
                self.displayed_fact = random.choice(self.plastic_facts)
                time.sleep(3.5)
                
            
            fact_text = font.render(self.displayed_fact, True, BLACK)

            screen.blit(fact_text, (SCREEN_WIDTH // 2 - 480, 20))
            
            pygame.display.flip()
            
            
            time.sleep(2)
            if not self.sound_played:  
                horay.play()
                self.sound_played = True
            
            time.sleep(10)
            
            
            
            
            if pygame.time.get_ticks() - self.message_timer >= MESSAGE_DELAY:
                self.displayed_fact = None
                self.reset_game()
                self.sound_played = False
        
        
        
        
        # player lose renderer
        
        elif self.state == "lose":
            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.fadeout(500)
                pygame.mixer.music.unload()
                self.currentmusic = None
                
            # Black screen
            bg_lose_img = pygame.image.load("images/losescreen.png")
            bg_lose = pygame.transform.scale(bg_lose_img, (WINDOW_SCREEN_WIDTH, WINDOW_SCREEN_HEIGHT))
            screen.blit(bg_lose, (0,0))
            
            
            
            # setting up end image
            img = pygame.image.load("images/breaking-news.jpg")
            img = pygame.transform.scale(img, ((img.get_width() // 2) -100, (img.get_height() // 2)-100))
            screen.blit(img, ((WINDOW_SCREEN_WIDTH // 2) - 500, (WINDOW_SCREEN_HEIGHT // 2) - 100))
            pygame.display.flip()
            
            
            time.sleep(4.5)
            if not self.sound_played:  
                doomed.play()
                self.sound_played = True
            
            
            
            
            
            if pygame.time.get_ticks() - self.message_timer >= MESSAGE_DELAY:
                self.displayed_fact = None
                self.reset_game()
                self.sound_played = False
        

        
        
        else:
            self.state = "game"

        pygame.display.flip()

    def reset_game(self):
        self.state = "home"
        self.score = 0
        self.start_time = pygame.time.get_ticks()

# Initialize the game
game = Game()


def cmd(state):
    if state == "home":
        game.state = "home"
    if state == "intro":
        game.state = "intro"
    if state == "game":
        game.state = "game"
    if state == "win":
        game.state = "win"
    if state == "lose":
        game.state = "lose"


# Game loop
while True:
    cmd("")
    game.handle_events()
    game.update()
    game.draw()

    pygame.time.Clock().tick(100)

    
    
    
    
    
    """
    The draw is where all the display happens and the screen
    while the updates, updates all the variables, and attributes

    """

