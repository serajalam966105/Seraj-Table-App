import streamlit as st
import math, random
from datetime import date

st.set_page_config(page_title="Seraj Maths Hub", page_icon="🧮", layout="centered")
st.markdown("<style>img{border-radius:50% !important;}</style>", unsafe_allow_html=True)
try:
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.image("seraj.jpg", width=180)
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
    number = st.number_input("Write Any Number", value=19, step=1)

    if "limit" not in st.session_state or st.session_state.limit > 10:
        st.session_state.limit = 10

    if st.button("Show The Table"):
        st.session_state.limit = 10

    if number:
        for i in range(1, st.session_state.limit + 1):
            st.write(f"{number} x {i} = {number * i}")

        if st.session_state.limit < 50: 
            if st.button("Aur +10 Tak ➕"):
                st.session_state.limit += 10
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
        st.info(f"📝 Means you **{dob.strftime('%d-%m-%Y')}** born on , and today **{today.strftime('%d-%m-%Y')}** you are **{total_days} Days** ka safar tay kar liya hai!")
        import math
st.divider()
st.header("🚀 More Useful Tools - For Everyone❗")

tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["Unit Converter"," %Percentage Calculator", "EMI Calculator", "CGPA", "Bill Split", "BMI Index"])
with tab6:
    st.subheader("📐 All-in-One Unit Converter")
    conv_type = st.selectbox("Kya Convert Karna Hai?", ["Length (Meter-Feet)", "Weight (KG-Gram)", "Temperature (C-F)"])
    if conv_type == "Length (Meter-Feet)":
        m = st.number_input("Meter daalo", value=1.0)
        st.success(f"{m} Meter = {m*3.28084:.2f} Feet")
    elif conv_type == "Weight (KG-Gram)":
        kg = st.number_input("KG daalo", value=1.0)
        st.success(f"{kg} KG = {kg*1000:.0f} Gram | {kg*2.20462:.2f} Pound")
    else:
        c = st.number_input("Celsius daalo", value=0.0)
        st.success(f"{c}°C = {(c*9/5)+32:.2f}°F")

with tab7:
    st.subheader("% Percentage Calculator")
    p_type = st.radio("Select:", ["Kitna % hai?", "Marks % Find", "Discount Find"])
    if p_type == "Kitna % hai?":
        a = st.number_input("Value", value=50.0)
        b = st.number_input("Total", value=200.0)
        if b != 0:
            st.success(f"Result: {(a/b)*100:.2f}%")
    elif p_type == "Marks % Find":
        obtained = st.number_input("Given Number", value=450.0)
        total_m = st.number_input("Total Number", value=500.0)
        if total_m != 0:
            st.success(f"Your Percentage: {(obtained/total_m)*100:.2f}%")
    else:
        price = st.number_input("Price", value=1000.0)
        disc = st.number_input("Discount %", value=20.0)
        st.success(f"After Dicount: {price - (price*disc/100):.2f} Rs. Saving: {price*disc/100:.2f} Rs.")

with tab8:
    st.subheader("🏦 EMI / Loan Calculator")
    loan = st.number_input("Loan Amount (Rs)", value=100000.0)
    rate = st.number_input("Interest % (Salana)", value=10.0)
    years = st.number_input("Saal", value=2.0)
    r = rate / (12*100)
    n = years * 12
    if r > 0:
        emi = loan * r * (1+r)**n / ((1+r)**n - 1)
        st.success(f"Monthly EMI: {emi:.2f} Rs.")
        st.info(f"Total Amount To Be Paid: {emi*n:.2f} Rs. | Total Interest: {emi*n - loan:.2f} Rs.")
    else:
        st.success(f"Monthly EMI: {loan/n:.2f} Rs.")

with tab9:
    st.subheader("🎓 CGPA to Percentage")
    cgpa = st.number_input("CGPA Daalo (0-10)", min_value=0.0, max_value=10.0, value=8.2)
    st.success(f"Percentage (x9.5 Formula): {cgpa*9.5:.2f}%")
    st.info(f"Percentage (x10 Formula): {cgpa*10:.2f}%")
    if cgpa >= 9: st.balloons()

with tab10:
    st.subheader("🧾 Bill Split Calculator")
    total_bill = st.number_input("Total Bill (Rs)", value=1000.0)
    persons = st.number_input("Kitne Log?", min_value=1, value=4)
    st.success(f"Har ek ko dena hai: {total_bill/persons:.2f} Rs.")

with tab11:
    st.subheader("💪 BMI Index Calculator")
    
    weight = st.number_input("Weight (kg) me:", min_value=1.0, value=65.0, key="bmi_w11")
    
    unit = st.radio("Height In?", ["CM me", "Feet-Inch me"], horizontal=True)
    
    height_cm = 0
    if unit == "CM me":
        height_cm = st.number_input("Height (cm) me:", min_value=50.0, value=170.0, key="bmi_h_cm")
    else:
        col1, col2 = st.columns(2)
        with col1:
            feet = st.number_input("Feet:", min_value=1, value=5, key="bmi_feet")
        with col2:
            inch = st.number_input("Inch:", min_value=0, value=7, key="bmi_inch")
        height_cm = (feet * 12 + inch) * 2.54
        st.info(f"Aapki height = {height_cm:.1f} cm")

    if st.button("Find BMI", key="bmi_btn11"):
        height_m = height_cm / 100
        bmi = weight / (height_m * height_m)
        st.success(f"Aapka BMI hai: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("Underweight ho")
        elif bmi < 24.9:
            st.success("Normal hai, Ekdum Mast! 🔥")
            st.balloons()
        elif bmi < 29.9:
            st.warning("Overweight hai")
        else:
            st.error("Obesity hai")



st.markdown("---")
st.markdown("<h3 style='text-align: center;'>📞 Contact Me</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by Seraj Alam | Gopalganj, Bihar</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("📱 WhatsApp", "https://wa.me/917739618329", use_container_width=True)
with col2:
    st.link_button("📷 Instagram", "https://www.instagram.com/thinklikeseraj", use_container_width=True)
with col3:
    st.link_button("📞 Call Me", "tel:+917739618329", use_container_width=True)
