import pyautogui
import time

time.sleep(4)  
pyautogui.moveTo(100, 100, duration=1)  # ADJUST ACCODING TO YOURSELF
pyautogui.click()  
pyautogui.write("Hello World!", interval=0.1)  # TYPE OF YOUR OWN TEXT
