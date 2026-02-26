import random

# Core logic
words = ['PIANO', 'HOUSE', 'BRAIN', 'LIGHT', 'TRACK']
secret_word = random.choice(words)

def print_board(guesses):
    print("\n--- WORDLE ---")
    for word, feedback in guesses:
        print(f"{word} | {feedback}")
    print("--------------")

def get_feedback(guess, secret):
    # Same feedback logic as before
    result = ['[X]'] * 5
    secret_list = list(secret)
    # Check Green
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = '[G]'
            secret_list[i] = None
    # Check Yellow
    for i in range(5):
        if result[i] == '[X]' and guess[i] in secret_list:
            result[i] = '[Y]'
            secret_list[secret_list.index(guess[i])] = None
    return "".join(result)

# Main Loop
guesses = []
for attempt in range(1, 7):
    guess = input(f"Guess {attempt}/6: ").upper()
    if len(guess) != 5:
        print("Invalid length!")
        continue
    
    feedback = get_feedback(guess, secret_word)
    guesses.append((guess, feedback))
    print_board(guesses)
    
    if guess == secret_word:
        print("You win!")
        break
else:
    print(f"Game over! The word was {secret_word}")
