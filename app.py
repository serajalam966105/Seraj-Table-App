import streamlit as st
st.image("seraj.jpg",width=200)
st.markdown("<h1 style:'color:#DAA520;text-align: center;'>Table Design By Seraj Alam</h1>",unsafe_allow_html=True)
n = st.number_input("Table Number", value=2)
m = st.number_input("Kitne tak", value=10)
if st.button("Click here to show"):
    for i in range(1, int(m)+1):
        st.write(n, "x", i, "=", n*i)
