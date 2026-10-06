import streamlit as st
st.title("Table by Seraj")
n = st.number_input("Table Number", value=2)
m = st.number_input("Kitne tak", value=10)
if st.button("Show"):
    for i in range(1, m+1):
        st.write(n, "x", i, "=", n*i)
