## EXAMPLE OF STATIC PROMPTS

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

user_input = st.text_input("What you want to summarize?")
if st.button("SUMMARIZE"):
    model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')
    result = model.invoke(user_input)
    st.write(result.content)
