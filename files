import random

# Core game data
words = ['PIANO', 'HOUSE', 'BRAIN', 'LIGHT', 'TRACK']
secretWord = random.choice(words)
max_guesses = 6

print('Welcome to Wordle-style Guessing!')

for attempt in range(1, max_guesses + 1):
    guess = input(f'Attempt {attempt}/{max_guesses}: ').upper()

    # Input Validation
    if len(guess) != 5:
        print('Please enter a 5-letter word.')
        continue
    
    # Check for Win
    if guess == secretWord:
        print(f'Congratulations! You guessed it in {attempt} attempts!')
        break
        
    # Feedback Generation
    feedback = ""
    # We use a list to track which letters in secretWord have been "used" 
    # to handle duplicate letters correctly.
    secret_list = list(secretWord)
    guess_list = list(guess)
    
    # First pass: Check for Greens (Correct position)
    result = ['[X]'] * 5
    for i in range(5):
        if guess_list[i] == secret_list[i]:
            result[i] = '[G]'
            secret_list[i] = None # Mark as used
            
    # Second pass: Check for Yellows (Correct letter, wrong position)
    for i in range(5):
        if result[i] == '[X]' and guess_list[i] in secret_list:
            result[i] = '[Y]'
            secret_list[secret_list.index(guess_list[i])] = None # Mark as used
            
    print('Result:', ''.join(result))

else:
    print(f'Game Over! The word was {secretWord}.')
