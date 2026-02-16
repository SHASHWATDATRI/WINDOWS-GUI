import pyautogui
import time
print("=now your num lock key will be hit again and again...to stop press ctrl+c=")
time.sleep(3) 
try:
    while True:
        pyautogui.press('capslock')  
        time.sleep(1.0)
except KeyboardInterrupt:
     print("\nnow the code is stoped..dontworry")