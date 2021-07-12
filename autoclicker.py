import pyautogui
import time

e= Exception
try:
    a = int(input("Clicks: "))
    b=input("Which Mouse Button?: (React with 'left' or 'right')")
    b_split= b.lower().split()
    time.sleep(5)
    pyautogui.click(clicks=a, interval=0.2, button=b_split[0])
except pyautogui.FailSafeException:
    print("PyAutoGui triggered a FailSafe exception \n"
          "Reason: Mouse moved to the corner of the screen")
