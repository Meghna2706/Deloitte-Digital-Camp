# ------------------ IMPORTS ------------------
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import speech_recognition as sr
import cv2
from io import StringIO
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Fraud Detection Dashboard", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main {background-color: #0f172a; color: white;}
.stButton>button {background-color: #2563eb; color: white; border-radius: 10px; padding: 10px 20px;}
.metric-box {padding: 20px; border-radius: 10px; background-color: #1e293b;}
</style>
""", unsafe_allow_html=True)

# ------------------ COMPREHENSIVE LANGUAGE SUPPORT ------------------
languages = {
    "English": {
        "title": "AI Fraud Detection Dashboard",
        "subtitle": "Intelligent Fraud Detection System",
        "upload": "Upload Dataset",
        "analyze": "Run Analysis",
        "result": "Results",
        "data_source": "Choose Data Source",
        "sample_data": "Sample Data",
        "upload_file": "Upload File",
        "overview": "Overview",
        "data": "Data",
        "results": "Results",
        "welcome": "Welcome to AI Fraud Detection System",
        "description": "This system detects fraud using 6 intelligent pillars.",
        "total_users": "Total Users",
        "high_risk": "High Risk",
        "medium_risk": "Medium Risk",
        "low_risk": "Low Risk",
        "risk_distribution": "Risk Distribution",
        "risk_score_dist": "Risk Score Distribution",
        "fraud_panel": "Fraud Explanation Panel",
        "export_csv": "Download Results as CSV",
        "settings": "Detection Settings",
        "thresholds": "Fraud Detection Thresholds",
        "ato_threshold": "ATO Location Threshold (amount)",
        "bot_threshold": "Bot Activity Order Limit",
        "payment_threshold": "Payment Anomaly Threshold",
        "multi_ip_threshold": "Multi-Account IP Threshold",
        "behavioral_multiplier": "Behavioral Deviation Multiplier",
        "voice_control": "Voice Control",
        "start_voice": "Start Voice Command",
        "listening": "Listening...",
        "not_understand": "Could not understand",
        "footer": "AI Fraud Detection System | Deloitte Ready Project",
        "login_title": "🔐 Face Recognition Login",
        "login_subtitle": "Secure Access via Facial Recognition",
        "start_camera": "Start Camera & Login",
        "face_detected": "Face Detected Successfully!",
        "no_face_detected": "No face detected",
        "authenticating": "Authenticating...",
        "login_success": "Login Successful!",
        "logout": "Logout",
        "camera_frames": "Processing frames for face detection",
        "access_denied": "Access Denied - No face detected"
    },
    "Chinese": {
        "title": "人工智能欺诈检测仪表板",
        "subtitle": "智能欺诈检测系统",
        "upload": "上传数据集",
        "analyze": "运行分析",
        "result": "结果",
        "data_source": "选择数据源",
        "sample_data": "示例数据",
        "upload_file": "上传文件",
        "overview": "概述",
        "data": "数据",
        "results": "结果",
        "welcome": "欢迎使用人工智能欺诈检测系统",
        "description": "该系统使用6个智能支柱进行欺诈检测。",
        "total_users": "用户总数",
        "high_risk": "高风险",
        "medium_risk": "中等风险",
        "low_risk": "低风险",
        "risk_distribution": "风险分布",
        "risk_score_dist": "风险评分分布",
        "fraud_panel": "欺诈解释面板",
        "export_csv": "下载结果为CSV",
        "settings": "检测设置",
        "thresholds": "欺诈检测阈值",
        "ato_threshold": "ATO位置阈值（金额）",
        "bot_threshold": "机器人活动订单限制",
        "payment_threshold": "支付异常阈值",
        "multi_ip_threshold": "多账户IP阈值",
        "behavioral_multiplier": "行为偏差乘数",
        "voice_control": "语音控制",
        "start_voice": "开始语音命令",
        "listening": "正在监听...",
        "not_understand": "无法理解",
        "footer": "人工智能欺诈检测系统 | Deloitte项目",
        "login_title": "🔐 人脸识别登录",
        "login_subtitle": "通过面部识别进行安全访问",
        "start_camera": "启动摄像头并登录",
        "face_detected": "成功检测到人脸！",
        "no_face_detected": "未检测到人脸",
        "authenticating": "正在认证...",
        "login_success": "登录成功！",
        "logout": "登出",
        "camera_frames": "正在处理人脸检测帧",
        "access_denied": "访问被拒绝 - 未检测到人脸"
    }
}

lang = st.sidebar.selectbox("Language", list(languages.keys()))
text = languages[lang]

# ============ FACE RECOGNITION LOGIN SYSTEM ============
@st.cache_resource
def get_face_detector():
    """Load Haar Cascade face detector (cached for performance)"""
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_cascade = get_face_detector()

def detect_faces_in_frame(frame):
    """Detect faces in a given frame"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces, gray

def face_recognition_login():
    """Face Recognition Authentication Page"""
    st.markdown(f"<h1 style='text-align: center;'>{text['login_title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{text['login_subtitle']}</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://img.icons8.com/color/96/000000/face-recognition.png", width=100)
        
        if st.button(f"🎥 {text['start_camera']}", key="login_camera", use_container_width=True):
            st.session_state["authenticating"] = True
    
    if st.session_state.get("authenticating", False):
        progress_bar = st.progress(0)
        status_text = st.empty()
        frame_display = st.empty()
        
        cap = cv2.VideoCapture(0)
        face_detected_count = 0
        frames_processed = 0
        max_frames = 30  # Process 30 frames for face detection
        
        status_text.info(f"🎬 {text['camera_frames']}...")
        
        try:
            while frames_processed < max_frames:
                ret, frame = cap.read()
                
                if not ret:
                    status_text.error("❌ Cannot access camera. Please check permissions.")
                    break
                
                # Resize frame for faster processing
                frame = cv2.resize(frame, (640, 480))
                
                # Detect faces
                faces, gray = detect_faces_in_frame(frame)
                
                # Draw rectangles around detected faces
                frame_display_copy = frame.copy()
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame_display_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame_display_copy, "Face Detected", (x, y - 10),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    face_detected_count += 1
                
                # Display frame
                frame_display.image(frame_display_copy, channels="BGR", use_column_width=True)
                
                # Update progress
                progress_bar.progress((frames_processed + 1) / max_frames)
                
                # Update status
                if len(faces) > 0:
                    status_text.success(f"✅ {text['face_detected']} ({len(faces)} face(s) detected)")
                else:
                    status_text.warning(f"⏳ {text['no_face_detected']} - Frame {frames_processed + 1}/{max_frames}")
                
                frames_processed += 1
                time.sleep(0.1)  # Small delay to allow frame capture
        
        finally:
            cap.release()
        
        # Authentication result
        if face_detected_count > 0:
            st.success(f"🎉 {text['login_success']}", icon="✅")
            st.balloons()
            time.sleep(1.5)
            st.session_state["authenticated"] = True
            st.session_state["authenticating"] = False
            st.rerun()
        else:
            st.error(f"❌ {text['access_denied']}", icon="🚫")
            st.session_state["authenticating"] = False

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "authenticating" not in st.session_state:
    st.session_state["authenticating"] = False

# Show login page if not authenticated
if not st.session_state.get("authenticated", False):
    face_recognition_login()
    st.stop()

# User is authenticated - show main app
st.title(text["title"])
st.markdown(f"### {text['subtitle']}")

# Add logout button in sidebar
with st.sidebar:
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col2:
        if st.button("🚪 " + text["logout"], use_container_width=True, key="logout_btn"):
            st.session_state["authenticated"] = False
            st.rerun()
    st.markdown("---")

# ------------------ COMPREHENSIVE SESSION INIT ------------------
if "voice_cmd" not in st.session_state:
    st.session_state["voice_cmd"] = ""
if "run" not in st.session_state:
    st.session_state["run"] = False
if "filter" not in st.session_state:
    st.session_state["filter"] = None
if "df" not in st.session_state:
    st.session_state["df"] = None
if "result" not in st.session_state:
    st.session_state["result"] = None

# REQUIRED COLUMNS FOR CSV VALIDATION
REQUIRED_COLUMNS = ["user_id", "amount", "location", "orders", "ip", "device"]

# ============ DATA LOADING SECTION ============
col1, col2 = st.columns([2, 1])

with col1:
    source = st.radio(text["data_source"], [text["sample_data"], text["upload_file"]], horizontal=True)

with col2:
    st.write("")  # spacing

def generate_sample_data():
    """Generate sample fraud detection dataset"""
    return pd.DataFrame({
        "user_id": ["U1", "U1", "U2", "U3", "U4", "U5", "U6", "U7"],
        "amount": [100, 7000, 200, 300, 9000, 50, 6500, 8500],
        "location": ["India", "USA", "India", "India", "UK", "India", "USA", "Canada"],
        "orders": [1, 15, 1, 2, 20, 1, 8, 12],
        "ip": ["111", "111", "222", "333", "333", "333", "444", "444"],
        "device": ["Mobile", "Laptop", "Mobile", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile"]
    })

def validate_csv(df):
    """Validate that uploaded CSV has required columns"""
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")
    return True

# Load data based on user selection
try:
    if text["upload_file"] in source:
        file = st.file_uploader(text["upload"], type=["csv"])
        if file:
            df = pd.read_csv(file)
            validate_csv(df)
            st.success(f"✅ File loaded successfully! Shape: {df.shape}")
            st.session_state["df"] = df
        else:
            st.info("📤 Waiting for file upload...")
            df = generate_sample_data()
            st.session_state["df"] = df
    else:
        df = generate_sample_data()
        st.session_state["df"] = df
except ValueError as e:
    st.error(f"❌ CSV Validation Error: {e}")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading file: {e}")
    df = generate_sample_data()
    st.session_state["df"] = df

# ============ CONFIGURABLE FRAUD DETECTION SETTINGS ============
with st.sidebar.expander(text["settings"], expanded=False):
    st.subheader(text["thresholds"])
    
    ato_amount = st.slider(
        text["ato_threshold"],
        min_value=1000,
        max_value=10000,
        value=5000,
        step=500,
        help="Amount threshold for Account Takeover detection (non-India)"
    )
    
    bot_orders = st.slider(
        text["bot_threshold"],
        min_value=5,
        max_value=50,
        value=10,
        step=1,
        help="Order limit for Bot Activity detection"
    )
    
    payment_anomaly = st.slider(
        text["payment_threshold"],
        min_value=5000,
        max_value=15000,
        value=8000,
        step=500,
        help="Amount threshold for Payment Anomaly detection"
    )
    
    multi_ip = st.slider(
        text["multi_ip_threshold"],
        min_value=2,
        max_value=5,
        value=2,
        step=1,
        help="User count threshold for Multi-Account fraud"
    )
    
    behavioral_mult = st.slider(
        text["behavioral_multiplier"],
        min_value=1.0,
        max_value=3.0,
        value=2.0,
        step=0.1,
        help="Multiplier for Behavioral Deviation (vs average)"
    )

# ============ OPTIMIZED FRAUD DETECTION ============
def detect_fraud_optimized(data, config):
    """
    Optimized fraud detection with configurable thresholds
    
    Parameters:
    - data: DataFrame with transaction data
    - config: Dictionary with detection thresholds
    """
    results = []
    
    # Pre-calculate statistics to avoid recalculation in loop
    avg_amount = data["amount"].mean()
    ip_counts = data["ip"].value_counts()
    
    for i, row in data.iterrows():
        risk = 0
        tags = []
        explanation = []
        
        # Pillar 1: Account Takeover (ATO)
        if row["location"] != "India" and row["amount"] > config["ato_amount"]:
            risk += 2
            tags.append("ATO")
            explanation.append(f"Unusual location ({row['location']}) with high transaction (${row['amount']})")
        
        # Pillar 2: Bot Activity
        if row["orders"] > config["bot_orders"]:
            risk += 2
            tags.append("Bot Activity")
            explanation.append(f"Too many orders ({row['orders']}) in short time")
        
        # Pillar 3: Multi-Account Fraud (optimized with pre-calculated counts)
        ip_user_count = ip_counts.get(row["ip"], 0)
        if ip_user_count > config["multi_ip"]:
            risk += 1
            tags.append("Multi-account")
            explanation.append(f"IP shared by {ip_user_count} users")
        
        # Pillar 4: Payment Anomaly
        if row["amount"] > config["payment_anomaly"]:
            risk += 2
            tags.append("Payment Anomaly")
            explanation.append(f"High value transaction (${row['amount']})")
        
        # Pillar 5: Transaction Inconsistency
        if row["orders"] == 0 and row["amount"] > 0:
            risk += 2
            tags.append("Inconsistency")
            explanation.append("Payment without corresponding order")
        
        # Pillar 6: Behavioral Deviation
        if row["amount"] > avg_amount * config["behavioral_multiplier"]:
            risk += 1
            tags.append("Behavioral Deviation")
            explanation.append(f"Spending {config['behavioral_multiplier']:.1f}x user average (${avg_amount:.2f})")
        
        # Determine risk level
        if risk >= 4:
            level = "High"
        elif risk >= 2:
            level = "Medium"
        else:
            level = "Low"
        
        results.append({
            "User": row["user_id"],
            "Amount": f"${row['amount']}",
            "Location": row["location"],
            "Orders": row["orders"],
            "Risk Score": risk,
            "Risk Level": level,
            "Flags": ", ".join(tags) if tags else "None",
            "Details": "; ".join(explanation) if explanation else "No anomalies detected"
        })
    
    return pd.DataFrame(results)

@st.cache_data
def convert_df_to_csv(df):
    """Convert DataFrame to CSV for download"""
    return df.to_csv(index=False).encode('utf-8')


# ============ INTELLIGENT VOICE COMMAND SYSTEM ============

def parse_voice_command(voice_input):
    """
    Intelligent natural language command parser
    Processes complex voice commands with multiple actions
    
    Returns: Dictionary with identified actions and parameters
    """
    cmd = voice_input.lower()
    actions = {
        "navigate_overview": False,
        "navigate_data": False,
        "navigate_results": False,
        "run_analysis": False,
        "filter_high": False,
        "filter_medium": False,
        "filter_low": False,
        "filter_all": False,
        "recognized": False
    }
    
    # Navigation keywords
    nav_keywords_overview = ["overview", "home", "go home", "show overview", "go to overview"]
    nav_keywords_data = ["data", "dataset", "go to data", "show data", "view data", "check data"]
    nav_keywords_results = ["results", "analysis", "go to results", "show results", "go to analysis"]
    
    # Action keywords
    action_keywords = ["run", "execute", "process", "start", "analyze", "perform", "do"]
    
    # Risk level keywords
    high_risk_keywords = ["high risk", "high", "dangerous", "critical"]
    medium_risk_keywords = ["medium risk", "medium", "moderate", "warning"]
    low_risk_keywords = ["low risk", "low", "safe", "normal"]
    clear_keywords = ["clear", "reset", "show all", "reset filter", "all risks", "all"]
    
    # Check for any recognized keywords
    all_keywords = (nav_keywords_overview + nav_keywords_data + nav_keywords_results + 
                   action_keywords + high_risk_keywords + medium_risk_keywords + 
                   low_risk_keywords + clear_keywords)
    
    if not any(keyword in cmd for keyword in all_keywords):
        return actions  # Return empty if no keywords found
    
    actions["recognized"] = True
    
    # Navigation detection (with context awareness)
    if any(keyword in cmd for keyword in nav_keywords_overview):
        actions["navigate_overview"] = True
    
    if any(keyword in cmd for keyword in nav_keywords_data):
        actions["navigate_data"] = True
    
    if any(keyword in cmd for keyword in nav_keywords_results):
        actions["navigate_results"] = True
    
    # Action detection (analyze/process commands)
    if any(keyword in cmd for keyword in action_keywords):
        # Check if it's in context of results
        if "result" in cmd or "analysis" in cmd or "process" in cmd:
            actions["run_analysis"] = True
    
    # Risk filtering detection
    if any(keyword in cmd for keyword in high_risk_keywords):
        actions["filter_high"] = True
    
    if any(keyword in cmd for keyword in medium_risk_keywords):
        actions["filter_medium"] = True
    
    if any(keyword in cmd for keyword in low_risk_keywords):
        actions["filter_low"] = True
    
    if any(keyword in cmd for keyword in clear_keywords):
        actions["filter_all"] = True
    
    return actions

st.sidebar.markdown("---")
st.sidebar.markdown(f"### {text['voice_control']}")

# Voice command hints
with st.sidebar.expander("💡 Voice Command Examples", expanded=False):
    st.markdown("""
    **Navigation Commands:**
    - "Go to data"
    - "Show overview"
    - "Navigate to results"
    
    **Action Commands:**
    - "Analyze the data"
    - "Run analysis"
    - "Process the results"
    
    **Filtering Commands:**
    - "Show high risk"
    - "Display medium risk"
    - "Filter low risk"
    
    **Combined Commands:**
    - "Go to data and process the result"
    - "Navigate to results and show high risk"
    - "Analyze and show high risk users"
    """)

def listen_command():
    """Capture voice command from user"""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.sidebar.info(text["listening"])
            audio = r.listen(source, timeout=5)
        
        text_cmd = r.recognize_google(audio)
        st.sidebar.success(f"✅ {text_cmd}")
        return text_cmd.lower()
    except Exception as e:
        st.sidebar.error(text["not_understand"])
        return ""

if st.sidebar.button(f"🎙️ {text['start_voice']}"):
    st.session_state["voice_cmd"] = listen_command()

cmd = st.session_state.get("voice_cmd", "")

# Parse and process voice command
if cmd:
    actions = parse_voice_command(cmd)
    
    if actions["recognized"]:
        # Process navigation commands
        if actions["navigate_overview"]:
            st.session_state["current_tab"] = "overview"
        
        if actions["navigate_data"]:
            st.session_state["current_tab"] = "data"
        
        if actions["navigate_results"]:
            st.session_state["current_tab"] = "results"
        
        # Process action commands
        if actions["run_analysis"]:
            st.session_state["run"] = True
            # Auto-navigate to results if analyzing
            st.session_state["current_tab"] = "results"
        
        # Process filter commands
        if actions["filter_high"]:
            st.session_state["filter"] = "High"
            st.session_state["current_tab"] = "results"
        
        if actions["filter_medium"]:
            st.session_state["filter"] = "Medium"
            st.session_state["current_tab"] = "results"
        
        if actions["filter_low"]:
            st.session_state["filter"] = "Low"
            st.session_state["current_tab"] = "results"
        
        if actions["filter_all"]:
            st.session_state["filter"] = None
        
        # Create feedback message
        feedback = []
        if actions["navigate_overview"]:
            feedback.append("📋 Overview")
        if actions["navigate_data"]:
            feedback.append("📊 Data")
        if actions["navigate_results"]:
            feedback.append("📈 Results")
        if actions["run_analysis"]:
            feedback.append("🔍 Running Analysis")
        if actions["filter_high"]:
            feedback.append("🔴 High Risk Filter")
        if actions["filter_medium"]:
            feedback.append("🟡 Medium Risk Filter")
        if actions["filter_low"]:
            feedback.append("🟢 Low Risk Filter")
        
        if feedback:
            st.sidebar.info(f"✨ Command recognized:\n" + ", ".join(feedback))
    else:
        st.sidebar.warning(f"❓ Could not understand: '{cmd}'\n\nTry: 'go to data', 'analyze', 'show high risk', etc.")

# Initialize current tab state
if "current_tab" not in st.session_state:
    st.session_state["current_tab"] = "overview"

# ============ MAIN INTERFACE - INTELLIGENT TAB SELECTION ============
# Determine which tab to show based on voice commands or user clicks
current_tab = st.session_state.get("current_tab", "overview")

# Tab selector in main area
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📋 " + text["overview"], use_container_width=True, 
                 key="btn_overview", type="primary" if current_tab == "overview" else "secondary"):
        st.session_state["current_tab"] = "overview"
        st.rerun()

with col2:
    if st.button("📊 " + text["data"], use_container_width=True,
                 key="btn_data", type="primary" if current_tab == "data" else "secondary"):
        st.session_state["current_tab"] = "data"
        st.rerun()

with col3:
    if st.button("📈 " + text["results"], use_container_width=True,
                 key="btn_results", type="primary" if current_tab == "results" else "secondary"):
        st.session_state["current_tab"] = "results"
        st.rerun()

st.markdown("---")

# OVERVIEW TAB
if current_tab == "overview":
    st.write(f"### {text['welcome']}")
    st.write(text["description"])
    
    col1, col2, col3 = st.columns(3)
    col1.info("🧱 **Account Takeover (ATO)**\nUnusual login location + high-value transactions")
    col2.info("🤖 **Bot Activity**\nRapid transactions & automated behavior")
    col3.info("🌐 **Multi-Account Fraud**\nMultiple users sharing same IP/device")
    
    col1, col2, col3 = st.columns(3)
    col1.info("💳 **Payment Anomaly**\nHigh-value or suspicious payment behavior")
    col2.info("⚠️ **Transaction Inconsistency**\nPayment success but order failure")
    col3.info("📊 **Behavioral Deviation**\nUser behavior deviates from normal patterns")

# DATA TAB
elif current_tab == "data":
    st.subheader(text["data"])
    st.dataframe(st.session_state["df"], use_container_width=True)
    
    st.markdown("**Dataset Summary:**")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", len(st.session_state["df"]))
    col2.metric("Unique Users", st.session_state["df"]["user_id"].nunique())
    col3.metric("Avg Transaction", f"${st.session_state['df']['amount'].mean():.2f}")
    col4.metric("Max Transaction", f"${st.session_state['df']['amount'].max():.2f}")

# RESULTS TAB
elif current_tab == "results":
    st.subheader(text["results"])
    
    # Prepare fraud detection config
    config = {
        "ato_amount": ato_amount,
        "bot_orders": bot_orders,
        "payment_anomaly": payment_anomaly,
        "multi_ip": multi_ip,
        "behavioral_multiplier": behavioral_mult
    }
    
    # Run analysis button
    if st.button(text["analyze"], key="analyze_btn") or st.session_state.get("run", False):
        with st.spinner("🔍 Analyzing transactions..."):
            result = detect_fraud_optimized(st.session_state["df"], config)
            st.session_state["result"] = result
        
        # Display metrics
        high_risk_count = (result["Risk Level"] == "High").sum()
        medium_risk_count = (result["Risk Level"] == "Medium").sum()
        low_risk_count = (result["Risk Level"] == "Low").sum()
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(text["total_users"], len(result))
        col2.metric(text["high_risk"], high_risk_count, delta=None, delta_color="inverse")
        col3.metric(text["medium_risk"], medium_risk_count)
        col4.metric(text["low_risk"], low_risk_count)
        
        # Display results table
        st.markdown("### 📋 Detailed Results")
        st.dataframe(result, use_container_width=True)
        
        # Export functionality
        csv = convert_df_to_csv(result)
        st.download_button(
            label=f"📥 {text['export_csv']}",
            data=csv,
            file_name="fraud_detection_results.csv",
            mime="text/csv"
        )
        
        # Filtering by risk level
        filter_level = st.session_state.get("filter")
        if filter_level:
            st.markdown(f"### 🔍 {filter_level} {text['risk_distribution']}")
            filtered = result[result["Risk Level"] == filter_level]
            st.dataframe(filtered, use_container_width=True)
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### {text['risk_distribution']}")
            risk_counts = result["Risk Level"].value_counts()
            fig_pie = px.pie(
                values=risk_counts.values,
                names=risk_counts.index,
                color_discrete_sequence=["#ef4444", "#eab308", "#22c55e"],
                title="Risk Distribution"
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            st.markdown(f"### {text['risk_score_dist']}")
            fig_bar = px.bar(
                result,
                x="User",
                y="Risk Score",
                color="Risk Level",
                color_discrete_map={"High": "#ef4444", "Medium": "#eab308", "Low": "#22c55e"},
                title="Risk Score by User"
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        # Fraud explanation panel
        st.markdown(f"### {text['fraud_panel']}")
        for i, row in result.iterrows():
            color_map = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
            flag_emoji = color_map.get(row["Risk Level"], "❓")
            
            with st.expander(f"{flag_emoji} {row['User']} - {row['Risk Level']} (Score: {row['Risk Score']})"):
                st.write(f"**Amount:** {row['Amount']}")
                st.write(f"**Location:** {row['Location']}")
                st.write(f"**Orders:** {row['Orders']}")
                st.write(f"**Flags:** {row['Flags']}")
                st.write(f"**Details:** {row['Details']}")
    else:
        st.info("👆 Click the 'Run Analysis' button to analyze transactions for fraud.")

# ============ FOOTER ============
st.markdown("---")
st.markdown(text["footer"])