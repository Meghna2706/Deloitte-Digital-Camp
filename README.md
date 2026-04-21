# ComDetect AI - Intelligent Fraud Detection System

## 🛡️ Overview

ComDetect AI is an **Agentic AI-powered fraud detection platform** designed to identify suspicious transaction patterns, detect anomalies, and provide **explainable insights** for auditors and risk teams in e-commerce environments.

The system leverages machine learning and behavioral analysis to detect various types of fraud in real-time, helping protect e-commerce platforms and financial institutions from fraudulent transactions.

---

## 🎯 Key Features

### Core Detection Pillars

1. **🧱 Account Takeover (ATO)**
   - Detects unusual login locations combined with high-value transactions
   - Identifies when user behavior significantly deviates from baseline

2. **🤖 Bot Activity**
   - Detects rapid, automated transactions
   - Identifies patterns consistent with bot-driven fraud
   - Monitors order velocity and frequency anomalies

3. **🌐 Multi-Account Fraud**
   - Identifies multiple users sharing the same IP address
   - Detects device fingerprinting patterns
   - Flags coordinated fraud attempts

4. **💳 Payment Anomaly**
   - Monitors high-value transaction detection
   - Identifies unusual payment methods or amounts
   - Analyzes payment-order relationships

5. **⚠️ Transaction Inconsistency**
   - Detects payment success with order failure scenarios
   - Identifies mismatches between payment and fulfillment systems
   - Flags chargebacks and returns anomalies

6. **📊 Behavioral Deviation**
   - Monitors user behavior against historical patterns
   - Identifies deviations from normal purchasing habits
   - Learns and adapts to individual user baselines

### User Interface Modules

- **Overview**: Comprehensive introduction to fraud detection pillars
- **Data**: Interactive dataset viewer with upload capability
- **Analysis**: Visual fraud risk assessment with pie charts and bar graphs
- **Voice**: Voice command control for hands-free navigation
- **Camera**: Facial recognition-based authentication for secure login

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web dashboard
- **Data Processing**: 
  - Pandas - Data manipulation and analysis
  - NumPy - Numerical computing
- **Visualization**: Plotly - Interactive graphs and charts
- **Computer Vision**: OpenCV - Face detection and camera integration
- **Audio**: Speech Recognition - Voice command processing
- **Language Support**: Multi-language interface (English, Chinese)

---

## 📋 Requirements

```
streamlit
pandas
numpy
plotly
opencv-python
SpeechRecognition
```

All dependencies are listed in `requirements.txt`.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd path/to/ComDetect
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

**Using main.py (Recommended)**
```bash
streamlit run main.py
```

**Using app.py**
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📊 How It Works

```
User Input → Fraud Detection Engine (6 Pillars) → Risk Scoring → Explainable Output → Dashboard Visualization
```

### Fraud Detection Logic

The system analyzes each transaction with the following criteria:

- **Account Takeover**: Non-India location + Amount > 5,000
- **Bot Activity**: Orders > 10 in short timeframe
- **Multi-Account Fraud**: Same IP address with 2+ user accounts
- **Payment Anomaly**: Transaction amount > 8,000
- **Transaction Inconsistency**: Payment without corresponding order
- **Behavioral Deviation**: Amount > 2x user's average

### Risk Scoring

- **Low Risk**: Normal behavior, no anomalies detected
- **Medium Risk**: Location anomaly or minor behavioral deviation
- **High Risk**: High transaction amount or multiple fraud indicators

---

## 👥 Target Users

- **Auditors**: Review suspicious transactions and generate compliance reports
- **Risk & Compliance Teams**: Monitor fraud trends and update detection rules
- **E-commerce Platforms**: Real-time fraud prevention and loss mitigation
- **Financial Institutions**: Transaction validation and chargeback prevention

---

## 📁 Project Structure

```
ComDetect/
├── main.py                 # Primary Streamlit application
├── app.py                  # Alternative Streamlit application
├── requirements.txt        # Python package dependencies
├── faces/
│   └── user.jpg           # Sample facial recognition image
├── venv/                  # Virtual environment (excluded from repo)
├── ComDetect_AI.pptx      # Project presentation
├── Prompt.docx            # Prompt engineering documentation
└── README.md              # This file
```

---

## 🎮 Usage Guide

### Overview Page
- Introduction to the fraud detection system
- Explanation of all 6 detection pillars
- System architecture overview

### Data Page
- View current transaction dataset
- Upload custom CSV files for analysis
- Examine data structure and patterns

### Analysis Page
- Run fraud detection on dataset
- View risk distribution pie chart
- Analyze transaction amounts by user
- Export detailed risk assessments

### Voice Control
- Use Windows Voice Typing (Win + H) or type commands
- Available commands:
  - "data" - Navigate to Data page
  - "analysis" - Run fraud analysis
  - "overview" - Return to Overview
  - "camera" - Access Camera Login
  - "high risk" - Filter and display high-risk users

### Camera Login
- Real-time facial recognition for user authentication
- Uses Haar Cascade for face detection
- Processes 100 frames for comprehensive face recognition
- Secure authentication before accessing sensitive data

---

## 🔐 Security Features

- Facial recognition-based authentication
- Multi-factor detection across 6 fraud pillars
- Explainable AI for audit trails
- Real-time risk scoring and alerts
- Behavioral baseline learning

---

## 📈 Performance Metrics

- **Detection Accuracy**: Multi-pillar approach for comprehensive fraud detection
- **Response Time**: Real-time analysis of transactions
- **False Positive Rate**: Minimized through behavioral learning
- **Explainability**: Each fraud flag includes detailed explanation

---

## 🔧 Configuration

### Fraud Detection Thresholds

You can adjust detection parameters in `main.py` and `app.py`:

- High transaction amount threshold (default: 1,000-8,000)
- Bot activity order limit (default: 10+ orders)
- Location change detection
- Multi-account IP sharing limit (default: 2+ users)

### Language Support

Currently supports:
- English
- Chinese (Simplified)

Additional languages can be added by extending the `languages` dictionary in the code.

---

## 🐛 Troubleshooting

### Camera Not Working
- Ensure your webcam is connected and enabled
- Check camera permissions in Windows settings
- Verify OpenCV installation: `pip install --upgrade opencv-python`

### Voice Command Issues
- Enable Windows Voice Typing (Win + H)
- Check microphone permissions
- Ensure SpeechRecognition library is installed

### Data Upload Errors
- Verify CSV format matches expected columns: `user_id`, `amount`, `location`, `orders`, `ip`, `device`
- Check file encoding (UTF-8 recommended)
- Ensure no special characters in column names

---

## 📝 Sample Data Format

Expected CSV columns:
- `user_id`: Unique user identifier (e.g., "U1", "U2")
- `amount`: Transaction amount (numeric)
- `location`: User location (text)
- `orders`: Number of orders in timeframe (numeric)
- `ip`: IP address (numeric or string)
- `device`: Device type (Mobile, Laptop, etc.)

---

## 🤝 Contributing

Improvements and enhancements are welcome! Consider contributing:
- Additional fraud detection pillars
- Enhanced ML models for better accuracy
- Support for additional languages
- Performance optimizations
- UI/UX improvements

---

## 📄 License

This project is proprietary software developed for Deloitte.

---

## 📞 Support

For issues, questions, or suggestions:
- Review the project documentation
- Check the troubleshooting section
- Consult the presentation (ComDetect_AI.pptx)
- Review prompt engineering notes (Prompt.docx)

---

## 🎓 Technical Insights

### Fraud Detection Algorithm

The system employs a multi-pillar approach where each transaction is evaluated across all 6 pillars simultaneously. Each positive detection increments a risk score:

```
Risk Score = Sum of all triggered fraud indicators
Risk Level = High (3+), Medium (1-2), Low (0)
```

### Machine Learning Integration

Current implementation uses rule-based detection. Future enhancements could include:
- Supervised learning with historical fraud data
- Unsupervised anomaly detection
- Neural networks for pattern recognition
- Temporal analysis for trend detection

### Explainable AI (XAI)

Every fraud flag includes:
- Specific trigger reason
- Affected transaction details
- Risk level justification
- Recommended action

---

**Version**: 1.0.0  
**Last Updated**: April 2026  
**Status**: Active Development
