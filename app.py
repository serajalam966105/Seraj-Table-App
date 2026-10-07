import streamlit as st

# Page setting
st.set_page_config(page_title="Seraj AI Table App", page_icon="🤖")

# Tumhari photo aur Title
st.image("seraj.jpg", width=250)
st.markdown("<h1 style='color:#FFFF00;text-align: center;'>Table Design By Seraj Alam</h1>", unsafe_allow_html=True)

# --- PART 1: Tumhara Table Wala App ---
st.divider()
st.subheader("📚 Table Generator")

col1, col2 = st.columns(2)
with col1:
    n = st.number_input("Table Number", value=2)
with col2:
    m = st.number_input("Kitne tak", value=10)

if st.button("Click here to show Table"):
    for i in range(1, int(m)+1):
        st.write(f"{int(n)} x {i} = {int(n*i)}")

# --- PART 2: Naya AI Chat Box ---
st.divider()
st.subheader("🤖 Seraj Alam ka AI Assistant")

# Chat history ko yaad rakhne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages dikhao
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Naya message lo
if prompt := st.chat_input("Yaha kuch pucho..."):
    # User ka message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot ka reply - simple AI logic
    prompt_low = prompt.lower()
    if "naam" in prompt_low:
        reply = "Mai Seraj Alam ka AI Assistant hu! Khagaria se."
    elif "table" in prompt_low:
        reply = "Upar Table Number daalo aur 'Click here to show' dabao, table aa jayega."
    elif "course" in prompt_low or "kya karte" in prompt_low:
        reply = "Seraj Python, Streamlit aur Web Development sikh rahe hai."
    elif "hello" in prompt_low or "hi" in prompt_low:
        reply = "Hello ji! Batao kya help chahiye?"
    else:
        reply = f"Tumne pucha: '{prompt}'. Ye bahut acha sawal hai! Abhi mai simple mode pe hu, jald hi full AI ban jaunga."

    with st.chat_message("assistant"):
        st.markdown(reply)
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
