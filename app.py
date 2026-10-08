import streamlit as st
import math, random
from datetime import date

st.set_page_config(page_title="Seraj Alam 🏫 Maths Hub", page_icon="♾️")
st.markdown("<style>img{border-radius:50% !important;}</style>", unsafe_allow_html=True)

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
if 'score' not in st.session_state:
    st.session_state.score = 0

# Ab 5 Tabs ho gaye
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Table", "🔢 Analysis", "🧮 Tools", "🎮 Quiz Game", "✨ Daily Magic"])

with tab1:
    number = st.number_input("Write Any Number", value=19, step=1, key="table_num")
    if st.button("Show The Table"):
        st.session_state.limit = 100
    if number:
        for i in range(1, st.session_state.limit + 1):
            st.write(f"{number} x {i} = {number * i}")
        if st.button("Aur +100 Tak ➕"):
            st.session_state.limit += 100
            st.rerun()

with tab2:
    n = st.number_input("Number Daalo", value=19, step=1, key="analysis")
    if n:
        c1, c2, c3 = st.columns(3)
        c1.metric("Square", n**2)
        c2.metric("Cube", n**3)
        c3.metric("Root", f"{math.sqrt(n):.2f}")
        def is_prime(num):
            if num <= 1: return False
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0: return False
            return True
        even_odd = "Even" if n % 2 == 0 else "Odd"
        st.info(f"{n} is **{even_odd} | {'Prime ✅' if is_prime(int(n)) else 'Not Prime ❌'}**")
        st.write(f"Factors: {[i for i in range(1, int(n)+1) if n % i == 0]}")

with tab3:
    a = st.number_input("First Number", value=12)
    b = st.number_input("Second Number", value=18)
    st.success(f"LCM = {math.lcm(int(a), int(b))} | HCF = {math.gcd(int(a), int(b))}")
    val = st.number_input("Value", value=80)
    total = st.number_input("Total", value=100)
    if total != 0:
        st.write(f"{val} is {val/total*100:.2f}% of {total}")

with tab4:
    st.subheader("🎯 Maths Brain Game")
    st.write(f"Score: **{st.session_state.score}**")
    num1 = random.randint(2, 20)
    num2 = random.randint(2, 20)
    correct = num1 * num2
    st.write(f"**Batao: {num1} x {num2} = ?**")
    ans = st.number_input("Jawab likho", step=1, key="quiz_ans")
    if st.button("Check Karo"):
        if ans == correct:
            st.balloons()
            st.success("Bilkul Sahi! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"Galat! Sahi jawab {correct} hai")

with tab5:
    st.subheader("Age Calculator 🎂")
    dob = st.date_input("Apna Birthday Chunno", value=date(2010, 1, 1))
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"Tumhari Age hai: **{age} Years**")

    st.divider()
    st.subheader("Number to Words 🔤")
    num_word = st.number_input("Number likho (1-10000)", value=125, step=1)
    # Simple logic
    def num_to_words(n):
        # chota wala logic, inflect ki zarurat nahi
        return f"{n} ko shabdo me likhna abhi beta version me hai: {n}"
    if num_word:
        st.write(f"**In Words:** {num_word} = One Hundred Twenty Five jaise (Full English me jaldi add karenge)")
        st.write(f"**Hindi me:** {num_word} ke liye ye feature next update me")
