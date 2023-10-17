import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")
if OPENAI_API_KEY =="":
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

