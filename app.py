import streamlit as st

st.set_page_config(page_title="Table Generator by Seraj", layout="centered")

# Menu hide
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FFC300;'>🏫 Table <br> Generator by Seraj Alam 🔥</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Consistency Builds Discipline - Seraj Alam</p>", unsafe_allow_html=True)

st.write("### Which Table you Want to know?")

# --- UNLIMITED INPUTS ---
table_no = st.number_input("Enter Table Number (Koi bhi number)", value=2, step=1)
limit = st.number_input("Kitne Tak Chahiye? (Limit)", value=10, min_value=1, max_value=10000, step=5)

if st.button("Click here to Show"):
    st.success(f"{table_no} ka Table - {limit} tak:")
    for i in range(1, limit + 1):
        st.write(f"{table_no} x {i} = {table_no * i}")
