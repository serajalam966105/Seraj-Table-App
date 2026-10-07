import streamlit as st
from google import genai

st.set_page_config(page_title="Seraj AI App", page_icon="🤖")

try:
    st.image("seraj.jpg", width=250)
except:
    pass
st.markdown("<h1 style='color:#FFFF00;text-align:center;'>Table Design By Seraj Alam</h1>", unsafe_allow_html=True)

# NAYA API SETUP
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error(f"API Key Error: {e}")
    st.stop()

st.divider()
st.subheader("📚 Table Generator")
n = st.number_input("Table Number", value=2)
m = st.number_input("Kitne tak", value=10)
if st.button("Click here to show Table"):
    for i in range(1, int(m)+1):
        st.write(f"{int(n)} x {i} = {int(n*i)}")

st.divider()
st.subheader("🤖 Seraj Alam ka AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Yaha kuch pucho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            with st.spinner("Soch raha hu..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
                reply = response.text
                st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error: {e}")
