
import streamlit as st
import json
import random

# Load questions from JSON
def load_questions():
    with open('questions.json', 'r') as file:
        data = json.load(file)
    random.shuffle(data)
    return data

def main():
    st.set_page_config(page_title="Cute Quiz App 💖", layout="centered")
    st.title("🧠 Fun Quiz Game")
    st.subheader("Let's see how smart you are 😉")

    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.qn = 0
        st.session_state.selected = None

    questions = load_questions()

    if st.session_state.qn < len(questions):
        q = questions[st.session_state.qn]
        st.write(f"**Q{st.session_state.qn + 1}:** {q['question']}")
        options = q['options']
        choice = st.radio("Choose one:", options)

        if st.button("Submit Answer"):
            if choice == q['answer']:
                st.success("Correct! 💖")
                st.session_state.score += 1
            else:
                st.error(f"Oops! The right answer was **{q['answer']}**")
            st.session_state.qn += 1
    else:
        st.balloons()
        st.success(f"Quiz Complete! 🎉 Your Score: {st.session_state.score} / {len(questions)}")
        if st.button("Play Again"):
            st.session_state.score = 0
            st.session_state.qn = 0

if __name__ == '__main__':
    main()
