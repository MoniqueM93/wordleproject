import pygame
import sys

# 1. Initialization
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wordle Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Game State
grid_size = 5 # 5 letters
attempts = 6

def draw_grid():
    # Draw the empty Wordle grid
    for row in range(attempts):
        for col in range(grid_size):
            rect = pygame.Rect(50 + col * 80, 50 + row * 80, 70, 70)
            pygame.draw.rect(screen, GRAY, rect, 2) # Draw outline

# 2. Main Game Loop
running = True
while running:
    # 3. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 4. Drawing/Rendering
    screen.fill(BLACK)
    draw_grid()
    
    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
