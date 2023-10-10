import streamlit as st


questionPane = st.container()


def show_question_pane():
    with questionPane:
        with st.form("playground_form"):
            col1, col2 = st.columns(2)
            with col1: 
                userInput = st.text_area("Your question goes here:", key='input', height=100)
            with col2:
                prompt = st.text_area("Your prompt goes here:", key='prompt', height=50)
                prompt2 = st.text_area("Your prompt goes here:", key='prompt2', height=50)

            
            st.write("prompt output" )
            feedback = st.text_area("your feedback:", key='prompt_output', height=50)
            submit_button = st.form_submit_button(label='Send')
            if submit_button:
                st.write(userInput)
                st.write(prompt)
                st.write(prompt2)

show_question_pane()