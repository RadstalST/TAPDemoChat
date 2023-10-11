import streamlit as st
from langchain.prompts import PromptTemplate

questionPane = st.container()

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
def show_question_pane():
    with questionPane:
        final_prompt = ""
        with st.container() as form:
            option = st.selectbox("bot option",('GPT4', 'GPT4+ToT', 'GPT4+CoT',"GPT+CoT+Chroma"))
            with st.expander("description"):
                st.write("This is a description")
        
            col1, col2 = st.columns(2)
            with col1: 
                st.subheader("User Input")
                userInput = st.text_area(
                    "Your input goes here:", 
                    placeholder="I have problem with headache today. I worked 10 hours yesterday",
                    key='input',
                    height=400)
            with col2:
                st.subheader("Scenario")
                prompt = st.text_area(
                    "Your prompt goes here:", 
                    key='prompt', height=400, 
                    value="Please provide possible symptom with my problem")
                

            if prompt:
                final_prompt = prompt
            else:
                final_prompt = option
            with st.expander("See Generated Prompt"):
                
                generated_prompt = prompt_template.format(userInput=userInput, prompt=final_prompt)
              
                # st.write(form.__dict__)
                


            

        with st.form("playground_form") as form:
            st.markdown(generated_prompt)

            submit_button = st.form_submit_button(label='Send')
            if submit_button:
                st.write(userInput)
                st.write(prompt)

        feedback = st.text_area("your feedback:", key='prompt_output', height=50)


show_question_pane()