import os

from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
# from
from langchain.prompts import PromptTemplate
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.memory import ConversationSummaryBufferMemory
import streamlit as st

# import logging

from langchain.chat_models import ChatOpenAI
# from langchain.retrievers.multi_query import MultiQueryRetriever

def load_chain(model_name: str ='gpt-4'):
    """
    Load a ConversationChain object with a specified OpenAI language model.

    Args:
        model_name (str): The name of the OpenAI language model to use. Defaults to 'gpt-4'.

    Returns:
        ConversationChain: A ConversationChain object with the specified language model.
    """
    llm = ChatOpenAI(temperature=0, model_name=model_name)
    chain = ConversationChain(llm=llm)
    return chain


class LangAgent:
    """
    A class representing a language agent that can answer questions based on given context.

    Args:
        path (str): The path to the CSV file containing the context and questions.

    Attributes:
        template (str): A string template for the answer prompt.
        QA_CHAIN_PROMPT (PromptTemplate): A PromptTemplate object for the answer prompt.
        vectorstore (Chroma): A Chroma object that stores the vector embeddings of the context documents.

    Methods:
        __init__(self, path: str = None): Initializes the LangAgent object.
    """

    def __init__(self, path: str = "./.datalake/HC_DATA/prepared_generated_data_for_nhs_uk_conversations.csv"):
        self.template = """Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, just say that you don't know, don't try to make up an answer. 
        Use three sentences maximum and keep the answer as concise as possible. 
        Always gives the answer in your own words, do not copy and paste from the context.
        Always give the reference to the source of the answer as links found from the context.
        response in markdown format
        HISTORY:
        {chat_history}
        QUESTION: 
        {question}
        Helpful Answer for a concerned clinic visitor :"""
        self.QA_CHAIN_PROMPT = PromptTemplate.from_template(self.template)
        self.llm = ChatOpenAI(temperature=0)

    
        if "memory" not in st.session_state: # if memory is not initialized
            st.session_state.memory = ConversationSummaryBufferMemory(
            llm=self.llm,
            memory_key='chat_history', return_messages=True, output_key='answer'
            )
            
        self.memory = st.session_state.memory

        if not os.path.exists("./.chroma_db"):
            loader = CSVLoader(file_path=path,csv_args={"quotechar": '"'})
            documents = loader.load_and_split()
            self.vectorstore = Chroma.from_documents(
                documents=documents, 
                embedding=OpenAIEmbeddings(),
                persist_directory="./.chroma_db",
                
                )
        else:
            self.vectorstore = Chroma(embedding_function=OpenAIEmbeddings(),persist_directory="./.chroma_db")

        
    
    def ask(self, input: str):
        # ask with DB
        qa_chain = ConversationalRetrievalChain.from_llm(
            ChatOpenAI(temperature=0),# ok
            retriever=self.vectorstore.as_retriever(), # ok
            condense_question_prompt = self.QA_CHAIN_PROMPT, # ok
            # chain_type_kwargs={"prompt": self.QA_CHAIN_PROMPT,"verbose":True},
            memory=self.memory,
            return_source_documents=True,
            verbose=True,
            )
        result = qa_chain({"question": input})
        return result
    
    def askWithToT(question:str)->dict():
        
        return dict()





