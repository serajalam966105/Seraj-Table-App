import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Siraj AI Bot")

prompt = st.chat_input("Kuch likho...")
if prompt:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    st.write(response.text)
