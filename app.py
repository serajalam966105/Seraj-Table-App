import streamlit as st
import math, random
from datetime import date

st.set_page_config(page_title="Seraj Maths Hub", page_icon="♾️")
st.markdown("<style>img{border-radius:50% !important;}</style>", unsafe_allow_html=True)

try:
    st.image("seraj.png", use_container_width=True)
except:
    try:
        st.image("seraj.jpg", use_container_width=True)
    except:
        pass

st.title("Seraj Alam Complete Maths Hub ♾️")

if 'limit' not in st.session_state:
    st.session_state.limit = 100
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'q1' not in st.session_state:
    st.session_state.q1 = random.randint(2,20)
    st.session_state.q2 = random.randint(2,20)

def new_question():
    st.session_state.q1 = random.randint(2,20)
    st.session_state.q2 = random.randint(2,20)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Table", "🔢 Analysis", "🧮 Tools", "🎮 Quiz Game", "✨ Daily Magic"])

with tab1:
    number = st.number_input("Write Any Number", value=19, step=1, key="t1")
    if st.button("Show The Table"):
        st.session_state.limit = 100
    if number:
        for i in range(1, st.session_state.limit + 1):
            st.write(f"{number} x {i} = {number * i}")
        if st.button("Aur +100 Tak ➕"):
            st.session_state.limit += 100
            st.rerun()

with tab2:
    n = st.number_input("Number Daalo", value=19, step=1, key="t2")
    if n:
        c1, c2, c3 = st.columns(3)
        c1.metric("Square", n**2)
        c2.metric("Cube", n**3)
        c3.metric("Root", f"{math.sqrt(n):.2f}")

with tab3:
    st.subheader("1. LCM / HCF")
    a = st.number_input("First Number", value=12, key="a1")
    b = st.number_input("Second Number", value=18, key="b1")
    # safe LCM/HCF
    try:
        lcm_val = math.lcm(int(a), int(b))
    except:
        lcm_val = int(abs(a*b) / math.gcd(int(a), int(b))) if a and b else 0
    hcf_val = math.gcd(int(a), int(b))
    st.success(f"LCM = {lcm_val} | HCF = {hcf_val}")

    st.divider()
    st.subheader("2. Simple + Compound Interest")
    P = st.number_input("Principal", value=1000.0, key="p")
    R = st.number_input("Rate %", value=5.0, key="r")
    T = st.number_input("Time (Years)", value=2.0, key="t")

    SI = (P*R*T)/100
    CI = P * (pow((1 + R/100), T) - 1)

    st.write(f"**Simple Interest = {SI:.2f}** | Total = {P+SI:.2f}")
    st.write(f"**Compound Interest = {CI:.2f}** | Total = {P+CI:.2f}")

with tab4:
    st.subheader("🎯 Maths Brain Game")
    st.write(f"Score: **{st.session_state.score}**")
    correct_ans = st.session_state.q1 * st.session_state.q2
    st.write(f"**Batao: {st.session_state.q1} x {st.session_state.q2} = ?**")
    ans = st.number_input("Jawab likho", step=1, key="quiz_ans")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Check Karo"):
            if ans == correct_ans:
                st.balloons()
                st.success(f"Sahi! {correct_ans} ✅")
                st.session_state.score += 1
                new_question()
                st.rerun()
            else:
                st.error(f"Galat! Sahi jawab {correct_ans} hai")
    with c2:
        if st.button("Next Question"):
            new_question()
            st.rerun()

with tab5:
    st.subheader("🎂 Advance Age Calculator")
    dob = st.date_input("Apna Birthday Chunno", value=date(2005, 1, 1), key="dob_adv")

    if dob is not None:
        today = date.today()
        now = st.session_state.get("now_time", None)

        # Total din ka hisab
        total_days = (today - dob).days

        # Saal aur Mahina ka sahi hisab
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            # pichle mahine ke din add karo
            if today.month == 1:
                prev_month = 12
                prev_year = today.year - 1
            else:
                prev_month = today.month - 1
                prev_year = today.year
            # mahine ke din
            import calendar
            days += calendar.monthrange(prev_year, prev_month)[1]

        if months < 0:
            years -= 1
            months += 12

        total_hours = total_days * 24
        total_minutes = total_hours * 60
        total_seconds = total_minutes * 60

        st.success(f"🎉 Aap **{years} Years** ke ho gaye ho!")

        st.write("### 📅 Line by Line Details:")
        st.write(f"✅ **Saal (Years):** {years} saal")
        st.write(f"✅ **Mahine (Months):** {years*12 + months} mahine (Total) | {months} mahine is saal me")
        st.write(f"✅ **Din (Days):** {total_days} din total jiye ho")
        st.write(f"✅ **Ghante (Hours):** {total_hours:,} ghante")
        st.write(f"✅ **Minute:** {total_minutes:,} minutes")
        st.write(f"✅ **Second:** {total_seconds:,} seconds")

        st.divider()
        st.info(f"📝 Matlab aap **{dob.strftime('%d-%m-%Y')}** ko paida hue the, aur aaj **{today.strftime('%d-%m-%Y')}** tak aapne **{total_days} din** ka safar tay kar liya hai!")
