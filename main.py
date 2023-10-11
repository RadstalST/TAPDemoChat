import streamlit as st
from streamlit_chat import message
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory,
    ConversationBufferWindowMemory,
)
<<<<<<< HEAD

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
        
def show_main_page():
    with mainSection:
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

        # # Setting page title and header
        # st.set_page_config(page_title="Health care assistance", page_icon=":robot_face:")
        # st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)

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

            # Check for medical keywords and set the system role accordingly
            medical_keywords = ['headache', 'pain', 'doctor', 'medical']
            if any(keyword in userInput.lower() for keyword in medical_keywords):
                system_role = 'doctor' 
            
            if system_role:
                userInput = f"{system_role}: {userInput}"

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

def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(userName, password):
    if userName == "sara" and password =="sara123":
        st.session_state['loggedIn'] = True
    else:
         st.session_state['loggedIn'] = False;
         st.error("Invalid user name or password")
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))


with headerSection:
    #st.set_page_config(page_title="Health care assistance", page_icon=":robot_face:")

    st.title("Health care assistance")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()  
        else:
            show_login_page()
=======
import os
import datetime 

os.environ["OPENAI_API_KEY"] = "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"

# Store session of conversation history with chatbot
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None

# Keep track of chat messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Store API key session
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ''

# Store conversation history
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

# Function to get the chatbot response
def getresponse(userInput, api_key, system_role=None):
    if st.session_state['conversation'] is None:
        llm = OpenAI(
            temperature=0,  # You can adjust this temperature if needed
            openai_api_key=api_key,
            model_name='gpt-3.5-turbo'
        )

        st.session_state['conversation'] = ConversationChain(
            llm=llm,
            verbose=True,
            memory=ConversationBufferWindowMemory(llm=llm, k=10)
        )
    
    # getting current date and time and storing it in session
    current_time = datetime.datetime.now().strftime("%b %d %I:%M %p")
    user_input_date_time = f"{current_time} - {userInput}" # adding date and time on user input prompt
    response = st.session_state['conversation'].predict(input=user_input_date_time)
    st.session_state['conversation_history'].append((user_input_date_time, response))

    # Looking at history in the console
    print("Conversation History:")
    for user_input, model_response in st.session_state['conversation_history']:
        print(f"User: {user_input}")

    return response

# Function to start a new chat
def start_new_chat():
    if 'messages' in st.session_state:
        st.session_state['messages'] = []  # Clear chat messages
    # Sidebar to display conversation history

# Setting page title and header
st.set_page_config(page_title="Healthcare Assistance", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)

# Add a "New Chat" button to the sidebar
st.sidebar.button("New Chat", on_click=start_new_chat)

# showing history on siderbar
st.sidebar.subheader("Conversation History")
for i, (user_input, model_response) in enumerate(st.session_state['conversation_history']):
    #st.sidebar.markdown(f"**User {i + 1}:** {user_input}")
    st.sidebar.markdown(f"{user_input}")

tasktype_option = st.selectbox(
    'Please select the action to be performed?',
    ('summary', 'speech to text', 'embedding'), key=1)

response_container = st.container()  # for displaying response
container = st.container()  # for user input

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
>>>>>>> origin/binod
