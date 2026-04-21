import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import cv2

if "menu" not in st.session_state:
    st.session_state.menu = "Overview"
# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ComDetect AI", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛡️ ComDetect AI")

menu = st.sidebar.radio(
    "Navigation",
    ["Overview", "Data", "Analysis", "Voice", "Camera"],
    index=["Overview", "Data", "Analysis", "Voice", "Camera"].index(st.session_state.menu)
)
data_option = st.sidebar.selectbox(
    "Data Source",
    ["Sample Data", "Upload CSV"]
)
st.session_state.menu = menu

# ---------------- SAMPLE DATA ----------------
def load_sample():
    data = {
        "user_id": ["U1","U1","U1","U2","U3","U3"],
        "amount": [500,600,700,200,1500,1600],
        "location": ["India","India","USA","India","India","USA"],
        "device": ["Mobile","Mobile","Laptop","Mobile","Laptop","Laptop"],
        "ip": ["123","123","999","456","777","777"]
    }
    return pd.DataFrame(data)

if data_option == "Sample Data":
    df = load_sample()
else:
    uploaded = st.sidebar.file_uploader("Upload CSV")
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = load_sample()

# ---------------- FRAUD LOGIC ----------------
def detect_fraud(df):
    df["risk"] = "Low"
    df.loc[df["amount"] > 1000, "risk"] = "High"
    df.loc[df["location"].shift() != df["location"], "risk"] = "Medium"

    df["explanation"] = np.where(
        df["risk"] == "High",
        "High transaction detected",
        np.where(df["risk"] == "Medium",
                 "Location anomaly detected",
                 "Normal behavior")
    )
    return df

# ---------------- OVERVIEW ----------------
if menu == "Overview":
    st.title("🛡️ ComDetect AI")

    st.markdown("### Intelligent Fraud Detection System for E-Commerce")

    st.markdown("""
    ComDetect AI is an **Agentic AI-powered fraud detection platform** designed to identify suspicious transaction patterns, 
    detect anomalies, and provide **explainable insights** for auditors and risk teams.
    """)

    st.markdown("## 🧠 Core Detection Pillars")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🧱 Account Takeover (ATO)\n\nDetects unusual login location + high-value transactions")
        st.info("🤖 Bot Activity\n\nDetects rapid transactions & automated behavior")

    with col2:
        st.info("🌐 Multi-Account Fraud\n\nMultiple users sharing same IP/device")
        st.info("💳 Payment Anomaly\n\nHigh-value or suspicious payment behavior")

    with col3:
        st.info("⚠️ Transaction Inconsistency\n\nPayment success but order failure")
        st.info("📊 Behavioral Deviation\n\nUser behavior deviates from normal patterns")

    st.markdown("## ⚙️ How It Works")

    st.success("""
    User Input → Fraud Detection Engine (6 Pillars) → Risk Scoring → Explainable Output → Dashboard Visualization
    """)

    st.markdown("## 🎯 Who Uses This?")
    st.write("- Auditors")
    st.write("- Risk & Compliance Teams")
    st.write("- E-commerce Platforms")

# ---------------- DATA ----------------
elif menu == "Data":
    st.title("📊 Dataset")
    st.dataframe(df)

# ---------------- ANALYSIS ----------------
elif menu == "Analysis":
    st.title("🔍 Fraud Analysis")

    result = detect_fraud(df)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(result, names="risk", title="Risk Distribution")
        st.plotly_chart(fig)

    with col2:
        fig2 = px.bar(result, x="user_id", y="amount", color="risk")
        st.plotly_chart(fig2)

    st.dataframe(result)

# ---------------- VOICE ----------------
elif menu == "Voice":
    st.title("🎤 Voice Control")

    cmd = st.text_input("Use mic (Win + H) or type command")

    if cmd:
        cmd = cmd.lower()

        st.success(f"Command received: {cmd}")

        if "data" in cmd:
            st.session_state.menu = "Data"

        elif "analysis" in cmd:
            st.session_state.menu = "Analysis"

        elif "overview" in cmd:
            st.session_state.menu = "Overview"

        elif "camera" in cmd:
            st.session_state.menu = "Camera"

        elif "high risk" in cmd:
            result = detect_fraud(df)
            st.write("### 🔴 High Risk Users")
            st.dataframe(result[result["risk"] == "High"])

        st.rerun()

# ---------------- CAMERA ----------------
elif menu == "Camera":
    st.title("📷 Camera Login")

    if st.button("Start Camera"):
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        stframe = st.empty()

        for _ in range(100):
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

            stframe.image(frame, channels="BGR")

        cap.release()