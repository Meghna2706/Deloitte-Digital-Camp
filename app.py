# ------------------ IMPORTS ------------------
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import speech_recognition as sr

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Fraud Detection Dashboard", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main {background-color: #0f172a; color: white;}
.stButton>button {background-color: #2563eb; color: white; border-radius: 10px; padding: 10px 20px;}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION INIT ------------------
if "voice_cmd" not in st.session_state:
    st.session_state["voice_cmd"] = ""

# ------------------ LANGUAGE ------------------
languages = {
    "English": {
        "title": "AI Fraud Detection Dashboard",
        "upload": "Upload Dataset",
        "analyze": "Run Analysis",
        "result": "Results"
    },
    "Chinese": {
        "title": "人工智能欺诈检测仪表板",
        "upload": "上传数据",
        "analyze": "运行分析",
        "result": "结果"
    }
}

lang = st.sidebar.selectbox("Language", list(languages.keys()))
text = languages[lang]

st.title(text["title"])

# ------------------ DATA ------------------
source = st.radio("Choose Data Source", ["Sample Data", "Upload File"])

def generate_data():
    return pd.DataFrame({
        "user_id": ["U1","U1","U2","U3","U4","U5"],
        "amount": [100, 7000, 200, 300, 9000, 50],
        "location": ["India","USA","India","India","UK","India"],
        "orders": [1,15,1,2,20,1],
        "ip": ["111","111","222","333","333","333"],
        "device": ["Mobile","Laptop","Mobile","Mobile","Laptop","Mobile"]
    })

if source == "Upload File":
    file = st.file_uploader(text["upload"], type=["csv"])
    if file:
        df = pd.read_csv(file)
    else:
        st.warning("Please upload a file")
        st.stop()
else:
    df = generate_data()

# ------------------ FRAUD LOGIC ------------------
def detect_fraud(data):
    results = []
    for i,row in data.iterrows():
        risk = 0
        tags = []
        explanation = []

        if row["location"] != "India" and row["amount"] > 5000:
            risk += 2
            tags.append("ATO")
            explanation.append("Unusual location with high transaction")

        if row["orders"] > 10:
            risk += 2
            tags.append("Bot Activity")
            explanation.append("Too many orders in short time")

        if df[df["ip"] == row["ip"]].shape[0] > 2:
            risk += 1
            tags.append("Multi-account")
            explanation.append("Multiple users sharing same IP")

        if row["amount"] > 8000:
            risk += 2
            tags.append("Payment Anomaly")
            explanation.append("High value transaction detected")

        if row["orders"] == 0 and row["amount"] > 0:
            risk += 2
            tags.append("Inconsistency")
            explanation.append("Payment without order")

        if row["amount"] > df["amount"].mean() * 2:
            risk += 1
            tags.append("Behavioral Deviation")
            explanation.append("Spending unusually high")

        level = "Low"
        if risk >= 4:
            level = "High"
        elif risk >= 2:
            level = "Medium"

        results.append({
            "user": row["user_id"],
            "risk_score": risk,
            "risk_level": level,
            "tags": ", ".join(tags),
            "explanation": "; ".join(explanation)
        })

    return pd.DataFrame(results)

# ------------------ VOICE ------------------
st.sidebar.markdown("### 🎤 Voice Control")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.sidebar.info("Listening...")
        audio = r.listen(source, timeout=5)

    try:
        text_cmd = r.recognize_google(audio)
        st.sidebar.success(f"You said: {text_cmd}")
        return text_cmd.lower()
    except:
        st.sidebar.error("Could not understand")
        return ""

if st.sidebar.button("🎙️ Start Voice Command"):
    st.session_state["voice_cmd"] = listen_command()

cmd = st.session_state.get("voice_cmd", "")

if "run analysis" in cmd:
    st.session_state["run"] = True

elif "show high risk" in cmd:
    st.session_state["filter"] = "High"

elif "show medium risk" in cmd:
    st.session_state["filter"] = "Medium"

elif "show low risk" in cmd:
    st.session_state["filter"] = "Low"

# ------------------ TABS ------------------
tab1, tab2, tab3 = st.tabs(["Overview", "Data", "Results"])

with tab1:
    st.write("Welcome to AI Fraud Detection System")
    st.write("This system detects fraud using 6 intelligent pillars.")

with tab2:
    st.dataframe(df)

with tab3:
    if st.button(text["analyze"]) or st.session_state.get("run", False):

        result = detect_fraud(df)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Users", len(result))
        col2.metric("High Risk", result[result["risk_level"]=="High"].shape[0])
        col3.metric("Medium Risk", result[result["risk_level"]=="Medium"].shape[0])

        st.subheader(text["result"])
        st.dataframe(result)

        filter_level = st.session_state.get("filter", None)
        if filter_level:
            st.subheader(f"{filter_level} Risk Users")
            st.dataframe(result[result["risk_level"] == filter_level])

        st.subheader("Risk Distribution")
        st.plotly_chart(px.pie(result, names="risk_level"))

        st.subheader("Risk Score Distribution")
        st.plotly_chart(px.bar(result, x="user", y="risk_score", color="risk_level"))

        st.subheader("Fraud Explanation Panel")
        for i,row in result.iterrows():
            st.info(f"User {row['user']}: {row['explanation']}")

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("AI Fraud Detection System | Deloitte Ready Project")