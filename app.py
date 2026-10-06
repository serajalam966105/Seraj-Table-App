import streamlit as st

st.set_page_config(page_title="Table Generator by Seraj", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FFC300;'>Table Generator by Seraj Alam</h1>", unsafe_allow_html=True)

table_no = st.number_input("Enter Table Number", value=2, step=1)
limit = st.number_input("Kitne Tak Chahiye?", value=10, min_value=1, max_value=10000, step=1)

if st.button("Click here to know"):
    st.success(f"{table_no} ka Table:")
    for i in range(1, limit + 1):
        st.write(f"{table_no} x {i} = {table_no * i}")
