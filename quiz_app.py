import streamlit as st
import json

# Load questions from JSON
def load_questions():
    with open("questions.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data

# Main app
def main():
    st.set_page_config(page_title="💡 Quiz App", layout="centered")
    st.title("🧠 Simple Quiz App")
    st.markdown("Test your knowledge one question at a time ✨")

    questions = load_questions()

    # Initialize session state
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.selected = None
        st.session_state.show_result = False

    current_q = questions[st.session_state.q_index]

    # Display current question
    st.subheader(f"Q{st.session_state.q_index + 1}: {current_q['question']}")
    st.session_state.selected = st.radio(
        "Choose an answer:",
        current_q["options"],
        index=0,
        key=st.session_state.q_index
    )

    # Submit button
    if st.button("✅ Submit Answer"):
        st.session_state.show_result = True
        if st.session_state.selected == current_q["answer"]:
            st.success("Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"Oops! Wrong answer. Correct is: {current_q['answer']}")

    # Next button (only after submitting)
    if st.session_state.show_result:
        if st.session_state.q_index < len(questions) - 1:
            if st.button("➡️ Next Question"):
                st.session_state.q_index += 1
                st.session_state.show_result = False
        else:
            st.balloons()
            st.success(f"🎉 Quiz Completed! Your Score: {st.session_state.score} / {len(questions)}")

if __name__ == "__main__":
    main()
