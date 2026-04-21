"""
ComDetect AI - Simple Screen Recording Script
Lightweight alternative using Windows built-in tools and OpenCV
No complex automation - just pure screen recording

Requirements: pip install mss opencv-python pillow
"""

import mss
import cv2
import numpy as np
import time
import subprocess
import threading
from datetime import datetime

class SimpleScreenRecorder:
    def __init__(self, output_file="ComDetect_Demo.mp4", fps=30, duration=180):
        """
        Simple screen recorder
        
        Args:
            output_file: Output video filename
            fps: Frames per second
            duration: Recording duration in seconds (default 3 minutes)
        """
        self.output_file = output_file
        self.fps = fps
        self.duration = duration
        self.frames = []
        self.recording = False
        
        # Get primary monitor
        sct = mss.mss()
        self.monitor = sct.monitors[1]  # Primary monitor
        
    def start_app(self):
        """Start the Streamlit app"""
        print("🚀 Starting Streamlit app...")
        self.process = subprocess.Popen(
            ["streamlit", "run", "app.py", "--logger.level=error"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("⏳ Waiting for app to load...")
        time.sleep(6)
        print("✅ App is ready!")
        
    def record_screen(self):
        """Record screen continuously"""
        print(f"📹 Recording screen for {self.duration} seconds...")
        print(f"💾 Saving to: {self.output_file}")
        
        sct = mss.mss()
        start_time = time.time()
        frame_count = 0
        
        while self.recording and (time.time() - start_time) < self.duration:
            # Capture screen
            screenshot = sct.grab(self.monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            
            # Add timestamp
            timestamp = datetime.now().strftime("%H:%M:%S")
            cv2.putText(frame, timestamp, (30, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
            
            self.frames.append(frame)
            frame_count += 1
            
            # Print progress every 30 frames
            if frame_count % 30 == 0:
                elapsed = time.time() - start_time
                print(f"  ⏱️  {elapsed:.1f}s - {frame_count} frames captured")
            
            time.sleep(1 / self.fps)
        
        print(f"✅ Recording complete! ({frame_count} frames)")
        
    def save_video(self):
        """Save frames to video file"""
        if not self.frames:
            print("❌ No frames captured!")
            return False
        
        print(f"\n💾 Saving video file...")
        
        # Get frame dimensions
        height, width = self.frames[0].shape[:2]
        
        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(
            self.output_file,
            fourcc,
            self.fps,
            (width, height)
        )
        
        # Write frames
        total = len(self.frames)
        for i, frame in enumerate(self.frames):
            if (i + 1) % 60 == 0:
                print(f"  Writing: {i+1}/{total} frames...")
            out.write(frame)
        
        out.release()
        
        duration = len(self.frames) / self.fps
        print(f"✅ Video saved successfully!")
        print(f"📊 Video details:")
        print(f"   • Resolution: {width}x{height}")
        print(f"   • Duration: {duration:.1f} seconds")
        print(f"   • FPS: {self.fps}")
        print(f"   • File: {self.output_file}")
        
        return True
    
    def run(self):
        """Run the recording"""
        try:
            self.start_app()
            
            print("\n" + "="*60)
            print("📸 SCREEN RECORDING STARTED")
            print("="*60)
            print("\n🎬 Now perform these actions while recording:")
            print("   1. Face Recognition Login (10s)")
            print("   2. Navigate through Overview tab (20s)")
            print("   3. View Data tab with dataset (20s)")
            print("   4. Go to Results tab")
            print("   5. Click 'Run Analysis' button")
            print("   6. View risk distribution charts")
            print("   7. Apply risk filters (high/medium/low)")
            print("   8. Show voice command help")
            print("   9. Open detection settings")
            print("  10. Show export CSV option")
            print("\n⏰ Recording will automatically stop after 3 minutes")
            print("="*60 + "\n")
            
            input("🟢 Press Enter to START recording... ")
            
            self.recording = True
            record_thread = threading.Thread(target=self.record_screen)
            record_thread.start()
            record_thread.join()
            
            self.save_video()
            
            print("\n🎉 Done! Your demo video is ready.")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
        finally:
            if hasattr(self, 'process'):
                self.process.terminate()
                print("✅ App closed")

def main():
    print("\n" + "="*60)
    print("🎬 ComDetect AI - Simple Screen Recorder")
    print("="*60)
    
    print("\n📋 This will record your screen for 3 minutes while you demo:")
    print("   ✓ Face recognition login")
    print("   ✓ System navigation & tabs")
    print("   ✓ Fraud analysis features")
    print("   ✓ Data visualization")
    print("   ✓ Voice commands")
    print("   ✓ Risk filtering")
    print("   ✓ Export functionality")
    
    print("\n✅ Requirements:")
    print("   • Install: pip install mss opencv-python")
    print("   • Camera available for face login")
    print("   • Good internet (not required for recording)")
    
    print("\n" + "="*60)
    
    recorder = SimpleScreenRecorder(
        output_file="ComDetect_Demo.mp4",
        fps=30,
        duration=180  # 3 minutes
    )
    recorder.run()

if __name__ == "__main__":
    main()
