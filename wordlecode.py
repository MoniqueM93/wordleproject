import streamlit as st
import random

# --- GAME CONFIGURATION ---
WORDS = ['PIANO', 'HOUSE', 'BRAIN', 'LIGHT', 'TRACK']

# Initialize the game state if it doesn't exist
if 'secret_word' not in st.session_state:
    st.session_state.secret_word = random.choice(WORDS)
    st.session_state.history = [] # Stores (guess, feedback)
    st.session_state.game_over = False

def get_feedback(guess, secret):
    # Logic: [G]reen, [Y]ellow, [X]Gray
    result = ['[X]'] * 5
    secret_list = list(secret)
    
    # 1st pass: Greens (Correct position)
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = '[G]'
            secret_list[i] = None 
            
    # 2nd pass: Yellows (Wrong position)
    for i in range(5):
        if result[i] == '[X]' and guess[i] in secret_list:
            result[i] = '[Y]'
            secret_list[secret_list.index(guess[i])] = None
            
    return "".join(result)

st.title("Wordle Web Clone")

# Input field
guess = st.text_input("Enter a 5-letter word:", key="user_input", max_chars=5)

if st.button("Submit") and not st.session_state.game_over:
    if len(guess) != 5:
        st.error("Must be 5 letters!")
    else:
        guess = guess.upper()
        feedback = get_feedback(guess, st.session_state.secret_word)
        st.session_state.history.append((guess, feedback))
        
        # Check Win/Loss
        if guess == st.session_state.secret_word:
            st.success(f"Correct! The word was {st.session_state.secret_word}")
            st.session_state.game_over = True
        elif len(st.session_state.history) >= 6:
            st.error(f"Game Over! The word was {st.session_state.secret_word}")
            st.session_state.game_over = True

# Display history
# --- IMPROVED VISUAL FEEDBACK ---
st.write("### Your Guesses:")

# Helper function to map feedback to colors
def get_color(code):
    if code == 'G': return "#538d4e" # Green
    if code == 'Y': return "#b59f3b" # Yellow
    return "#3a3a3c" # Gray (X)

for word, feedback in st.session_state.history:
    cols = st.columns(5) # Create 5 columns per guess
    for i, col in enumerate(cols):
        # We render a colored box with the letter inside
        color = get_color(feedback[i])
        col.markdown(
            f"""
            <div style="background-color: {color}; color: white; padding: 15px; 
            text-align: center; border-radius: 5px; font-weight: bold; font-size: 20px;">
            {word[i]}
            </div>
            """, unsafe_allow_html=True
        )
