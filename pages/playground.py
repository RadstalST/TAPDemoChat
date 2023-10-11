import streamlit as st
from langchain.prompts import PromptTemplate
from agents import PlaygroundBot
@st.cache_resource
def playGroundBotSelector(option:str)->PlaygroundBot.BasePlaygroundBot:
    match option:
        case "GPT4":
            return PlaygroundBot.PlayGroundGPT4()
        case "GPT4+ToT":
            return PlaygroundBot.PlayGroundGPT4ToT()
        case "GPT4+CoT":
            return PlaygroundBot.PlayGroundGPT4CoT()
        case "GPT+CoT+Chroma":
            return PlaygroundBot.PlayGroundGPT4CoTChroma()
        case _:
            return PlaygroundBot.BasePlaygroundBot()     



st.header("Welcome to Playground")
st.write("This is a demo of the Med Bot")
st.warning("if you are editing the code in modules, please restart the app or press 'c' (clear resource cache) to see the changes")
questionPane = st.container()
st.divider()
formPane = st.container()
resultContainer = st.container()



if getattr(st.session_state, 'status', None) is None:
    st.session_state['status'] = {}
else:
    st.session_state.status = {}


prompt_template = PromptTemplate.from_template(
                    """'''
                    userInput: {userInput}
                    prompt: {prompt}
                    '''"""
                ) 
generated_prompt = ""
playgroundbot = PlaygroundBot.BasePlaygroundBot() # empty model


with questionPane:
    final_prompt = ""
    with st.container() as form:
        option = st.selectbox("bot option",('GPT4', 'GPT4+ToT', 'GPT4+CoT',"GPT+CoT+Chroma"))

        playgroundbot = playGroundBotSelector(option)
               

        with st.expander("description",expanded=True):
            st.write(playgroundbot.getDescription())
    
        col1, col2 = st.columns(2)
        with col1: 
            st.subheader("User Input")
            userInput = st.text_area(
                "Your input goes here:", 
                placeholder="I have problem with headache today. I worked 10 hours yesterday",
                value="I have problem with headache today. I worked 10 hours yesterday",
                key='input',
                height=300)
        with col2:
            st.subheader("Scenario")
            prompt = st.text_area(
                "Your prompt goes here:", 
                key='prompt', height=300, 
                value="Please provide possible symptom with my problem")
            

        if prompt:
            final_prompt = prompt
        else:
            final_prompt = option
        with st.expander("See Generated Prompt"):
            
            generated_prompt = prompt_template.format(userInput=userInput, prompt=final_prompt)
            
            # st.write(form.__dict__)
with formPane:        
    with st.form("playground_form"):
        st.markdown(generated_prompt)

        submit_button = st.form_submit_button(label='Send')
        if submit_button:
            with st.spinner('Wait for it...'):
                result = playgroundbot.ask(generated_prompt)
            resultContainer.subheader("Bot Response")
            playgroundbot.display(resultContainer,result)

            with resultContainer.expander("debug"):
                st.write(result)




feedback = st.text_area("your feedback:", key='prompt_output', height=50)


