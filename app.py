import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Seraj AI App", page_icon="🤖")

# Photo aur Title
try:
    st.image("seraj.jpg", width=250)
except:
    pass
st.markdown("<h1 style='color:#FFFF00;text-align:center;'>Table Design By Seraj Alam</h1>", unsafe_allow_html=True)

# API Setup
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Naya model naam
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    st.error(f"API Key ka Error hai: {e}")
    st.stop()

# Table Wala Part
st.divider()
st.subheader("📚 Table Generator")
n = st.number_input("Table Number", value=2)
m = st.number_input("Kitne tak", value=10)
if st.button("Click here to show Table"):
    for i in range(1, int(m)+1):
        st.write(f"{int(n)} x {i} = {int(n*i)}")

# AI Chat Part - Sirf Ek Baar
st.divider()
st.subheader("🤖 Seraj Alam ka AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages dikhana
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Naya Message Lena - Sirf ek hi input
if prompt := st.chat_input("Yaha kuch pucho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            with st.spinner("Soch raha hu..."):
                response = model.generate_content(prompt)
                reply = response.text
                st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error aa gaya: {e} - Shayad API Key galat hai ya limit khatam ho gayi.")
