import streamlit as st

# --- Menu hide karne ka code (jo tumne kiya) ---
st.set_page_config(page_title="Table Generator by Seraj")
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# --- Tumhara Design ---
st.markdown("<h1 style='text-align: center; color: #FFC300;'>🏫 Table <br> Generator by Seraj Alam 🔥</h1>", unsafe_allow_html=True)
st.write("Consistency Builds Discipline-Seraj Alam")

# --- NAYA UNLIMITED LOGIC ---
st.write("### Which Table you Want to know?")

col1, col2 = st.columns(2)

with col1:
    table_no = st.number_input("Table Number", value=2, step=1)

with col2:
    limit = st.number_input("Kitna Tak Chahiye? (Limit)", value=10, min_value=1, max_value=10000, step=1)

if st.button("Click here to Show"):
    st.write(f"### {table_no} ka Table ({limit} tak):")
    for i in range(1, limit+1):
        st.write(f"{table_no} x {i} = {table_no * i}")
