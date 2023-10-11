

import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
import streamlit as st 

class BasePlaygroundBot():
    def __init__(self,model_name="gpt-4") -> None:
        self.llm = ChatOpenAI(temperature=0, model_name=model_name)
        self.description = "Blank Description"
    def ask(self,question:str)->str:
        pass
    def getDescription(self)->str:
        return self.description
    def display(self,elem,result):
        elem.write("empty bot")



class PlayGroundGPT4(BasePlaygroundBot):

    def __init__(self, model_name="gpt-4") -> None:
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "GPT4 is the latest version of GPT3. It is trained on a larger dataset and has more parameters. It is the most powerful language model in the world."
    def ask(self, prompt: str):
        return self.chain(prompt)
    def display(self,elem,result):
        elem.write(result["response"])


class PlayGroundGPT4ToT(BasePlaygroundBot):

    def __init__(self, model_name="gpt-4") -> None:
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "The Tree of Thought is a conversational AI model developed by Langchain that uses GPT-4 as its underlying language model. It is designed to generate human-like responses to user input and can be used for a variety of applications, including chatbots, virtual assistants, and customer service."
    def ask(self, prompt: str) -> str:
        return self.chain(prompt)
class PlayGroundGPT4CoT(BasePlaygroundBot):

    def __init__(self, model_name="gpt-4") -> None:
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "CoT"
    def ask(self, prompt: str) -> str:
        return self.chain(prompt)
class PlayGroundGPT4CoTChroma(BasePlaygroundBot):

    def __init__(self, model_name="gpt-4") -> None:
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "CoTChroma"
    def ask(self, prompt: str) -> str:
        return self.chain(prompt)




