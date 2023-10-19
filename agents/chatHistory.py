import datetime
import streamlit as st

def add_user_input_to_history(userInput, response):
    current_time = datetime.datetime.now().strftime("%b %d %I:%M %p")
    formatted_time = f"{current_time} - {userInput}"

    st.session_state.conversation_history.append((formatted_time, response))

    return response
