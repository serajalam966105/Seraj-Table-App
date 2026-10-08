import streamlit as st
import math

st.set_page_config(page_title="Seraj Maths Hub", page_icon="♾️")
st.markdown("<style>img{border-radius:50% !important;}</style>", unsafe_allow_html=True)

# Photo
try:
    st.image("seraj.png", use_container_width=True)
except:
    try:
        st.image("seraj.jpg", use_container_width=True)
    except:
        pass

st.title("Seraj Complete Maths Hub ♾️")

if 'limit' not in st.session_state:
    st.session_state.limit = 100

# 3 Tabs bana diye - sab kuch ek jagah
tab1, tab2, tab3 = st.tabs(["📊 Table", "🔢 Smart Analysis", "🧮 All Tools"])

with tab1:
    number = st.number_input("Write Any Number", value=19, step=1, key="table_num")
    if st.button("Show The Table"):
        st.session_state.limit = 100
    
    if number:
        st.divider()
        for i in range(1, st.session_state.limit + 1):
            st.write(f"{number} x {i} = {number * i}")
        if st.button("Aur +100 Tak ➕"):
            st.session_state.limit += 100
            st.rerun()

with tab2:
    n = st.number_input("Number Daalo Analysis ke liye", value=19, step=1, key="analysis")
    if n:
        col1, col2, col3 = st.columns(3)
        col1.metric("Square", f"{n**2}")
        col2.metric("Cube", f"{n**3}")
        col3.metric("Square Root", f"{math.sqrt(n):.2f}")

        # Prime + Even/Odd + Factors
        def is_prime(num):
            if num <= 1: return False
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0: return False
            return True

        even_odd = "Even" if n % 2 == 0 else "Odd"
        prime = "Prime ✅" if is_prime(int(n)) else "Not Prime ❌"
        
        st.info(f"{n} -> **{even_odd} | {prime} | Factorial: {math.factorial(n) if n<=20 else 'Too Large'}**")
        
        factors = [i for i in range(1, int(n)+1) if n % i == 0]
        st.write(f"**Factors of {n}:** {factors}")

with tab3:
    st.subheader("Important Maths Tools")
    
    # LCM / HCF
    st.write("**1. LCM / HCF Calculator**")
    c1, c2 = st.columns(2)
    a = c1.number_input("First Number", value=12)
    b = c2.number_input("Second Number", value=18)
    if a and b:
        st.write(f"LCM = {math.lcm(int(a), int(b))} | HCF = {math.gcd(int(a), int(b))}")
    
    st.divider()
    # Percentage
    st.write("**2. Percentage Calculator**")
    p1, p2 = st.columns(2)
    val = p1.number_input("Value", value=80)
    total = p2.number_input("Total", value=100)
    if total != 0:
        st.write(f"{val} is {val/total*100:.2f}% of {total}")

    st.divider()
    # Simple Interest
    st.write("**3. Simple Interest**")
    si1, si2, si3 = st.columns(3)
    P = si1.number_input("Principal", value=1000)
    R = si2.number_input("Rate %", value=5)
    T = si3.number_input("Time (Years)", value=2)
    SI = (P*R*T)/100
    st.success(f"Simple Interest = {SI} | Total Amount = {P+SI}")
