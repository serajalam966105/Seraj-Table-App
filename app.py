import streamlit as st
st.set_page_config(page_title="Seraj ka Table App", page_icon="🔥")
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🏫 Table Generator by Seraj Alam 🔥</h1>", unsafe_allow_html=True)
st.image("seraj.jpg",caption="Consistency Builds Discipline-Seraj Alam")
number = st.number_input("Which Table you Want to know?", min_value=1, max_value=100, value=2)
if st.button(Click here to know"):
    st.balloons()
    for i in range(1, 11):
        st.write(f"{number} x {i} = {number*i}")
