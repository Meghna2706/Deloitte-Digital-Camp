# ComDetect AI - Video Demo Recording Guide

## 📹 Quick Start

There are 3 ways to record a demo of your ComDetect AI application:

### **Option 1: Simple Screen Recording (RECOMMENDED) ⭐**

**Best for:** Quick, straightforward recording of your app demo

```bash
python simple_recorder.py
```

**Features:**
- ✅ Simple & reliable
- ✅ 3-minute recording window
- ✅ Automatic timestamp overlay
- ✅ No complex automation
- ✅ Works on any Windows system

**Requirements:**
```bash
pip install mss opencv-python
```

**How to use:**
1. Run the script
2. When it says "Press Enter to START recording...", get ready
3. Press Enter
4. Perform your app demo:
   - Login with face recognition
   - Navigate tabs (Overview, Data, Results)
   - Click "Run Analysis" button
   - Show charts and visualization
   - Apply risk filters
   - Open settings panel
   - Show voice command help
   - Click export button
5. Recording stops automatically after 3 minutes
6. Video saves as `ComDetect_Demo.mp4`

---

### **Option 2: Advanced Auto-Demo Recording**

**Best for:** Automated demo with pre-programmed actions

```bash
python demo_recorder.py
```

**Features:**
- ✅ Fully automated demo sequence
- ✅ Shows all major features
- ✅ Scene-by-scene recording
- ✅ Professional flow
- ✅ Includes timing annotations

**Requirements:**
```bash
pip install pyautogui mss opencv-python pillow imageio imageio-ffmpeg
```

**Note:** This requires camera access for face detection

---

### **Option 3: Windows Screen Recorder Batch Script**

**Best for:** Quick one-liner recording using Windows native tools

```bash
record_demo.bat
```

**How it works:**
- Uses Windows built-in screen recording tools
- Starts Streamlit app automatically
- Records your actions
- No Python dependencies needed (beyond Streamlit)

---

## 📊 Demo Script Walkthrough

When recording, follow this sequence for best results:

### **Scene 1: Login (10-15 seconds)**
```
→ App loads with Face Recognition Login screen
→ Click "🎥 Start Camera & Login" button
→ Face detection happens automatically
→ See success message and balloons
```

### **Scene 2: Overview Tab (15-20 seconds)**
```
→ Click "📋 Overview" button
→ Show all 6 fraud detection pillars
→ Scroll down to see complete information
```

### **Scene 3: Data Tab (15-20 seconds)**
```
→ Click "📊 Data" button
→ Show dataset with transaction records
→ Display dataset summary (records, users, average amount)
→ Scroll to see more rows
```

### **Scene 4: Results Tab - Analysis (20-30 seconds)**
```
→ Click "📈 Results" button
→ Click blue "Run Analysis" button
→ Wait for analysis to complete
→ Show metrics (Total Users, High Risk, Medium Risk, Low Risk)
→ Display detailed results table
```

### **Scene 5: Visualizations (15-20 seconds)**
```
→ Scroll down to see Risk Distribution pie chart
→ Show Risk Score bar chart
→ Hover over charts to show interactivity
```

### **Scene 6: Risk Filtering (10-15 seconds)**
```
→ Scroll back up slightly
→ Notice "Risk Distribution" filter section appears
→ Show filtering for high risk users
→ Show different risk levels
```

### **Scene 7: Detection Settings (10-15 seconds)**
```
→ In sidebar, click "Detection Settings" expander
→ Show adjustable thresholds:
  - ATO Location Threshold
  - Bot Activity Order Limit
  - Payment Anomaly Threshold
  - Multi-Account IP Threshold
  - Behavioral Deviation Multiplier
→ Demonstrate slider adjustments
```

### **Scene 8: Voice Command Help (5-10 seconds)**
```
→ In sidebar, click "Voice Control"
→ Click "💡 Voice Command Examples" expander
→ Show all available voice commands
```

### **Scene 9: Export Feature (5-10 seconds)**
```
→ Scroll down in Results tab
→ Show "📥 Download Results as CSV" button
→ Explain export functionality
```

### **Scene 10: Logout (5 seconds)**
```
→ Click "🚪 Logout" button in sidebar
→ App returns to Face Recognition Login
```

---

## 🎬 Recording Best Practices

### **Before Recording:**
- ✅ Close unnecessary applications
- ✅ Ensure good lighting (for face detection)
- ✅ Check your camera works
- ✅ Have internet connection (for app)
- ✅ Use 1920x1080 resolution for best quality
- ✅ Test the app once manually first

### **During Recording:**
- ✅ Move mouse slowly and deliberately
- ✅ Pause between actions (2-3 seconds)
- ✅ Click buttons clearly
- ✅ Scroll smoothly
- ✅ Give time for app to load
- ✅ Speak clearly if narrating (record separately)

### **Video Quality Tips:**
- ✅ Use at least 30 FPS for smooth video
- ✅ Keep resolution at 1920x1080
- ✅ Adequate lighting for face recognition
- ✅ Minimal background movement

---

## 📁 Output Files

### **ComDetect_Demo.mp4**
- Your final demo video
- Shareable on social media, YouTube, presentations
- ~3-5 MB size (depending on recording length)

### **How to Share:**
1. **Upload to YouTube:**
   - YouTube.com → Create → Upload video
   - Title: "ComDetect AI - Fraud Detection Demo"
   - Description: Include features and benefits

2. **Share as Attachment:**
   - Email to stakeholders
   - Include in project documentation
   - Add to README.md

3. **Embed in Presentation:**
   - Add to PowerPoint/Google Slides
   - Use in investor pitch
   - Include in proposals

---

## 🛠️ Troubleshooting

### **Issue: "Camera not found"**
```
Solution:
- Check camera is connected
- Test camera with Windows Camera app
- Grant permission in Windows Settings
- Try running as Administrator
```

### **Issue: "Streamlit app won't start"**
```
Solution:
- Ensure Streamlit is installed: pip install streamlit
- Check you're in correct directory
- Kill any existing Streamlit processes
- Try manually: streamlit run app.py
```

### **Issue: "Recording is laggy"**
```
Solution:
- Close other applications
- Reduce FPS to 24 instead of 30
- Reduce resolution to 1280x720
- Exit browser tabs
```

### **Issue: "Face detection fails during login"**
```
Solution:
- Ensure good lighting on your face
- Sit 30cm from camera
- Look straight at camera
- Camera should be clear (no obstructions)
- Try multiple times if needed
```

### **Issue: "Video file is corrupted"**
```
Solution:
- Install ffmpeg: pip install imageio-ffmpeg
- Try using simple_recorder.py instead
- Check disk space is available
- Use supported format (MP4, AVI)
```

---

## 📝 Script Comparison

| Feature | Simple | Advanced | Batch |
|---------|--------|----------|-------|
| Setup | 2 minutes | 5 minutes | 1 minute |
| Ease of Use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Automation | Manual Demo | Full Auto | Script Only |
| Python Required | Yes | Yes | No |
| Requirements | mss, cv2 | pyautogui, more | None |
| Duration | Variable | ~2 minutes | Variable |
| Customization | Easy | Advanced | Hard |

**RECOMMENDATION: Use `simple_recorder.py` for best results! 🎯**

---

## 🎥 Video Editing (Optional)

After recording, you can enhance your video:

### **Using OpenCV (Python):**
```python
import cv2

cap = cv2.VideoCapture('ComDetect_Demo.mp4')
# Edit, trim, add text, music using cv2
```

### **Using Online Tools:**
- Clipchamp.com (Free, no download)
- iMovie (Mac)
- Windows Photos Video Editor (Windows)
- DaVinci Resolve (Free, professional)

### **Enhancements:**
- ✅ Add background music
- ✅ Insert title screen
- ✅ Add text overlays for features
- ✅ Trim unnecessary sections
- ✅ Adjust playback speed
- ✅ Add captions

---

## 📤 Sharing Checklist

Before sharing your demo:

- [ ] Video is 30+ seconds minimum
- [ ] Shows login feature
- [ ] Demonstrates fraud detection
- [ ] Shows visualization/charts
- [ ] Includes voice command mention
- [ ] Video is clear and smooth
- [ ] Audio is good (if narrated)
- [ ] File size is reasonable (<50MB)
- [ ] Filename is descriptive

---

## 📞 Support

If you need help:
1. Check the troubleshooting section
2. Review the requirements
3. Try `simple_recorder.py` as backup
4. Check Streamlit documentation
5. Review app.py for any errors

---

**Happy Recording! 🎬✨**

*ComDetect AI - Intelligent Fraud Detection System*
