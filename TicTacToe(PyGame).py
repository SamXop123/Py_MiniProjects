import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 10
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Board and game variables
board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
current_player = "X"  # X starts
game_over = False
winner = None

# Font
font = pygame.font.SysFont(None, 40)

# Draw grid lines
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * row), (WIDTH, CELL_SIZE * row), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (CELL_SIZE * row, 0), (CELL_SIZE * row, HEIGHT), LINE_WIDTH)

# Draw X and O
def draw_marks():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == "X":
                pygame.draw.line(screen, RED, (col * CELL_SIZE + 20, row * CELL_SIZE + 20),
                                 ((col + 1) * CELL_SIZE - 20, (row + 1) * CELL_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, RED, ((col + 1) * CELL_SIZE - 20, row * CELL_SIZE + 20),
                                 (col * CELL_SIZE + 20, (row + 1) * CELL_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 20, LINE_WIDTH)

# Check for winner
def check_winner():
    global winner, game_over
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            game_over = True
            return
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            game_over = True
            return
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        game_over = True
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        game_over = True
        return
    if all(all(cell is not None for cell in row) for row in board):
        game_over = True  # Tie game

# Display winner or tie message
def draw_winner():
    if winner:
        text = font.render(f"{winner} wins!", True, RED)
    else:
        text = font.render("It's a tie!", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // CELL_SIZE
            col = x // CELL_SIZE
            if board[row][col] is None:
                board[row][col] = current_player
                
                # Update display to show the latest move before checking winner
                draw_marks()
                pygame.display.update()
                
                check_winner()
                
                # Switch players after the check
                current_player = "O" if current_player == "X" else "X"

    if game_over:
        draw_winner()
        pygame.display.update()
        pygame.time.delay(3000)  # 3 seconds delay before closing
        running = False  # Exit the loop to end the game

    pygame.display.update()

pygame.quit()  # Close the pygame window after exiting the loop
sys.exit()  # Exit the program
