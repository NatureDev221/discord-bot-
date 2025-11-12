import pyautogui as auto 
import time

try:
    time.sleep(1)
    while True:
        auto.write('Whats up')
        auto.press('Enter')
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by user (Ctrl+C)")        
