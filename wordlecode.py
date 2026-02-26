import pygame
import sys

# 1. Initialize the engine
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My Game Engine")
clock = pygame.time.Clock()

# 2. Main Game Loop
while True:
    # A. Event Handling (Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # B. Update (Logic)
    # This is where you would check if the user guessed the word correctly

    # C. Draw (Rendering)
    screen.fill((0, 0, 0))  # Clear the screen (Black)
    # This is where you would draw the text/guesses
    
    pygame.display.flip()   # Update the display
    clock.tick(60)          # Keep the game running at 60 FPS
