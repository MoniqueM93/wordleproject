import streamlit as st
import random

# --- CONFIGURATION ---
WORDS = ['PIANO', 'HOUSE', 'BRAIN', 'LIGHT', 'TRACK', 'APPLE']

# Initialize session state (this remembers your game variables)
if 'secret_word' not in st.session_state:
    st.session_state.secret_word = random.choice(WORDS)
    st.session_state.guesses = []
    st.session_state.game_over = False

def get_feedback(guess, secret):
    result = ['[X]'] * 5
    secret_list = list(secret)
    # First pass: Greens
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = '[G]'
            secret_list[i] = None
    # Second pass: Yellows
    for i in range(5):
        if result[i] == '[X]' and guess[i] in secret_list:
            result[i] = '[Y]'
            secret_list[secret_list.index(guess[i])] = None
    return "".join(result)

# --- UI LAYER ---
st.title("Wordle Web Clone")

# Show previous guesses
for word, feedback in st.session_state.guesses:
    st.write(f"**{word}** - {feedback}")

# Input field
if not st.session_state.game_over:
    user_guess = st.text_input("Enter your 5-letter guess:", key="guess_input", max_chars=5)
    
    if st.button("Submit Guess"):
        guess = user_guess.upper()
        if len(guess) == 5:
            feedback = get_feedback(guess, st.session_state.secret_word)
            st.session_state.guesses.append((guess, feedback))
            
            if guess == st.session_state.secret_word:
                st.success("You win!")
                st.session_state.game_over = True
            elif len(st.session_state.guesses) >= 6:
                st.error(f"Game Over! The word was {st.session_state.secret_word}")
                st.session_state.game_over = True
            st.rerun() # Refresh to update the board
        else:
            st.warning("Please enter a 5-letter word.")

if st.button("Restart Game"):
    st.session_state.secret_word = random.choice(WORDS)
    st.session_state.guesses = []
    st.session_state.game_over = False
    st.rerun()
