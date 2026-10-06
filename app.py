import streamlit as st
st.image("seraj.jpg",width=200)
st.title("🏫Table by Seraj Alam👍")
n = st.number_input("Table Number", value=2)
m = st.number_input("Kitne tak", value=10)
if st.button("Show"):
    for i in range(1, int(m)+1):
        st.write(n, "x", i, "=", n*i)
