# take_screenshot.py
import os

def take_screenshot(speak):
    """Take a screenshot and save it."""
    screenshot_name = "screenshot.png"
    os.system(f"scrot {screenshot_name}")  # Works on Linux. Use `pyautogui.screenshot()` for Windows.
    speak("Screenshot taken successfully.")
