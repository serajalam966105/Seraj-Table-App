import streamlit as st

st.set_page_config(page_title="Seraj Table App", page_icon="♾️")

# Photo upar
try:
   st.markdown("<style>img{border-radius:50%}</style>", unsafe_allow_html=True)
st.image("seraj.png", use_container_width=True)
except:
    st.warning("seraj.jpg load nahi ho raha")

st.title("Infinite Table Generator ♾️")

if 'limit' not in st.session_state:
    st.session_state.limit = 100

number = st.number_input("Write Any Number", value=19, step=1)

if st.button("Show The Table"):
    st.session_state.limit = 100

if number:
    st.divider()
    for i in range(1, st.session_state.limit + 1):
        st.write(f"{number} x {i} = {number * i}")
    
    if st.button("Aur +100 Tak ➕"):
        st.session_state.limit += 100
        st.rerun()
