import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Floor is Lava")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Grid settings
grid_size = 10
square_size = 50

# Player settings
player_pos = [0, 0]
player_radius = square_size // 3  # Radius of the player circle

# Fixed lava positions (example positions)
lava_positions = [
    [2, 3], [4, 5], [1, 8], [7, 2], 
    [9, 6], [3, 1], [6, 4], [5, 9], 
    [8, 0], [2, 4], [5, 1], [4, 9], 
    [8, 6], [0, 7], [4, 8], [5, 8], 
    [0, 1], [8, 8], [0, 6], [1, 4]
]  
# Adjust as needed

# Checkpoint position
checkpoint_pos = [grid_size - 1, grid_size - 1]

# Game loop
clock = pygame.time.Clock()
running = True
game_over = False
win = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    if not game_over and not win:
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 1
        if keys[pygame.K_RIGHT] and player_pos[0] < grid_size - 1:
            player_pos[0] += 1
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= 1
        if keys[pygame.K_DOWN] and player_pos[1] < grid_size - 1:
            player_pos[1] += 1
    
    # Check for collision with lava
    if player_pos in lava_positions:
        game_over = True
        print("Game Over!")
    
    # Check for reaching the checkpoint
    if player_pos == checkpoint_pos:
        win = True
        game_over = True
        print("You Win!")

    # Draw everything
    screen.fill(WHITE)
    
    # Draw the grid
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, BLACK, rect, 1)
    
    # Draw the lava squares if the game is over
    if game_over:
        for lava in lava_positions:
            rect = pygame.Rect(lava[0] * square_size, lava[1] * square_size, square_size, square_size)
            pygame.draw.rect(screen, RED, rect)
        # Display game result message
        if win:
            font = pygame.font.Font(None, 74)
            text = font.render("YOU WIN!", True, BLACK)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        else:
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over!", True, BLACK)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    
    # Draw the checkpoint
    rect = pygame.Rect(checkpoint_pos[0] * square_size, checkpoint_pos[1] * square_size, square_size, square_size)
    pygame.draw.rect(screen, GREEN, rect)
    
    # Draw the player (circle that doesn't fit completely)
    player_center = (player_pos[0] * square_size + square_size // 2, player_pos[1] * square_size + square_size // 2)
    pygame.draw.circle(screen, BLUE, player_center, player_radius)
    
    pygame.display.flip()
    clock.tick(10)
    
    # Add a delay on game over to allow the player to see the revealed lava and game over message
    if game_over:
        pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds)
        running = False  # Exit the loop after the delay

pygame.quit()
sys.exit()
