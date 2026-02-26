import pygame
import random
import sys

# --- CONFIGURATION ---
WIDTH, HEIGHT = 500, 600
BG_COLOR = (18, 18, 19)
TILE_OUTLINE = (58, 58, 60)
GREEN = (83, 141, 78)
YELLOW = (181, 159, 59)
GRAY = (58, 58, 60)
WHITE = (255, 255, 255)

# --- GAME DATA ---
WORDS = ['PIANO', 'HOUSE', 'BRAIN', 'LIGHT', 'TRACK', 'APPLE']
SECRET_WORD = random.choice(WORDS)

# --- SETUP ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Python Wordle")
font = pygame.font.SysFont("Arial", 40, bold=True)

# State
guesses = []
current_guess = ""
game_over = False

def get_feedback(guess, secret):
    # Logic: [G]reen, [Y]ellow, [X]Gray
    feedback = []
    secret_list = list(secret)
    # First pass: Greens
    result = ['X'] * 5
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = 'G'
            secret_list[i] = None
    # Second pass: Yellows
    for i in range(5):
        if result[i] == 'X' and guess[i] in secret_list:
            result[i] = 'Y'
            secret_list[secret_list.index(guess[i])] = None
    return result

# --- MAIN LOOP ---
running = True
while running:
    screen.fill(BG_COLOR)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_BACKSPACE:
                current_guess = current_guess[:-1]
            elif event.key == pygame.K_RETURN:
                if len(current_guess) == 5:
                    guesses.append((current_guess, get_feedback(current_guess, SECRET_WORD)))
                    if current_guess == SECRET_WORD or len(guesses) >= 6:
                        game_over = True
                    current_guess = ""
            elif len(current_guess) < 5 and event.unicode.isalpha():
                current_guess += event.unicode.upper()

    # Draw Grid (Previous guesses)
    for row, (word, feedback) in enumerate(guesses):
        for col, letter in enumerate(word):
            color = GREEN if feedback[col] == 'G' else YELLOW if feedback[col] == 'Y' else GRAY
            pygame.draw.rect(screen, color, (50 + col * 80, 50 + row * 80, 70, 70))
            text = font.render(letter, True, WHITE)
            screen.blit(text, (70 + col * 80, 60 + row * 80))

    # Draw Current Guess
    for col in range(5):
        pygame.draw.rect(screen, TILE_OUTLINE, (50 + col * 80, 50 + len(guesses) * 80, 70, 70), 2)
        if col < len(current_guess):
            text = font.render(current_guess[col], True, WHITE)
            screen.blit(text, (70 + col * 80, 60 + len(guesses) * 80))

    pygame.display.flip()

pygame.quit()
sys.exit()
