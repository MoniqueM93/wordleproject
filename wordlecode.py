import streamlit as st
import random

st.title("Mini Wordle")

# Initialize game
if 'secret' not in st.session_state:
    st.session_state.secret = "APPLE"
    st.session_state.history = []

# Input area
guess = st.text_input("Enter a 5-letter word:", key="user_input")

if st.button("Submit"):
    if len(guess) != 5:
        st.error("Must be 5 letters!")
    else:
        st.session_state.history.append(guess.upper())

# Display history
st.write("### Guesses:")
for word in st.session_state.history:
    st.write(word)
