import streamlit as st
st.set_page_config(page_title="Seraj ka Table App", page_icon="🔥")
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔥 Table Generator by Seraj Alam 🔥</h1>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=700", caption="Padhega Seraj toh Badhega Bihar!")
number = st.number_input("Kaunsa Table Chahiye?", min_value=1, max_value=100, value=2)
if st.button(f"{number} ka Table Dikhao"):
    st.balloons()
    for i in range(1, 11):
        st.write(f"{number} x {i} = {number*i}")
