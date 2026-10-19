import streamlit as st
import random
from datetime import date
from gtts import gTTS
from PIL import Image

st.set_page_config(page_title="Solve With Seraj🎯", page_icon="🧮", layout="wide")
import base64

def circular_photo(image_path, size=150):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <div style="display:flex; justify-content:center; margin-top:10px; margin-bottom:10px;">
            <img src="data:image/jpeg;base64,{encoded}" 
                 style="border-radius:50%; width:{size}px; height:{size}px; object-fit:cover; border:3px solid #4CAF50;">
        </div>
    """, unsafe_allow_html=True)

circular_photo("seraj.jpg", 150)

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
st.markdown("<h2 style='text-align:center;'>Think and Solve With Seraj🎖️👍</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Your All-in-One Calculator & Learning App</p>", unsafe_allow_html=True)

# --- TOP 6 TABS ---
tab1, tab2, tab3, tab4, tab5, tab6,tab7, tab8= st.tabs(["Table", "Analysis", "Habit Tracker", "Quiz Game", "Age Calculator", "🗣️ Speaking Table","📷 Scan Question", "Formula Sheet"])

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

    n = st.number_input("Analysis ke liye number daalo:", value=10, step=1, key="analysis_num")
    
    if st.button("Analyze Karo"):
        st.write(f"### Result for {n}")
        
        # Even / Odd
        if n % 2 == 0:
            st.write(f"**Even Number**")
        else:
            st.write(f"**Odd Number**")

        # Prime Check
        is_prime = True
        if n < 2:
            is_prime = False
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    is_prime = False
                    break
        if is_prime:
            st.success(f"{n} ek **Prime Number**")
        else:
            st.error(f"{n} **Prime Number nahi**")

        # Square, Cube, Roots
        st.write(f"Square: {n**2}")
        st.write(f"Cube: {n**3}")
        st.write(f"Square Root: {n**0.5:.2f}")
        st.write(f"Cube Root: {n**(1/3):.2f}")

with tab3:
    st.header("🧰 Habit Tracker")
    
    st.subheader("📊 Habit Tracker")
    habit = st.text_input("Write Your Habit:", placeholder="Ex: Daily 1 Hour In GYM🏋️")
    
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
            st.error("Wrong, Try Again!")

with tab5:
    st.header("🎂 Age Calculator")
    dob = st.date_input("Choose Your DOB", value=date(2005,1,1))
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"Aapki Age: {age} saal")

with tab6:
    st.header("🔊 Speaking Table - Learn by Listening")
    st.write("Listen and memorize tables without reading. Just listen to the audio.")
    
    b_num = st.number_input("Which number table do you want to listen?", value=19, key="Speak_num")
    
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
    st.write("Scan Your Question, I will Solve.")
    
    photo = st.camera_input("Take photo with your camera")
    upload = st.file_uploader("Or upload from here", type=['jpg','png','jpeg'])
    
    final_photo = photo if photo else upload
    
    if final_photo:
        img = Image.open(final_photo)
        st.image(img, width=300)
        st.success("Photo found!")
        q = st.text_input("What write in photo? Example: 19*5", key="scan_q")
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

with tab8:
    st.header("Formula Sheet - Class 9 & 10")
    st.write("Choose Your Suhject, Every Important Formula given Here")

    subject = st.selectbox("Choose Subject", ["Maths Class 10", "Maths Class 9", "Physics Class 10", "Chemistry Class 10"])

    if subject == "Maths Class 10":
        with st.expander("Algebra"):
            st.latex(r"(a+b)^2 = a^2 + 2ab + b^2")
            st.latex(r"(a-b)^2 = a^2 - 2ab + b^2")
            st.latex(r"a^2 - b^2 = (a+b)(a-b)")
            st.write("Quadratic Formula: x = [-b ± √(b²-4ac)] / 2a")
        with st.expander("Trigonometry"):
            st.latex(r"\sin^2\theta + \cos^2\theta = 1")
            st.write("sin 0°=0, sin 30°=1/2, sin 45°=1/√2, sin 60°=√3/2, sin 90°=1")
            st.write("cos 0°=1, cos 30°=√3/2, cos 45°=1/√2, cos 60°=1/2, cos 90°=0")

    elif subject == "Maths Class 9":
        with st.expander("Number System & Algebra"):
            st.latex(r"(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx")
            st.latex(r"x^3 + y^3 = (x+y)(x^2 - xy + y^2)")
            st.write("√2, √3 ye sab Irrational Number hote hain")

    elif subject == "Physics Class 10":
        with st.expander("Light - Mirror & Lens"):
            st.write("Mirror Formula: 1/v + 1/u = 1/f")
            st.write("Magnification: m = -v/u = h'/h")
            st.write("Lens Power: P = 1/f (f in meter)")
        with st.expander("Electricity"):
            st.write("V = I x R")
            st.write("Power: P = V x I = I²R = V²/R")

    elif subject == "Chemistry Class 10":
        with st.expander("Chemical Reactions"):
            st.write("Combination: A + B -> AB")
            st.write("Decomposition: AB -> A + B")
            st.write("Oxidation me Oxygen add hota hai, Reduction me Oxygen remove hota hai")
        with st.expander("Acid, Base & Salt"):
            st.write("pH Scale 0 to 14 tak hota hai")
            st.write("Acid ka pH < 7, Base ka pH > 7, Neutral ka pH = 7")
            st.write("HCl = Hydrochloric Acid, H2SO4 = Sulphuric Acid")

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
