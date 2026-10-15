import streamlit as st
import random
from datetime import date
from gtts import gTTS

st.set_page_config(page_title="Seraj Alam Complete Maths Hub", page_icon="🧮", layout="wide")

# --- SESSION ---
if "limit" not in st.session_state:
    st.session_state.limit = 10
if "q1" not in st.session_state:
    st.session_state.q1 = 19
    st.session_state.q2 = 2

def new_q():
    st.session_state.q1 = random.randint(2,20)
    st.session_state.q2 = random.randint(2,20)

# --- TITLE ---
st.markdown("<h2 style='text-align:center;'>Seraj Alam Complete Maths Hub</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Your All-in-One Calculator & Learning App</p>", unsafe_allow_html=True)

# --- TOP 6 TABS ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Table", "Analysis", "Tools", "Quiz Game", "Age Calculator", "🗣️ Bolta Table"])

with tab1:
    st.subheader("Write Any Number")
    num = st.number_input(" ", value=19, label_visibility="collapsed", key="main_num")
    if st.button("Show The Table"):
        st.session_state.limit = 10
    for i in range(1, st.session_state.limit+1):
        st.write(f"{num} x {i} = {num*i}")
    if st.button("Aur +10 Tak +"):
        st.session_state.limit += 10
        st.rerun()

with tab2:
    st.header("📊 Analysis")
    st.info(f"{num} ka table {st.session_state.limit} tak. Isme har step me {num} add hota hai.")

with tab3:
    st.header("🧰 Tools")
    st.write("More tools will be added here.")

with tab4:
    st.header("🎮 Quiz Game")
    st.write(f"Q: {st.session_state.q1} x {st.session_state.q2} = ?")
    ans = st.number_input("Your Answer", value=0, key="quiz_ans")
    if st.button("Check Answer"):
        if ans == st.session_state.q1 * st.session_state.q2:
            st.success("Sahi Jawab! 🎉")
            new_q()
        else:
            st.error("Galat, fir try karo!")

with tab5:
    st.header("🎂 Age Calculator")
    dob = st.date_input("Apna DOB Chuno", value=date(2005,1,1))
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"Aapki Age: {age} saal")

with tab6:
    st.header("🗣️ Bolta Table - Sunke Yaad Karo")
    st.write("Bina photo ke sirf awaaz se table yaad karo.")
    b_num = st.number_input("Kis number ka table sunna hai?", value=19, key="bolta_num")
    if st.button("🔊 Bol Ke Sunao"):
        full_text = f"{b_num} ka table. "
        for i in range(1, 11):
            full_text += f"{b_num} guna {i} barabar {b_num*i}. "
        tts = gTTS(text=full_text, lang='hi', slow=False)
        tts.save("bolta.mp3")
        st.audio("bolta.mp3", autoplay=True)
        st.success("Baj raha hai 🔊")

# --- MORE USEFUL TOOLS (Tumhare video wala section) ---
st.markdown("---")
st.markdown("### 🚀 More Useful Tools - For Everyone")

t1, t2, t3, t4, t5, t6 = st.tabs(["Unit Converter", "%Percentage Calculator", "EMI Calculator", "CGPA", "Bill Split", "BMI Index"])

with t1:
    st.markdown("#### All-in-One Unit Converter")
    st.selectbox("What to be Convert?", ["Length (Meter-Feet)"], key="uc1")
    m = st.number_input("Enter Meter", value=1.00, key="m1")
    st.success(f"{m} Meter = {m*3.28:.2f} Feet")

with t2:
    st.markdown("#### %Percentage Calculator")
    price = st.number_input("Price", value=1000.00, key="p1")
    disc = st.number_input("Discount %", value=20.00, key="d1")
    st.success(f"After Discount: {price - price*disc/100:.2f} Rs | Saving: {price*disc/100:.2f} Rs")

with t3:
    st.markdown("#### EMI Calculator Pro")
    loan = st.number_input("Loan Amount (Rs)", value=500000.00, key="loan")
    intr = st.number_input("Interest % (Yearly)", value=10.00, key="intr")
    yrs = st.number_input("Year", value=5, key="yrs")
    r = intr/100/12
    n = yrs*12
    emi = (loan*r*(1+r)**n)/((1+r)**n-1) if r>0 else loan/n
    st.success(f"Monthly EMI: {emi:.2f} Rs")

with t4:
    st.markdown("#### CGPA Calculator")
    cg = st.number_input("CGPA (0-10)", value=8.5, key="cg")
    st.success(f"Percentage: {cg*9.5:.2f}% (x9.5 Formula)")

with t5:
    st.markdown("#### Bill Split Calculator")
    tb = st.number_input("Total Bill Rs", value=1500.00, key="tb")
    np = st.number_input("No of People", value=3, min_value=1, key="np")
    st.success(f"Each Person: {tb/np:.2f} Rs")

with t6:
    st.markdown("#### BMI Index Calculator")
    wt = st.number_input("Weight (kg)", value=65.00, key="wt")
    ht = st.number_input("Height (cm)", value=170.00, key="ht")
    bmi = wt / ((ht/100)**2)
    st.success(f"Your BMI is: {bmi:.2f}")

# --- CONTACT ME (Tumhari photo wala exact code) ---
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>📞 Contact Me</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by Seraj Alam | Gopalganj, Bihar</p>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("💬 WhatsApp", "https://wa.me/917739618329", use_container_width=True)
with c2:
    st.link_button("📷 Instagram", "https://www.instagram.com/thinklikeseraj", use_container_width=True)
with c3:
    st.link_button("📞 Call Me", "tel:+917739618329", use_container_width=True)

# --- ABOUT ME ---
st.markdown("---")
st.markdown("### 👨‍💻 About Me")
st.info("I am **Siraj Alam** from **Gopalganj, Bihar**. I built this useful website so that everyone can easily use it. Features like Tables, Calculator, Needs & more that you can use for Free.")
