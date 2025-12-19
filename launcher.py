#!/usr/bin/env python3
"""
Quick launcher for Quantum Go application
"""
import subprocess
import sys
import os

def main():
    print("=" * 50)
    print("  ⚛️ Quantum Go - ZidanAI Launcher")
    print("=" * 50)
    print()
    
    # Check if dependencies are installed
    print("[1/2] Checking dependencies...")
    try:
        import flask
        import qiskit
        import matplotlib
        print("✓ All dependencies found!")
    except ImportError as e:
        print(f"✗ Missing dependency: {e.name}")
        print("\nInstalling dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print()
    print("[2/2] Starting Flask application...")
    print()
    print("=" * 50)
    print("  Server starting at: http://localhost:5000")
    print("  Press Ctrl+C to stop")
    print("=" * 50)
    print()
    
    # Run the app
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n\nServer stopped. Goodbye!")

if __name__ == "__main__":
    main()
