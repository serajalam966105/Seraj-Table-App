import streamlit as st
import random
from datetime import date
from gtts import gTTS
from PIL import Image

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
tab1, tab2, tab3, tab4, tab5, tab6,tab7 = st.tabs(["Table", "Analysis", "Habit Tracker", "Quiz Game", "Age Calculator", "🗣️ Speaking Table","📷 Scan Question"])

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
    st.header("🧰 Habit Tracker")
    
    st.subheader("📊 Habit Tracker")
    habit = st.text_input("Apni Habit Likho:", placeholder="Ex: Roz 1 ghanta padhai")
    
    if habit:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        cols = st.columns(7)
        count = 0
        for i, day in enumerate(days):
            with cols[i]:
                if st.checkbox(day, key=day+habit):
                    count += 1
        
        st.progress(count / 7)
        st.success(f"Progress: {count}/7 din pura hua - {habit}")

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
    st.header("🔊 Speaking Table - Learn by Listening")
    st.write("Listen and memorize tables without reading. Just listen to the audio.")
    
    b_num = st.number_input("Which number table do you want to listen?", value=19, key="bolta_num")
    
    if st.button("🔊 Speak The Table"):
        full_text = f"Table of {b_num}. "
        for i in range(1, 11):
            full_text += f"{b_num} times {i} equals {b_num*i}. "
        
        tts = gTTS(text=full_text, lang='en', slow=False)
        tts.save("bolta.mp3")
        st.audio("bolta.mp3", autoplay=True)
        st.success(f"🔊 Now Playing Table of {b_num}")

with tab7:
    st.header("📸 Scan Your Question")
    st.write("Apni copy ka photo lo, mai solve kar dunga.")
    
    photo = st.camera_input("Camera se photo lo")
    upload = st.file_uploader("Ya yahan se upload karo", type=['jpg','png','jpeg'])
    
    final_photo = photo if photo else upload
    
    if final_photo:
        img = Image.open(final_photo)
        st.image(img, width=300)
        st.success("Photo mil gaya!")
        q = st.text_input("Photo me kya likha hai? Jaise: 19*5", key="scan_q")
        if q:
            try:
                ans = eval(q.replace('x','*').replace('X','*'))
                st.success(f"Answer = {ans}")
                
                # English me bolega
                speak_text = f"The answer is {ans}"
                tts = gTTS(text=speak_text, lang='en')
                tts.save("ans.mp3")
                st.audio("ans.mp3", autoplay=True)
            except:
                st.error("Sahi se likho jaise 19*5")

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
    
    # Option select
    unit = st.radio("Height kaise dalna hai?", ["cm me", "Fit + Inch me"], horizontal=True)
    
    wt = st.number_input("Weight (kg)", value=65.00, key="wt")
    
    if unit == "cm me":
        ht = st.number_input("Height (cm)", value=170.00, key="ht")
        height_m = ht / 100
    else:
        c1, c2 = st.columns(2)
        with c1:
            feet = st.number_input("Feet", value=5, min_value=1, key="feet")
        with c2:
            inch = st.number_input("Inch", value=6, min_value=0, max_value=11, key="inch")
        total_inch = feet * 12 + inch
        height_m = total_inch * 0.0254  # inch to meter
        st.write(f"Total Height: {feet} ft {inch} inch = {total_inch} inch")

    bmi = wt / (height_m**2) if height_m > 0 else 0
    
    if bmi > 0:
        if bmi < 18.5:
            status = "Underweight 😟"
            color = "orange"
        elif bmi < 24.9:
            status = "Fit / Normal 😍"
            color = "green"
        elif bmi < 29.9:
            status = "Overweight 😐"
            color = "orange"
        else:
            status = "Obese 😟"
            color = "red"
        
        st.success(f"Your BMI is: {bmi:.2f}")
        st.markdown(f"<h4 style='color:{color};'>Status: {status}</h4>", unsafe_allow_html=True)



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
