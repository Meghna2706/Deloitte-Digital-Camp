"""
ComDetect AI - App Demo Recorder Script
Records a video demonstration of the Streamlit application
with all features including face login, voice commands, analysis, etc.

Requirements: pip install pyautogui mss opencv-python pillow imageio imageio-ffmpeg
"""

import pyautogui
import mss
import cv2
import numpy as np
import time
import subprocess
import os
from PIL import Image, ImageDraw, ImageFont
import threading

class AppDemoRecorder:
    def __init__(self, output_file="ComDetect_Demo.mp4", fps=24, screen_index=0):
        """
        Initialize the demo recorder
        
        Args:
            output_file: Name of the output video file
            fps: Frames per second for the recording
            screen_index: Screen index to record (0 for primary)
        """
        self.output_file = output_file
        self.fps = fps
        self.frame_width = 1920
        self.frame_height = 1080
        self.recording = False
        self.frames = []
        self.monitor = {"top": 0, "left": 0, "width": self.frame_width, "height": self.frame_height}
        
    def start_streamlit_app(self):
        """Start the Streamlit app in background"""
        print("🚀 Starting Streamlit app...")
        self.streamlit_process = subprocess.Popen(
            ["streamlit", "run", "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(5)  # Wait for app to start
        print("✅ Streamlit app started")
        
    def capture_screen(self):
        """Capture screen frames"""
        print("📹 Starting screen capture...")
        sct = mss.mss()
        
        while self.recording:
            # Capture screen
            screenshot = sct.grab(self.monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            self.frames.append(frame)
            time.sleep(1 / self.fps)
        
        print(f"✅ Captured {len(self.frames)} frames")
        
    def click(self, x, y, duration=0.2):
        """Click at position"""
        pyautogui.click(x, y, duration=duration)
        time.sleep(0.5)
        
    def type_text(self, text, interval=0.05):
        """Type text slowly"""
        pyautogui.typewrite(text, interval=interval)
        time.sleep(0.5)
        
    def key_press(self, key, repeat=1):
        """Press keyboard key"""
        for _ in range(repeat):
            pyautogui.press(key)
            time.sleep(0.3)
    
    def move_mouse(self, x, y, duration=1):
        """Move mouse to position"""
        pyautogui.moveTo(x, y, duration=duration)
        time.sleep(0.5)
    
    def add_text_overlay(self, frame, text, position=(50, 50), fontsize=40, color=(0, 255, 0)):
        """Add text overlay to frame"""
        cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 
                   fontsize/20, color, 2, cv2.LINE_AA)
        return frame
    
    def run_demo_sequence(self):
        """Run the full demo sequence"""
        print("\n" + "="*60)
        print("🎬 STARTING DEMO RECORDING")
        print("="*60)
        
        # Start recording in separate thread
        self.recording = True
        capture_thread = threading.Thread(target=self.capture_screen)
        capture_thread.daemon = True
        capture_thread.start()
        
        # Wait a moment for first frame
        time.sleep(2)
        
        print("\n📍 SCENE 1: Face Recognition Login")
        print("-" * 40)
        print("⏱️  Duration: ~15 seconds")
        print("Showing: Face recognition interface")
        time.sleep(10)
        
        # Simulate clicking "Start Camera & Login" button
        print("Clicking Start Camera button...")
        self.click(960, 500)  # Center of screen
        time.sleep(5)
        
        print("\n📍 SCENE 2: Successfully Logged In")
        print("-" * 40)
        print("⏱️  Duration: ~10 seconds")
        print("Showing: Main dashboard after successful face detection")
        time.sleep(10)
        
        print("\n📍 SCENE 3: Overview Tab")
        print("-" * 40)
        print("⏱️  Duration: ~15 seconds")
        print("Showing: System features and fraud detection pillars")
        
        # Click Overview button
        self.click(400, 300)  # Overview button area
        time.sleep(5)
        
        # Scroll down to show all pillars
        for _ in range(3):
            pyautogui.scroll(-3)
            time.sleep(2)
        
        print("\n📍 SCENE 4: Data Tab")
        print("-" * 40)
        print("⏱️  Duration: ~15 seconds")
        print("Showing: Dataset with transaction information")
        
        # Click Data button
        self.click(960, 300)  # Data button area
        time.sleep(5)
        
        # Scroll to see full dataset
        for _ in range(2):
            pyautogui.scroll(-3)
            time.sleep(2)
        
        print("\n📍 SCENE 5: Voice Command Demo")
        print("-" * 40)
        print("⏱️  Duration: ~10 seconds")
        print("Showing: Voice command panel with examples")
        
        # Click help expander
        self.click(500, 400)
        time.sleep(5)
        
        print("\n📍 SCENE 6: Results Tab - Analysis")
        print("-" * 40)
        print("⏱️  Duration: ~20 seconds")
        print("Showing: Fraud detection analysis and results")
        
        # Click Results button
        self.click(1520, 300)  # Results button area
        time.sleep(3)
        
        # Click Analyze button
        self.click(960, 350)  # Analyze button area
        time.sleep(10)
        
        # Scroll to see metrics
        for _ in range(2):
            pyautogui.scroll(-3)
            time.sleep(1.5)
        
        print("\n📍 SCENE 7: Risk Distribution Charts")
        print("-" * 40)
        print("⏱️  Duration: ~15 seconds")
        print("Showing: Risk distribution pie chart and bar chart")
        
        time.sleep(10)
        
        # Scroll more to see charts
        for _ in range(2):
            pyautogui.scroll(-3)
            time.sleep(2)
        
        print("\n📍 SCENE 8: Risk Filtering")
        print("-" * 40)
        print("⏱️  Duration: ~10 seconds")
        print("Showing: High risk user filtering")
        
        # Scroll back up to show filtering options
        for _ in range(3):
            pyautogui.scroll(3)
            time.sleep(1)
        
        time.sleep(5)
        
        print("\n📍 SCENE 9: Detection Settings")
        print("-" * 40)
        print("⏱️  Duration: ~15 seconds")
        print("Showing: Configurable fraud detection thresholds")
        
        # Scroll up to sidebar
        pyautogui.scroll(10)
        time.sleep(2)
        
        # Click on settings expander
        self.click(200, 300)
        time.sleep(8)
        
        print("\n📍 SCENE 10: Export Functionality")
        print("-" * 40)
        print("⏱️  Duration: ~5 seconds")
        print("Showing: CSV export option for results")
        
        # Scroll down to see export button
        for _ in range(2):
            pyautogui.scroll(-2)
            time.sleep(1)
        
        time.sleep(5)
        
        print("\n📍 SCENE 11: Logout & Summary")
        print("-" * 40)
        print("⏱️  Duration: ~10 seconds")
        print("Showing: Logout button and final summary")
        
        # Scroll to top
        for _ in range(5):
            pyautogui.scroll(5)
            time.sleep(0.5)
        
        time.sleep(5)
        
        print("\n" + "="*60)
        print("🎬 RECORDING COMPLETE")
        print("="*60)
        
        # Stop recording
        self.recording = False
        capture_thread.join()
        
    def save_video(self):
        """Save recorded frames as video file"""
        if not self.frames:
            print("❌ No frames captured!")
            return False
        
        print(f"\n💾 Saving video as {self.output_file}...")
        print(f"📊 Total frames: {len(self.frames)}")
        print(f"⏱️  Video duration: ~{len(self.frames) / self.fps:.1f} seconds")
        
        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(
            self.output_file,
            fourcc,
            self.fps,
            (self.frame_width, self.frame_height)
        )
        
        # Write frames
        for i, frame in enumerate(self.frames):
            if i % 100 == 0:
                print(f"  Writing frame {i}/{len(self.frames)}...")
            out.write(frame)
        
        out.release()
        print(f"✅ Video saved successfully!")
        print(f"📁 Location: {os.path.abspath(self.output_file)}")
        return True
    
    def run(self):
        """Run the complete demo recording process"""
        try:
            self.start_streamlit_app()
            self.run_demo_sequence()
            self.save_video()
            print("\n🎉 Demo recording complete! Check your project folder for ComDetect_Demo.mp4")
        except Exception as e:
            print(f"\n❌ Error during recording: {e}")
        finally:
            # Cleanup
            if hasattr(self, 'streamlit_process'):
                self.streamlit_process.terminate()
                print("✅ Streamlit app terminated")

def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("🎬 ComDetect AI - App Demo Recorder")
    print("="*60)
    print("\n📋 This script will:")
    print("  1. Start the Streamlit application")
    print("  2. Record screen for ~2-3 minutes")
    print("  3. Demonstrate all major features:")
    print("     ✓ Face recognition login")
    print("     ✓ System overview")
    print("     ✓ Data viewing")
    print("     ✓ Fraud analysis")
    print("     ✓ Risk visualization")
    print("     ✓ Voice command examples")
    print("     ✓ Risk filtering")
    print("     ✓ Configurable settings")
    print("     ✓ Export functionality")
    print("  4. Save as MP4 video file")
    print("\n⚠️  Make sure:")
    print("  • Camera is available (for face detection)")
    print("  • Python packages installed: pip install pyautogui mss opencv-python pillow")
    print("  • You're in the project directory")
    
    input("\n🟢 Press Enter to start recording... ")
    
    recorder = AppDemoRecorder()
    recorder.run()

if __name__ == "__main__":
    main()
