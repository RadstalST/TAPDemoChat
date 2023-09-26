import streamlit as st
from agents import lang,utils
from dotenv import load_dotenv

load_dotenv()
st.title("Med Bot")

st.text("This is a demo of the Med Bot")

st.warning("example: Is there any specific treatment for bronchiolitis?")


@st.cache(allow_output_mutation=True)
def load_lang_agent():
    return lang.LangAgent(path="./.datalake/HC_DATA/prepared_generated_data_for_nhs_uk_conversations.csv")

with st.status("Loading..."):
    st.write("Loading the language agent...")
    lang_agent = load_lang_agent()
    st.write("Initialize chat history")
    if "messages" not in st.session_state:
        st.session_state.messages = []


# @st.cache_data
# def ask(question):
#     response = lang_agent.ask(input=question)
#     return response



def renderAI(response):
    with st.chat_message("assistant"):
        st.markdown(response["answer"])
        # collapse

        # tabReferences, tabDetails, tabExtra = st.tabs(["References", "Details", "Extra"])

        # # with tabDetails:
        # #     # st.json(response)
        # #     st.json(response)

        for i,source in enumerate(response["source_documents"]):
            with st.expander(f"Source #{i+1}",expanded=True if i==0 else False):
                for chat in utils.split_document_chat(source.page_content):
                    role = chat["who"]
                    message = chat["message"]
                    st.markdown(f"**{role.upper()}** {message}")

def renderUser(prompt):
    with st.chat_message("user"):
        st.markdown(prompt)
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    
    if message["role"] == "assistant":
        renderAI(message["content"])
    else:
        renderUser(message["content"])

# React to user input
if prompt := st.chat_input("Hi, I am a bit worried about my blood pressure. How can I tell if I have high blood pressure?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = lang_agent.ask(input=prompt)
    renderAI(response)
    # Display assistant response in chat message container
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    