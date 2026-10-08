import streamlit as st
import math

st.set_page_config(page_title="Seraj Maths App", page_icon="♾️")

# White background hatane ke liye CSS - circle only
st.markdown("<style>img{border-radius:50% !important;}</style>", unsafe_allow_html=True)

# Photo upar - pehle png try karega, nahi mila to jpg
try:
    st.image("seraj.png", use_container_width=True)
except:
    try:
        st.image("seraj.jpg", use_container_width=True)
    except:
        st.warning("Photo nahi mili - seraj.jpg / seraj.png naam check karo")

st.title("Infinite Table Generator ♾️")

if 'limit' not in st.session_state:
    st.session_state.limit = 100

number = st.number_input("Write Any Number", value=19, step=1)

if st.button("Show The Table"):
    st.session_state.limit = 100

# --- SMART MATHS TOOLKIT (Option 1) ---
if number:
    st.divider()
    st.subheader(f"🔢 Smart Analysis for {number}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Square", f"{number**2}")
    with col2:
        st.metric("Cube", f"{number**3}")
    with col3:
        st.metric("Square Root", f"{math.sqrt(number):.2f}")

    # Even/Odd & Prime Check
    even_odd = "Even" if number % 2 == 0 else "Odd"
    
    def is_prime(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True
    
    prime_status = "Prime ✅" if is_prime(int(number)) else "Not Prime ❌"

    st.info(f"**{number} is {even_odd} | {prime_status}**")

    # Table Section
    st.subheader(f"📊 Table of {number}")
    for i in range(1, st.session_state.limit + 1):
        st.write(f"{number} x {i} = {number * i}")
    
    if st.button("Aur +100 Tak ➕"):
        st.session_state.limit += 100
        st.rerun()
