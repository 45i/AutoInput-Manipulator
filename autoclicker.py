import pyautogui
import time
a = int(input("Clicks: "))
time.sleep(5)
pyautogui.click(clicks=a, interval=0.2, button='left')
