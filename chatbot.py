import streamlit as st
from streamlit_chat import message
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory,
    ConversationBufferWindowMemory,
)

import os
from dotenv import load_dotenv

# load environment variables from .env files
load_dotenv()

# get the key 
api_key = os.environ.get("OPENAI_API_KEY","")

# checking if the api key is set or not
if not api_key:
    st.error("API key is not set. Please set it as an environment variable.")
    st.stop

# store session of converstation history with chatbot
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None

# keeps track of chat messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# store api key session
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ''

# Setting page title and header
st.set_page_config(page_title="Health care assistance", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)

# setting up the siderbar
st.sidebar.title("History")

# for having the different select box option
tasktype_option = st.selectbox(
    'Please select the action to be performed?',
    ('summary', 'speech to text', 'embedding'))


def getresponse(userInput, api_key, system_role=None):
    if st.session_state['conversation'] is None:
        llm = OpenAI(
            temperature=0,  # can adjust the temperature as needed
            openai_api_key=api_key,
            model_name='gpt-3.5-turbo'
        )

        st.session_state['conversation'] = ConversationChain(
            llm=llm,
            verbose=True,
            memory=ConversationSummaryMemory(llm=llm)
        )

    response = st.session_state['conversation'].predict(input=userInput)
    print(st.session_state['conversation'].memory.buffer)

    return response

response_container = st.container() # for displaying response
container = st.container() # for user input

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Your question goes here:", key='input', height=50)
        submit_button = st.form_submit_button(label='Send')

        if submit_button:
            st.session_state['messages'].append(user_input)
            # Specify the system role when calling getresponse
            model_response = getresponse(user_input, st.session_state['API_Key'], system_role='doctor')
            st.session_state['messages'].append(model_response)

            with response_container:
                for i in range(len(st.session_state['messages'])):
                    if (i % 2) == 0:
                        message(st.session_state['messages'][i], is_user=True, key=str(i) + '_user')
                    else:
                        message(st.session_state['messages'][i], key=str(i) + '_AI')

# feedback form
with st.container():
    st.write("---")
    st.header("We would love to hear from you!")
    st.write("##")

    # Refer: https://formsubmit.co/
    feedback_form = """
    <form action="https://formsubmit.co/6d5189f5e008a3398f3c9b2bfee1a576" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Write your feedback here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(feedback_form, unsafe_allow_html=True)

# Use custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style/style.css")