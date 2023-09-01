import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
PLAYER_SIZE = 50
ENEMY_SIZE = 30
ENEMY_SPEED = 3
PLAYER_ACCELERATION = 5
TIME_LIMIT = 50  # Time limit in seconds
MESSAGE_DELAY = 7800  # Delay in milliseconds (2 seconds)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("OceanGuaridan")

# Load font
font = pygame.font.Font(None, 36)
fact_font = pygame.font.Font(None, 15)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = pygame.Vector2(0, 0)

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.x = max(0, min(self.x, SCREEN_WIDTH - PLAYER_SIZE))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - PLAYER_SIZE))

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))

class Enemy:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.direction = direction

    def move(self):
        if self.direction == 'left':
            self.rect.x += ENEMY_SPEED
        else:
            self.rect.x -= ENEMY_SPEED

class Game:
    def __init__(self):
        self.player = Player(SCREEN_WIDTH // 2 - PLAYER_SIZE // 2, SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2)
        self.enemies = []
        self.enemy_spawn_timer = 0
        self.score = 0
        self.start_time = pygame.time.get_ticks()  # Start time in milliseconds
        self.state = "home"
        self.message_timer = 0  # Timer for win/lose message display
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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "home" and self.play_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "game"
                elif self.state == "game":
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for enemy in self.enemies:
                        if enemy.rect.collidepoint(mouse_x, mouse_y):
                            target_vector = pygame.Vector2(enemy.rect.centerx - self.player.x, enemy.rect.centery - self.player.y)
                            target_vector.normalize_ip()
                            self.player.velocity = target_vector * PLAYER_ACCELERATION
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

            if time_elapsed >= TIME_LIMIT or self.score >= 20:
                if self.score >= 20:
                    self.state = "win"
                else:
                    self.state = "lose"
                self.player = Player(SCREEN_WIDTH // 2 - PLAYER_SIZE // 2, SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2)
                self.enemies.clear()
                self.message_timer = pygame.time.get_ticks()

            self.enemy_spawn_timer += 1
            if self.enemy_spawn_timer >= 60:
                side = random.choice(['left', 'right'])
                if side == 'left':
                    enemy_x = 0 - ENEMY_SIZE
                    enemy_y = random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE)
                else:
                    enemy_x = SCREEN_WIDTH
                    enemy_y = random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE)
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
        screen.fill(WHITE)

        if self.state == "home":
            self.play_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 25, 150, 50)
            pygame.draw.rect(screen, RED, self.play_button)
            play_text = font.render("Play", True, WHITE)
            screen.blit(play_text, (self.play_button.centerx - 30, self.play_button.centery - 15))
        elif self.state == "game":
            self.player.draw()
            for enemy in self.enemies:
                pygame.draw.rect(screen, RED, enemy.rect)

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
    pygame.time.Clock().tick(60)