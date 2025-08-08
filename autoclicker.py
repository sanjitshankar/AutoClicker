import pyautogui
import time

interval = 0.5  # seconds between clicks

print("Auto clicker starting in 3 seconds. Move your mouse where you want to click...")
time.sleep(3)

try:
    while True:
        pyautogui.click()
        time.sleep(interval)
except KeyboardInterrupt:
    print("Stopped")
