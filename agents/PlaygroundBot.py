

import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
import streamlit as st 

class BasePlaygroundBot():
    """
    A base class representing a playground bot.

    Attributes:
    -----------
    model_name : str
        The name of the model to use. Default is "gpt-4".
    llm : ChatOpenAI
        An instance of the ChatOpenAI class.
    description : str
        A description of the playground bot.

    Methods:
    --------
    ask(question: str) -> str:
        Asks the bot a question or gives it a prompt and returns the bot's response.
    getDescription() -> str:
        Returns the description of the playground bot.
    display(elem, result):
        Displays the bot's response in the specified element.
    """
    def __init__(self,model_name="gpt-4") -> None:
        """
        Initializes a new instance of the BasePlaygroundBot class.

        Parameters:
        -----------
        model_name : str
            The name of the model to use. Default is "gpt-4".
        """
        self.llm = ChatOpenAI(temperature=0, model_name=model_name)
        self.description = "Blank Description"
    def ask(self,question:str)->str:
        """
        Asks the bot a question or gives it a prompt and returns the bot's response.

        Parameters:
        -----------
        question : str
            The prompt or question to ask the bot.

        Returns:
        --------
        str
            The bot's response to the prompt or question.
        """
        pass
    def getDescription(self)->str:
        """
        Returns the description of the playground bot.

        Returns:
        --------
        str
            The description of the playground bot.
        """
        return self.description
    def display(self,elem,result):
        """
        Displays the bot's response in the specified element.

        Parameters:
        -----------
        elem : str
            The element to display the bot's response in.
        result : dict
            A dictionary containing the bot's response.
        """
        elem.write("empty bot")



class PlayGroundGPT4(BasePlaygroundBot):
    """
    A class representing a playground bot that uses the GPT-4 model.

    Attributes:
    -----------
    model_name : str
        The name of the model to use. Default is "gpt-4".
    chain : ConversationChain
        An instance of the ConversationChain class.
    description : str
        A description of the GPT-4 model.

    Methods:
    --------
    ask(prompt: str) -> str:
        Asks the bot a question or gives it a prompt and returns the bot's response.
    display(elem, result):
        Displays the bot's response in the specified element.
    """
    def __init__(self, model_name="gpt-4") -> None:
        """
        Initializes a new instance of the PlayGroundGPT4 class.

        Parameters:
        -----------
        model_name : str
            The name of the model to use. Default is "gpt-4".
        """
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "GPT4 is the latest version of GPT3. It is trained on a larger dataset and has more parameters. It is the most powerful language model in the world."
    
    def ask(self, prompt: str) -> str:
        """
        Asks the bot a question or gives it a prompt and returns the bot's response.

        Parameters:
        -----------
        prompt : str
            The prompt or question to ask the bot.

        Returns:
        --------
        str
            The bot's response to the prompt or question.
        """
        return self.chain(prompt)
    
    def display(self, elem, result):
        """
        Displays the bot's response in the specified element.

        Parameters:
        -----------
        elem : str
            The element to display the bot's response in.
        result : dict
            A dictionary containing the bot's response.
        """
        elem.write(result["response"])


class PlayGroundGPT4ToT(BasePlaygroundBot):
    """
    A class representing a playground bot that uses the Tree of Thought model.

    Attributes:
    -----------
    model_name : str
        The name of the model to use. Default is "gpt-4".
    chain : ConversationChain
        An instance of the ConversationChain class.
    description : str
        A description of the Tree of Thought model.

    Methods:
    --------
    ask(prompt: str) -> str:
        Asks the bot a question or gives it a prompt and returns the bot's response.
    display(elem, result):
        Displays the bot's response in the specified element.
    """
    def __init__(self, model_name="gpt-4") -> None:
        """
        Initializes a new instance of the PlayGroundGPT4ToT class.

        Parameters:
        -----------
        model_name : str
            The name of the model to use. Default is "gpt-4".
        """
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "The Tree of Thought is a conversational AI model developed by Langchain that uses GPT-4 as its underlying language model. It is designed to generate human-like responses to user input and can be used for a variety of applications, including chatbots, virtual assistants, and customer service."
    def ask(self, prompt: str) -> str:
        """
        Asks the bot a question or gives it a prompt and returns the bot's response.

        Parameters:
        -----------
        prompt : str
            The prompt or question to ask the bot.

        Returns:
        --------
        str
            The bot's response to the prompt or question.
        """
        return self.chain(prompt)

    def display(self,elem,result):
        """
        Displays the bot's response in the specified element.

        Parameters:
        -----------
        elem : str
            The element to display the bot's response in.
        result : dict
            A dictionary containing the bot's response.
        """
        elem.write(result["response"])

class PlayGroundGPT4CoT(BasePlaygroundBot):
    """
    A class representing a playground bot that uses the CoT model.

    Attributes:
    -----------
    model_name : str
        The name of the model to use. Default is "gpt-4".
    chain : ConversationChain
        An instance of the ConversationChain class.
    description : str
        A description of the CoT model.

    Methods:
    --------
    ask(prompt: str) -> str:
        Asks the bot a question or gives it a prompt and returns the bot's response.
    display(elem, result):
        Displays the bot's response in the specified element.
    """
    def __init__(self, model_name="gpt-4") -> None:
        """
        Initializes a new instance of the PlayGroundGPT4CoT class.

        Parameters:
        -----------
        model_name : str
            The name of the model to use. Default is "gpt-4".
        """
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "CoT"
    def ask(self, prompt: str) -> str:
        """
        Asks the bot a question or gives it a prompt and returns the bot's response.

        Parameters:
        -----------
        prompt : str
            The prompt or question to ask the bot.

        Returns:
        --------
        str
            The bot's response to the prompt or question.
        """
        return self.chain(prompt)
    def display(self,elem,result):
        """
        Displays the bot's response in the specified element.

        Parameters:
        -----------
        elem : str
            The element to display the bot's response in.
        result : dict
            A dictionary containing the bot's response.
        """
        elem.write(result["response"])

class PlayGroundGPT4CoTChroma(BasePlaygroundBot):
    """
    A class representing a playground bot that uses the CoTChroma model.

    Attributes:
    -----------
    model_name : str
        The name of the model to use. Default is "gpt-4".
    chain : ConversationChain
        An instance of the ConversationChain class.
    description : str
        A description of the CoTChroma model.

    Methods:
    --------
    ask(prompt: str) -> str:
        Asks the bot a question or gives it a prompt and returns the bot's response.
    display(elem, result):
        Displays the bot's response in the specified element.
    """
    def __init__(self, model_name="gpt-4") -> None:
        """
        Initializes a new instance of the PlayGroundGPT4CoTChroma class.

        Parameters:
        -----------
        model_name : str
            The name of the model to use. Default is "gpt-4".
        """
        super().__init__(model_name=model_name)
        self.chain = ConversationChain(llm=self.llm)
        self.description = "CoTChroma"
    def ask(self, prompt: str) -> str:
        """
        Asks the bot a question or gives it a prompt and returns the bot's response.

        Parameters:
        -----------
        prompt : str
            The prompt or question to ask the bot.

        Returns:
        --------
        str
            The bot's response to the prompt or question.
        """
        return self.chain(prompt)
    def display(self,elem,result):
        """
        Displays the bot's response in the specified element.

        Parameters:
        -----------
        elem : str
            The element to display the bot's response in.
        result : dict
            A dictionary containing the bot's response.
        """
        elem.write(result["response"])




